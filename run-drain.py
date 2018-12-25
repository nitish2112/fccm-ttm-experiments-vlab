import os
import sys

emul = 0

if (emul):
  aoc_opt = "-march=emulator"
else:
  aoc_opt = "-time time.out -time-passes -regtest_mode -v -g -fpc -fp-relaxed -report"

# Note: II has to be 1 else the compute buffer cannot be implemented as rotating register

if (emul):
  I_BITS, II_BITS, III_BITS = 0,0,1
  J_BITS, JJJ_BITS = 0,1
  K_BITS, KKK_BITS = 0,1
  L_BITS, LL_BITS, LLL_BITS = 1,1,1
  
  JJ = 2
  KK = 2

else:
  I_BITS, II_BITS, III_BITS = 3,0,4
  J_BITS, JJJ_BITS = 2,4
  K_BITS, KKK_BITS = 2,4
  L_BITS, LL_BITS, LLL_BITS = 2,1,4
  
  JJ = 8
  KK = 9

I,J,K,L = 2**I_BITS, 2**J_BITS, 2**K_BITS, 2**L_BITS
II, LL = 2**II_BITS, 2**LL_BITS
III, JJJ, KKK, LLL = 2**III_BITS, 2**JJJ_BITS, 2**KKK_BITS, 2**LLL_BITS

print I,J,K,L
print II,JJ,KK,LL
print III,JJJ,KKK,LLL

aocx_name = "ttm-drain"

suffix = "{}x{}".format(JJ,KK)

command = "qsub-aoc {} -D_I_={} -D_J_={} -D_K_={} -D_L_={} -D_II_={} -D_JJ_={} -D_KK_={} -D_LL_={} -D_III_={} -D_JJJ_={} -D_KKK_={} -D_LLL_={} -D_I_BITS={} -D_II_BITS={} -D_III_BITS={} -D_J_BITS={} -D_JJJ_BITS={} -D_K_BITS={} -D_KKK_BITS={} -D_L_BITS={} -D_LL_BITS={} -D_LLL_BITS={} -DFLOAT_VEC=float{} -DLOG_FLOAT_VEC_SZ={} {}.cl -o {}_{}.aocx 2>&1 | tee -a run.log".format(aoc_opt,I,J,K,L,II,JJ,KK,LL,III,JJJ,KKK,LLL,I_BITS,II_BITS,III_BITS,J_BITS,JJJ_BITS, K_BITS,KKK_BITS, L_BITS, LL_BITS, LLL_BITS, LLL, LLL_BITS, aocx_name,aocx_name, suffix)

os.system("echo "+command)
os.system(command)
