from robotpkg.movement import forwar
from robotpkg.battery import check
from robotpkg.safety import safe

print(check(15))
print(safe(12))
forwar(1.5)
