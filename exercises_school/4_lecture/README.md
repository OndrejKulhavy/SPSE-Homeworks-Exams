# Assignment - lecture 4
`Monday, October , 2023`

## Task 4.3
[Python Script](./3_task.py)

Napište metodu password_policy_check(username, password), která přijme na vstupu heslo a zkontroluje, jestli heslo odpovídá následujícím parametrům pomocí regulárních výrazů:

- Heslo musí být minimálně 10 znaků.
- Heslo musí obsahovat alespoň jedno číslo.
- Heslo musí obsahovat alespoň jedno písmeno malé a jedno písmeno velké abecedy
- Heslo musí obsahovat alespoň nečíselný a nepísmený znak.
- Heslo nesmí obsahovat username.
- Heslo nesmí obsahovat jakýkkoli podřetězec username delší než 3 znaky.


Nápověda

Co je to řetězec a podřetězec? To je stejné jako množina a podmnožina. Je-li například řetězec "AHOJ SVETE" jeho podřetězec ja například "HOJ", nebo "AHOJ", nebo "ETE"... prostě podmnožina těch písmenek se zachováním pořadí.

---

## Task 4.5
[Python Script](./5_task.py)

Napište metodu, která bude realizovat úpravu emailu účtu v rámci již hotové desktopové aplikace. Na vstupu přijme dva argumenty: username a email. Metoda vrátí SQL příkaz pro úpravu profilu účtu v relačním databázovém systému, například Microsoft SQL Server u databázové tabulky, která je definována takto:

CREATE TABLE ACCOUNT (

  ID INT NOT NULL IDENTITY  PRIMARY KEY,

  USERNAME VARCHAR(100) NOT NULL,

  EMAIL VARCHAR(255) NOT NULL

);

Pro otestování je třeba SQL string vypsat na obrazovku a otestovat pomocí klienta, například SQL Server Mangement Studio

---

## Task 4.9
[Python Script](./9_task.py)

Napište metodu s názvem person_search(xml) , která na vstupu přijme XML z rozhraní ARES (například jako string) a vypíše všechny fyzické osoby, které jsou v záznamu o firmě uvedené:

https://wwwinfo.mfcr.cz/cgi-bin/ares/darv_rzp.cgi?ico=27074358
