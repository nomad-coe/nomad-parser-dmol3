package eu.nomad_lab.parsers

import eu.nomad_lab.{ parsers, DefaultPythonInterpreter }
import org.scalacheck.Properties
import org.specs2.mutable.Specification
import org.{ json4s => jn }

object Dmol3ParserSpec extends Specification {
  "Dmol3ParserTest" >> {
    "test with h2o.outmol" >> {
      "test with json-events" >> {
        ParserRun.parse(Dmol3Parser, "parsers/dmol3/test/examples/h2o.outmol", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(Dmol3Parser, "parsers/dmol3/test/examples/h2o.outmol", "json") must_== ParseResult.ParseSuccess
      }
    }
  }
}
