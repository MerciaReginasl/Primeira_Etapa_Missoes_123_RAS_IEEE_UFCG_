//PROCESSO SELETIVO CAPITULO RAS - IEEE UFCG
//CANDIDATA: MÉRCIA REGINA DA SILVA

//MISSÃO 1.0: PRIMEIRO CIRCUITO ELETRÔNICO 
//ASCENDENDO UM LED COM ARDUINO

//PROJETO: SEMÁFORO COM ARDUINO

//Define os pinos 13, 12 e 11 como OUTPUT como a variável de saída

int vermelho = 13;
int amarelo =12;
int verde = 11;

//
void setup(){
  pinMode(vermelho, OUTPUT);
  pinMode(amarelo, OUTPUT);
  pinMode(verde, OUTPUT); 
}

//Sequência dos comandos: LOW: BAIXO (ACENDE) ou HIGH: ALTO (APAGA)
void loop(){
  
  digitalWrite(vermelho, LOW);
  digitalWrite(amarelo, HIGH);
  digitalWrite(verde, LOW);
  
  delay(4000); //Tempo de espera 4 Segundos (4 s). 

  digitalWrite(amarelo, LOW);
  digitalWrite(vermelho, HIGH);

  delay(4000); //Tempo de espera 4 Segundos (4 s). 
  
  digitalWrite(verde, HIGH);
  digitalWrite(vermelho, LOW);
  
}
  delay(5000); //Tempo de espera 2 Segundos (5 s). 
}
  

