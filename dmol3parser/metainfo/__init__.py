import sys
from nomad.metainfo import Environment
from nomad.metainfo.legacy import LegacyMetainfoEnvironment
import dmol3parser.metainfo.dmol3
import nomad.datamodel.metainfo.common
import nomad.datamodel.metainfo.public
import nomad.datamodel.metainfo.general

m_env = LegacyMetainfoEnvironment()
m_env.m_add_sub_section(Environment.packages, sys.modules['dmol3parser.metainfo.dmol3'].m_package)  # type: ignore
m_env.m_add_sub_section(Environment.packages, sys.modules['nomad.datamodel.metainfo.common'].m_package)  # type: ignore
m_env.m_add_sub_section(Environment.packages, sys.modules['nomad.datamodel.metainfo.public'].m_package)  # type: ignore
m_env.m_add_sub_section(Environment.packages, sys.modules['nomad.datamodel.metainfo.general'].m_package)  # type: ignore
