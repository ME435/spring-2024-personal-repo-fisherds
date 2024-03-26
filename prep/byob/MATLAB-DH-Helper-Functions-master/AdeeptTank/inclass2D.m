clc
A1 = create_A_matrix(2, 3, 0, 0);
A2 = create_A_matrix(3, 0, 0, 0);

T0_1 = A1;
T0_2 = A1 * A2;

ptAOnLink1 = [0;0;2;1];
expectedPtAOnLink0 = [2;0;5;1]
actualPtAOnLink0 = T0_1 * ptAOnLink1

ptBOnLink2 = [1;0;1;1];
expectedPtBOnLink0 = [6;0;4;1]
actualPtBOnLink0 = T0_2 * ptBOnLink2




