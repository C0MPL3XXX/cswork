Names = ['May', 'Eri', 'Elen', 'Rit', 'Rato', 'More', 'Epi', 'Ent', 'Ronal', 'Bob']
Grades = [99, 55, 77, 45, 89, 98, 76, 46, 33, 75]

def printing_students():
     Min = Grades[0]

     Max = Grades[0]

     Av = 0

     Average = 0

     M = 0

     Best = '0'

     Worst = '0'

     print('------------------------')
     print('STUDENT LIST')
     print('------------------------')

     for M in range(0, 10):
         print('No ', M + 1, '--Student    ', Names[M], '          --Mark ',
               Grades[M])

     for M in range(0, 10):
         if Min >= Grades[M]:
             Min = Grades[M]
             Worst = Names[M]

     for M in range(0, 10):
         Av = Av + Grades[M]
         if Max <= Grades[M]:
             Max = Grades[M]
             Best = Names[M]
     Average = Av/10

     print('------------------------')
     print('Statistics')
     print('------------------------')
     print('Minimum mark', str(Min), ' Student ', str(Worst))
     print('Maximum mark', str(Max), ' Student ', str(Best))
     print('Class average ', str(Average))

printing_students()
