% 2D by hand example

clc
ptAOnLink1 = [0;0;2;1];
ptBOnLink2 = [1;0;1;1];

% Calc A1
A1 = create_A_matrix(2, 3, 0, 0);
% Calc A2
A2 = create_A_matrix(3, 0, 0, 0);

% Calc T0_1 = A1
T0_1 = A1;
% Calc T0_2 = A1 * A2
T0_2 = A1 * A2;

% Actual points  T0_1 * ptAOnLink1
% Actual points  T0_2 * ptBOnLink2

actualAOnLink0 = T0_1 * ptAOnLink1
expectedAOnLink0 = [2;0;5;1]
actualBOnLink0 = T0_2 * ptBOnLink2
expectedBOnLink0 = [6;0;4;1]


