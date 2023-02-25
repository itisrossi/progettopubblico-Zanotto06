function fattoriale(numero){
    if (numero<2){
        return 1;
    }
    return numero*fattoriale(numero-1);
}