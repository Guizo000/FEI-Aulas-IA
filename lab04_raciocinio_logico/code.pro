/*
Queries:
1) -> pai(josé, joão)
2) -> mãe(maria, F)
3) -> primos_ou_primas(paulo, P)
4) -> sobrinhos_ou_sobrinhas(T, S)
5) -> ascendente(X, carlos)
6) -> irmã(helena, I)
*/

%M é mãe de F
mãe(M, F) :-
    progenitor(M, F),
    mulher(M).

%P é pai de F
pai(P, F) :-
    progenitor(P, F),
    homem(P).

%X é irmã de Y, sendo Y irmão OU irmã de X
irmã(X, Y) :-
    mãe(M, X), 
    mãe(M, Y),
	mulher(X),
    X \= Y.

%X é irmão de Y, sendo Y irmão OU irmã de X
irmão(X, Y) :-
    mãe(M, X), 
    mãe(M, Y),
    homem(X),
    X \= Y.

primos_ou_primas(X, Y) :-
    (   
	(mãe(M, X), progenitor(P, Y), irmã(M, P));
    (pai(P1, X), progenitor(P2, Y), irmão(P1, P2))
    ),
    X \= Y.

%X é tio ou tia de Y, sendo Y sobrinho ou sobrinha de X
sobrinhos_ou_sobrinhas(X, Y) :-
    progenitor(P, Y),
    (irmão(X, P) ; irmã(X, P)),
    X \= Y.

% X é ascendente de Y se X for progenitor direto de Y
ascendente(X, Y) :- 
    progenitor(X, Y).

% X é ascendente de Y se existe um Z que é progenitor de Y, 
% e X é ascendente desse Z.
ascendente(X, Y) :- 
    progenitor(Z, Y), 
    ascendente(X, Z).
    
mulher(ana).
mulher(maria).
mulher(helena).
mulher(joana).

homem(josé).
homem(joão).
homem(paulo).
homem(carlos).

progenitor(josé, joão).
progenitor(josé, ana).
progenitor(maria, joão).
progenitor(maria, ana).
progenitor(ana, helena).
progenitor(ana, joana).
progenitor(joão, paulo).
progenitor(helena, carlos).
progenitor(paulo, carlos).