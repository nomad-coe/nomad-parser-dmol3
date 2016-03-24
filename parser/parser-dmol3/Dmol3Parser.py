import setup_paths
import numpy as np
import nomadcore.ActivateLogging
from nomadcore.caching_backend import CachingLevel
from nomadcore.simple_parser import AncillaryParser, mainFunction
from nomadcore.simple_parser import SimpleMatcher as SM
from Dmol3Common import get_metaInfo
import logging, os, re, sys

############################################################
# This is the parser for the main file of dmol3.
############################################################


############################################################
###############(1) PARSER CONTEXT CLASS  ###################
############################################################
logger = logging.getLogger("nomad.dmol3Parser") 

class Dmol3ParserContext(object):

    def __init__(self):
        self.functionals                       = []


    def initialize_values(self):
        """Initializes the values of certain variables.

        This allows a consistent setting and resetting of the variables,
        when the parsing starts and when a section_run closes.
        """

    def startedParsing(self, fInName, parser):
        """Function is called when the parsing starts.

        Get compiled parser, filename and metadata.

        Args:
            fInName: The file name on which the current parser is running.
            parser: The compiled parser. Is an object of the class SimpleParser in nomadcore.simple_parser.py.
        """
        self.parser = parser
        self.fName = fInName
        # save metadata
        self.metaInfoEnv = self.parser.parserBuilder.metaInfoEnv
        # allows to reset values if the same superContext is used to parse different files
        self.initialize_values()


# Here we add info about the XC functional and relativistic treatment
    def onClose_section_method(self, backend, gIndex, section):

        # Push the functional string into the backend
        backend.addValue('XC_functional', self.functionals)


                


#############################################################
#################(2) MAIN PARSER STARTS HERE  ###############
#############################################################

def build_Dmol3MainFileSimpleMatcher():
    """Builds the SimpleMatcher to parse the main file of dmol3.

    First, several subMatchers are defined, which are then used to piece together
    the final SimpleMatcher.
    SimpleMatchers are called with 'SM (' as this string has length 4,
    which allows nice formating of nested SimpleMatchers in python.

    Returns:
       SimpleMatcher that parses main file of dmol3. 
    """

   ########################################
    # submatcher for section method
    calculationMethodSubMatcher = SM(name = 'calculationMethods',
        startReStr = r"\sFunctional\s*\:",
        forwardMatch = True,
        sections = ["section_method"],
        subMatchers = [

           SM(name = "dmol3XC",
              startReStr = r"\sFunctional\s*\:",
              forwardMatch = True,
              sections = ["dmol3_section_functionals"],
              subMatchers = [

                 SM(r"\sFunctional\s* *(?P<dmol3_functional_name> [A-Za-z0-9() ]*)")

                             ]), # CLOSING dmol3_section_functionals

                      ]) # CLOSING SM calculationMethods


    ########################################
    # return main Parser
    return SM (name = 'Root',

        startReStr = "",
        forwardMatch = True,
        weak = True,
        subMatchers = [
        SM (name = 'NewRun',
            startReStr = r"\s*Materials Studio DMol\^3 version 3.0",
            endReStr = r"\s*DMol3 job finished successfully",
            repeats = True,
            required = True,
            forwardMatch = True,
            sections = ['section_run'],
            subMatchers = [


               SM(name = 'ProgramHeader',
                  startReStr = r"\s*Materials Studio DMol\^3 version 3.0",
                  subMatchers = [
#castap : on Fri, 19 Feb 2016 13:44:46 +0000
#dmol3  : compiled on Nov 12 2003 20:18:37 
                     SM(r"\s compiled on\s(?P<dmol3_program_compilation_date>[a-zA-Z,\s0-9]*)\s *(?P<dmol3_program_compilation_time>[0-9:]*)")
                                  ]), # CLOSING SM ProgramHeader

             calculationMethodSubMatcher  # section_method
          
           ]) # CLOSING SM NewRun  

        ]) # END Root

def get_cachingLevelForMetaName(metaInfoEnv):
    """Sets the caching level for the metadata.

    Args:
        metaInfoEnv: metadata which is an object of the class InfoKindEnv in nomadcore.local_meta_info.py.

    Returns:
        Dictionary with metaname as key and caching level as value. 
    """
    # manually adjust caching of metadata
    cachingLevelForMetaName = {
                                'eigenvalues_eigenvalues': CachingLevel.Cache,
                                'eigenvalues_kpoints':CachingLevel.Cache
                                }

    # Set caching for temparary storage variables
    for name in metaInfoEnv.infoKinds:
        if (   name.startswith('dmol3_store_')
            or name.startswith('dmol3_cell_')):
            cachingLevelForMetaName[name] = CachingLevel.Cache
    return cachingLevelForMetaName




def main():
    """Main function.

    Set up everything for the parsing of the dmol3 main file and run the parsing.
    """
    # get main file description
    Dmol3MainFileSimpleMatcher = build_Dmol3MainFileSimpleMatcher()
    # loading metadata from nomad-meta-info/meta_info/nomad_meta_info/dmol3.nomadmetainfo.json
    metaInfoPath = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../../nomad-meta-info/meta_info/nomad_meta_info/dmol3.nomadmetainfo.json"))
    metaInfoEnv = get_metaInfo(metaInfoPath)
    # set parser info
    parserInfo = {'name':'dmol3-parser', 'version': '1.0'}
    # get caching level for metadata
    cachingLevelForMetaName = get_cachingLevelForMetaName(metaInfoEnv)
    # start parsing
    mainFunction(mainFileDescription = Dmol3MainFileSimpleMatcher,
                 metaInfoEnv = metaInfoEnv,
                 parserInfo = parserInfo,
                 cachingLevelForMetaName = cachingLevelForMetaName,
                 superContext = Dmol3ParserContext())

if __name__ == "__main__":
    main()

