import numpy as np            # pylint: disable=unused-import
import typing                 # pylint: disable=unused-import
from nomad.metainfo import (  # pylint: disable=unused-import
    MSection, MCategory, Category, Package, Quantity, Section, SubSection, SectionProxy,
    Reference
)
from nomad.metainfo.legacy import LegacyDefinition

from nomad.datamodel.metainfo import public

m_package = Package(
    name='dmol3_nomadmetainfo_json',
    description='None',
    a_legacy=LegacyDefinition(name='dmol3.nomadmetainfo.json'))


class dmol3_section_hirshfeld_population(MSection):
    '''
    Hirshfeld Population Analysis Section
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='dmol3_section_hirshfeld_population'))

    dmol3_hirshfeld_population = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Hirshfeld Population Analysis
        ''',
        a_legacy=LegacyDefinition(name='dmol3_hirshfeld_population'))


class dmol3_section_mulliken_population(MSection):
    '''
    Mulliken Population Analysis Section
    '''

    m_def = Section(validate=False, a_legacy=LegacyDefinition(name='dmol3_section_mulliken_population'))

    dmol3_mulliken_population = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Mulliken Population Analysis
        ''',
        a_legacy=LegacyDefinition(name='dmol3_mulliken_population'))


class section_method(public.section_method):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_method'))

    dmol3_aux_density = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 aux density
        ''',
        a_legacy=LegacyDefinition(name='dmol3_aux_density'))

    dmol3_aux_partition = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        dmol3 aux parition
        ''',
        a_legacy=LegacyDefinition(name='dmol3_aux_partition'))

    dmol3_basis_name = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 basis name
        ''',
        a_legacy=LegacyDefinition(name='dmol3_basis_name'))

    dmol3_calculation_type = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 calculation type
        ''',
        a_legacy=LegacyDefinition(name='dmol3_calculation_type'))

    dmol3_charge = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 system charge
        ''',
        a_legacy=LegacyDefinition(name='dmol3_charge'))

    dmol3_electrostatic_moments = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Electrostatic_Moments
        ''',
        a_legacy=LegacyDefinition(name='dmol3_electrostatic_moments'))

    dmol3_functional_name = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 functional name
        ''',
        a_legacy=LegacyDefinition(name='dmol3_functional_name'))

    dmol3_hirshfeld_analysis = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Hirshfeld_Analysis
        ''',
        a_legacy=LegacyDefinition(name='dmol3_hirshfeld_analysis'))

    dmol3_integration_grid = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 integration grid
        ''',
        a_legacy=LegacyDefinition(name='dmol3_integration_grid'))

    dmol3_kpoints = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Kpoints
        ''',
        a_legacy=LegacyDefinition(name='dmol3_kpoints'))

    dmol3_mulliken_analysis = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Mulliken_Analysis
        ''',
        a_legacy=LegacyDefinition(name='dmol3_mulliken_analysis'))

    dmol3_nuclear_efg = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Nuclear_EFG
        ''',
        a_legacy=LegacyDefinition(name='dmol3_nuclear_efg'))

    dmol3_occupation_name = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Occupation name
        ''',
        a_legacy=LegacyDefinition(name='dmol3_occupation_name'))

    dmol3_occupation_width = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 Occupation width
        ''',
        a_legacy=LegacyDefinition(name='dmol3_occupation_width'))

    dmol3_opt_coordinate_system = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 OPT_Coordinate_System
        ''',
        a_legacy=LegacyDefinition(name='dmol3_opt_coordinate_system'))

    dmol3_opt_displacement_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 OPT_Displacement_Convergence
        ''',
        a_legacy=LegacyDefinition(name='dmol3_opt_displacement_convergence'))

    dmol3_opt_energy_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 OPT_Energy_Convergence
        ''',
        a_legacy=LegacyDefinition(name='dmol3_opt_energy_convergence'))

    dmol3_opt_gdiis = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 OPT_Gdiis
        ''',
        a_legacy=LegacyDefinition(name='dmol3_opt_gdiis'))

    dmol3_opt_gradient_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 OPT_Gradient_Convergence
        ''',
        a_legacy=LegacyDefinition(name='dmol3_opt_gradient_convergence'))

    dmol3_opt_hessian_project = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 OPT_Hessian_Project
        ''',
        a_legacy=LegacyDefinition(name='dmol3_opt_hessian_project'))

    dmol3_opt_iterations = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        dmol3 OPT_Iterations
        ''',
        a_legacy=LegacyDefinition(name='dmol3_opt_iterations'))

    dmol3_opt_max_displacement = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 OPT_Max_Displacement
        ''',
        a_legacy=LegacyDefinition(name='dmol3_opt_max_displacement'))

    dmol3_opt_steep_tol = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 OPT_Steep_Tol
        ''',
        a_legacy=LegacyDefinition(name='dmol3_opt_steep_tol'))

    dmol3_optical_absorption = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Optical_Absorption
        ''',
        a_legacy=LegacyDefinition(name='dmol3_optical_absorption'))

    dmol3_partial_dos = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 Partial_Dos
        ''',
        a_legacy=LegacyDefinition(name='dmol3_partial_dos'))

    dmol3_pseudopotential_name = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 pseudopotential name
        ''',
        a_legacy=LegacyDefinition(name='dmol3_pseudopotential_name'))

    dmol3_rcut = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 atom R_cut
        ''',
        a_legacy=LegacyDefinition(name='dmol3_rcut'))

    dmol3_scf_charge_mixing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 SCF_Charge_Mixing
        ''',
        a_legacy=LegacyDefinition(name='dmol3_scf_charge_mixing'))

    dmol3_scf_density_convergence = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 SCF_Density_Convergence
        ''',
        a_legacy=LegacyDefinition(name='dmol3_scf_density_convergence'))

    dmol3_scf_diis_name = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 SCF_DIIS name
        ''',
        a_legacy=LegacyDefinition(name='dmol3_scf_diis_name'))

    dmol3_scf_diis_number = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 SCF_DIIS number
        ''',
        a_legacy=LegacyDefinition(name='dmol3_scf_diis_number'))

    dmol3_scf_direct = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 SCF_Direct
        ''',
        a_legacy=LegacyDefinition(name='dmol3_scf_direct'))

    dmol3_scf_iterations = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        dmol3 SCF_Iterations
        ''',
        a_legacy=LegacyDefinition(name='dmol3_scf_iterations'))

    dmol3_scf_number_bad_steps = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        dmol3 SCF_Number_Bad_Steps
        ''',
        a_legacy=LegacyDefinition(name='dmol3_scf_number_bad_steps'))

    dmol3_scf_restart = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 SCF_Restart
        ''',
        a_legacy=LegacyDefinition(name='dmol3_scf_restart'))

    dmol3_scf_spin_mixing = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 SCF_Spin_Mixing
        ''',
        a_legacy=LegacyDefinition(name='dmol3_scf_spin_mixing'))

    dmol3_spin_polarization = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 spin polarization
        ''',
        a_legacy=LegacyDefinition(name='dmol3_spin_polarization'))

    dmol3_spin = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        dmol3 number of unpaired electrons
        ''',
        a_legacy=LegacyDefinition(name='dmol3_spin'))

    dmol3_symmetry = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 sysmmetry
        ''',
        a_legacy=LegacyDefinition(name='dmol3_symmetry'))


class section_scf_iteration(public.section_scf_iteration):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_scf_iteration'))

    dmol3_binding_energy_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        dmol3 binding energy at every SCF
        ''',
        a_legacy=LegacyDefinition(name='dmol3_binding_energy_scf_iteration'))

    dmol3_convergence_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 convergence at every SCF
        ''',
        a_legacy=LegacyDefinition(name='dmol3_convergence_scf_iteration'))

    dmol3_number_scf_iteration = Quantity(
        type=np.dtype(np.int32),
        shape=[],
        description='''
        dmol3 iteration number at every SCF
        ''',
        a_legacy=LegacyDefinition(name='dmol3_number_scf_iteration'))

    dmol3_time_scf_iteration = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        dmol3 time at every SCF
        ''',
        a_legacy=LegacyDefinition(name='dmol3_time_scf_iteration'))


class section_eigenvalues(public.section_eigenvalues):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_eigenvalues'))

    dmol3_eigenvalue_eigenvalue = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='joule',
        description='''
        Single eigenvalue
        ''',
        a_legacy=LegacyDefinition(name='dmol3_eigenvalue_eigenvalue'))

    dmol3_eigenvalue_occupation = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        description='''
        Occupation of single eigenfunction
        ''',
        a_legacy=LegacyDefinition(name='dmol3_eigenvalue_occupation'))


class section_system(public.section_system):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_system'))

    dmol3_geometry_atom_labels = Quantity(
        type=str,
        shape=[],
        description='''
        labels of atom
        ''',
        a_legacy=LegacyDefinition(name='dmol3_geometry_atom_labels'))

    dmol3_geometry_atom_positions_x = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        x component of atomic position
        ''',
        a_legacy=LegacyDefinition(name='dmol3_geometry_atom_positions_x'))

    dmol3_geometry_atom_positions_y = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        y component of atomic position
        ''',
        a_legacy=LegacyDefinition(name='dmol3_geometry_atom_positions_y'))

    dmol3_geometry_atom_positions_z = Quantity(
        type=np.dtype(np.float64),
        shape=[],
        unit='meter',
        description='''
        z component of atomic position
        ''',
        a_legacy=LegacyDefinition(name='dmol3_geometry_atom_positions_z'))


class section_run(public.section_run):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_run'))

    dmol3_program_compilation_date = Quantity(
        type=str,
        shape=[],
        description='''
        dmol3 compilation date
        ''',
        a_legacy=LegacyDefinition(name='dmol3_program_compilation_date'))

    dmol3_program_compilation_time = Quantity(
        type=str,
        shape=[],
        description='''
        dmol compilation date
        ''',
        a_legacy=LegacyDefinition(name='dmol3_program_compilation_time'))


class section_single_configuration_calculation(public.section_single_configuration_calculation):

    m_def = Section(validate=False, extends_base_section=True, a_legacy=LegacyDefinition(name='section_single_configuration_calculation'))

    dmol3_section_hirshfeld_population = SubSection(
        sub_section=SectionProxy('dmol3_section_hirshfeld_population'),
        repeats=True,
        a_legacy=LegacyDefinition(name='dmol3_section_hirshfeld_population'))

    dmol3_section_mulliken_population = SubSection(
        sub_section=SectionProxy('dmol3_section_mulliken_population'),
        repeats=True,
        a_legacy=LegacyDefinition(name='dmol3_section_mulliken_population'))


m_package.__init_metainfo__()
