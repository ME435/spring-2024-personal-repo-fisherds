clc
ptAOnLink1 = [0; 0; 2; 1];
ptBOnLink2 = [1; 0; 1; 1];

% Calculate A1
A1 = create_A_matrix(2, 3, 0, 0);
% Calculate A2
A2 = create_A_matrix(3, 0, 0, 0);

% T0_1 = A1
T0_1 = A1;
% T0_2 = A1 * A2
T0_2 = A1 * A2;

% Actual A on link 0   T0_1 * ptAOnLink1
actualPtAOnLink0 = T0_1 * ptAOnLink1
expectedPtAOnLink0 = [2; 0; 5; 1]

% Actual B on link 0   T0_2 * ptBOnLink2
actualPtBOnLink0 = T0_2 * ptBOnLink2
expectedPtBOnLink0 = [6; 0; 4; 1]
