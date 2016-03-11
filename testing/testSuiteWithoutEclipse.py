# -*- coding: utf-8 -*-.

import unittest
import os

os.chdir("testing")

from testAccions                import *
from testActorsUserHistory      import *
from testBackLog                import *
from testCategory               import *
from testHistory                import *
from testLogin                  import *
from testObjective              import *
from testObjectivesUserHistory  import *
from testRole                   import *
from testTask                   import *
from testUser                   import *
from testArchivo                import *
from testPrueba                 import *

if __name__ == '__main__':
    unittest.main()

