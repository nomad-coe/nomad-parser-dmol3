/*
 * Copyright 2016-2018 Fawzi Mohamed, Honghui Shang, Ankit Kariryaa
 * 
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 * 
 *     http://www.apache.org/licenses/LICENSE-2.0
 * 
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 */

package eu.nomad_lab.parsers

import eu.{ nomad_lab => lab }
import eu.nomad_lab.DefaultPythonInterpreter
import org.{ json4s => jn }
import scala.collection.breakOut

object Dmol3Parser extends SimpleExternalParserGenerator(
  name = "Dmol3Parser",
  parserInfo = jn.JObject(
    ("name" -> jn.JString("Dmol3Parser")) ::
      ("parserId" -> jn.JString("Dmol3Parser" + lab.Dmol3VersionInfo.version)) ::
      ("versionInfo" -> jn.JObject(
        ("nomadCoreVersion" -> jn.JObject(lab.NomadCoreVersionInfo.toMap.map {
          case (k, v) => k -> jn.JString(v.toString)
        }(breakOut): List[(String, jn.JString)])) ::
          (lab.Dmol3VersionInfo.toMap.map {
            case (key, value) =>
              (key -> jn.JString(value.toString))
          }(breakOut): List[(String, jn.JString)])
      )) :: Nil
  ),
  mainFileTypes = Seq("text/.*"),
  mainFileRe = """\s*============================================*\s*
\s*Materials Studio DMol\^3 version (?<version>[-0-9.a-zA-Z_]+)\s*
""".r,
  cmd = Seq(DefaultPythonInterpreter.pythonExe(), "${envDir}/parsers/dmol3/parser/parser-dmol3/Dmol3Parser.py",
    "--uri", "${mainFileUri}", "${mainFilePath}"),
  resList = Seq(
    "parser-dmol3/Dmol3Parser.py",
    "parser-dmol3/Dmol3Common.py",
    "parser-dmol3/setup_paths.py",
    "nomad_meta_info/public.nomadmetainfo.json",
    "nomad_meta_info/common.nomadmetainfo.json",
    "nomad_meta_info/meta_types.nomadmetainfo.json",
    "nomad_meta_info/dmol3.nomadmetainfo.json"
  ) ++ DefaultPythonInterpreter.commonFiles(),
  dirMap = Map(
    "parser-dmol3" -> "parsers/dmol3/parser/parser-dmol3",
    "nomad_meta_info" -> "nomad-meta-info/meta_info/nomad_meta_info",
    "python" -> "python-common/common/python/nomadcore"
  ) ++ DefaultPythonInterpreter.commonDirMapping(),
  metaInfoEnv = Some(lab.meta.KnownMetaInfoEnvs.dmol3)
)
