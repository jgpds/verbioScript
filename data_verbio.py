list_of_words = ["ADEMIR", "ALTAIR", "ITAMAR", "JUNIOR", "NAVIER", "TAYLOR", "VICTOR", "ABAFAR", "ABALAR", "ABANAR",
                 "ABATER", "ABLUIR", "ABOLIR", "ABSTER", "ABUSAR", "ACABAR", "ACATAR", "ACENAR", "ACUDIR", "ACUSAR",
                 "ADERIR", "ADITAR", "ADORAR", "ADOTAR", "ADOCAR", "ADUBAR", "ADULAR", "ADVIER", "AFAGAR", "AFANAR",
                 "AFAZER", "AFERIR", "AFETAR", "AFINAR", "AFIXAR", "AFLUIR", "AFOBAR", "AFOFAR", "AFOGAR", "AFORAR",
                 "AGITAR", "AGUIAR", "AGUCAR", "AJUDAR", "ALAGAR", "ALEGAR", "ALHEAR", "ALIJAR", "ALISAR", "ALOCAR",
                 "ALOJAR", "ALTEAR", "ALUDIR", "ALUGAR", "AMADOR", "AMIGAR", "AMIMAR", "AMOLAR", "ANELAR", "ANEXAR",
                 "ANIMAR", "ANOTAR", "ANSIAR", "ANULAR", "APAGAR", "APARAR", "APEGAR", "APELAR", "APENAR", "APESAR",
                 "APITAR", "APOIAR", "APURAR", "AREJAR", "ARGUIR", "ARPOAR", "ARREAR", "ARRIAR", "ASILAR", "ASSEAR",
                 "ASSOAR", "ATACAR", "ATINAR", "ATIRAR", "ATIVAR", "ATIVER", "ATICAR", "ATOLAR", "ATRAIR", "ATURAR",
                 "AUTUAR", "AVISAR", "AVIVAR", "AXILAR", "AZARAR", "AZEDAR", "AZULAR", "ACUCAR", "BAILAR", "BAIXAR",
                 "BALEAR", "BANCAR", "BANHAR", "BARRAR", "BASEAR", "BASTAR", "BEIJAR", "BEIRAR", "BENZER", "BERRAR",
                 "BILHAR", "BILIAR", "BLEFAR", "BOBEAR", "BORDAR", "BORRAR", "BOXEAR", "BRADAR", "BRAMAR", "BRAMIR",
                 "BRECAR", "BRIGAR", "BROCAR", "BROTAR", "BRUNIR", "BUNDAR", "BURLAR", "BUSCAR", "BEQUER", "CALCAR",
                 "CALHAR", "CALCAR", "CANSAR", "CANTAR", "CANTOR", "CAPTAR", "CARPIR", "CASSAR", "CASTOR", "CAUSAR",
                 "CAVIAR", "CACOAR", "CEIFAR", "CENSOR", "CERCAR", "CERNIR", "CERRAR", "CESSAR", "CHAGAR", "CHAMAR",
                 "CHECAR", "CHEGAR", "CHOCAR", "CHOFER", "CHORAR", "CHOVER", "CHUPAR", "CHUTAR", "CIFRAR", "CILIAR",
                 "CINDIR", "CINGIR", "CISCAR", "CISMAR", "CLAMAR", "CLAMOR", "CLICAR", "COAGIR", "COATOR", "COAXAR",
                 "COBRAR", "COBRIR", "COIBIR", "COLHER", "COMPOR", "CONDOR", "CONTAR", "CONTER", "CONVIR", "COPIAR",
                 "COROAR", "CORRER", "CORTAR", "COUBER", "CRAVAR", "CREDOR", "CREMAR", "CRIVAR", "CROMAR", "CRUZAR",
                 "CUIDAR", "CULPAR", "CULTOR", "CUNHAR", "CURSAR", "CURSOR", "CURTIR", "CURVAR", "CUSPIR", "CUSTAR",
                 "CANCER", "DANCAR", "DECAIR", "DEITAR", "DEIXAR", "DESCER", "DESPIR", "DIGNAR", "DILUIR", "DISCAR",
                 "DISPOR", "DISSER", "DISTAR", "DOADOR", "DOBRAR", "DORMIR", "DOURAR", "DOUTOR", "DRAGAR", "DRENAR",
                 "DROGAR", "DUBLAR", "DUELAR", "DISPAR", "EDITAR", "EDITOR", "EDUCAR", "EJETAR", "ELEGER", "ELEVAR",
                 "ELIXIR", "EMANAR", "EMITIR", "EMULAR", "ENCHER", "ENFIAR", "ENJOAR", "ENOJAR", "ENTOAR", "ENTRAR",
                 "ENVIAR", "EREGIR", "ERGUER", "ERIGIR", "ERICAR", "ERODIR", "ESCOAR", "ESPIAR", "ESVAIR", "EVADIR",
                 "EVITAR", "EVOCAR", "EXALAR", "EXARAR", "EXIBIR", "EXIGIR", "EXILAR", "EXIMIR", "EXPIAR", "EXUMAR",
                 "FALHAR", "FALTAR", "FAQUIR", "FARTAR", "FATIAR", "FECHAR", "FENDER", "FERRAR", "FERVER", "FERVOR",
                 "FICHAR", "FILIAR", "FILMAR", "FINCAR", "FINDAR", "FINGIR", "FINTAR", "FIRMAR", "FISGAR", "FLORIR",
                 "FOLGAR", "FORJAR", "FORMAR", "FORRAR", "FORCAR", "FRAGOR", "FREMIR", "FRESAR", "FRETAR", "FRIGIR",
                 "FRISAR", "FRITAR", "FULGIR", "FULGOR", "FUNDAR", "FUNDIR", "FUNGAR", "FURTAR", "GALGAR", "GANHAR",
                 "GARFAR", "GAROAR", "GASTAR", "GINGAR", "GLOSAR", "GOLEAR", "GOSTAR", "GRAFAR", "GRAVAR", "GRIFAR",
                 "GRILAR", "GRITAR", "GRUDAR", "HAURIR", "HERDAR", "HONRAR", "HORROR", "HOUVER", "ILUDIR", "IMITAR",
                 "IMOLAR", "INALAR", "INCHAR", "INCOAR", "INFLAR", "INIBIR", "INOVAR", "INSTAR", "INTUIR", "ISOLAR",
                 "ITERAR", "JAGUAR", "JANTAR", "JEJUAR", "JORRAR", "JUDIAR", "JULGAR", "JUNTAR", "LACRAR", "LADRAR",
                 "LAMBER", "LANCAR", "LARGAR", "LASCAR", "LAVRAR", "LEITOR", "LIMIAR", "LIMPAR", "LINEAR", "LISTAR",
                 "LIVRAR", "LOGRAR", "LOTEAR", "LOUVAR", "LOUVOR", "LUCRAR", "MAGOAR", "MALHAR", "MANCAR", "MANDAR",
                 "MANEAR", "MANJAR", "MANTER", "MAPEAR", "MARCAR", "MASCAR", "MEDIAR", "MEDRAR", "MELHOR", "MENEAR",
                 "MENTIR", "MIGRAR", "MILHAR", "MISTER", "MOEDOR", "MOLDAR", "MOLHAR", "MONTAR", "MORDER", "MORRER",
                 "MOSCAR", "MULHER", "MULTAR", "MARTIR", "NARRAR", "NASCER", "NESTOR", "NOIVAR", "NOMEAR", "NUTRIR",
                 "OBSTAR", "OBVIAR", "OCULAR", "OCUPAR", "OMITIR", "ONDEAR", "ONERAR", "OPERAR", "OPINAR", "OPUSER",
                 "ORADOR", "OXIDAR", "PAIRAR", "PAJEAR", "PAREAR", "PARTIR", "PASMAR", "PASSAR", "PASTAR", "PASTOR",
                 "PAUTAR", "PEIDAR", "PEITAR", "PENDER", "PENDOR", "PENHOR", "PENSAR", "PERDER", "PESCAR", "PICHAR",
                 "PILHAR", "PINGAR", "PINTAR", "PINTOR", "PINCAR", "PIORAR", "PISCAR", "PLACAR", "PLANAR", "PLOTAR",
                 "PLUGAR", "PORTAR", "POSPOR", "POSTAR", "POUPAR", "POUSAR", "POVOAR", "PRAZER", "PREGAR", "PREMIR",
                 "PREPOR", "PREVER", "PREVIR", "PREZAR", "PRIMAR", "PRIMOR", "PRIVAR", "PROPOR", "PROVAR", "PROVER",
                 "PROVIR", "PULSAR", "PURGAR", "POQUER", "QUASAR", "QUEDAR", "QUERER", "QUISER", "QUITAR", "RACHAR",
                 "RADIAR", "RALHAR", "RANCOR", "RANGER", "RAPTAR", "RAREAR", "RASGAR", "RASPAR", "RATEAR", "REAGIR",
                 "REATAR", "REATOR", "REAVER", "REBOAR", "RECAIR", "RECEAR", "RECUAR", "REGRAR", "REINAR", "REITOR",
                 "REMOER", "RENDER", "REQUER", "RESTAR", "REUNIR", "RISCAR", "RODEAR", "ROEDOR", "ROMPER", "RONCAR",
                 "RONDAR", "ROSNAR", "ROTEAR", "ROUBAR", "SACIAR", "SAGRAR", "SALDAR", "SALGAR", "SALTAR", "SALVAR",
                 "SAMBAR", "SANEAR", "SAUDAR", "SEDIAR", "SEGUIR", "SEMEAR", "SENHOR", "SENTAR", "SENTIR", "SEQUER",
                 "SERIAR", "SERRAR", "SERVIR", "SERZIR", "SILHAR", "SILVAR", "SISMAR", "SITIAR", "SITUAR", "SOBRAR",
                 "SOFRER", "SOLDAR", "SOLTAR", "SONDAR", "SONHAR", "SOPRAR", "SORRIR", "SORTIR", "SORVER", "SOUBER",
                 "SULCAR", "SUPRIR", "SURGIR", "SURRAR", "SURTIR", "SUSTAR", "SUSTER", "SUETER", "TACHAR", "TALHAR",
                 "TALHER", "TAMBOR", "TAMPAR", "TANGER", "TAPEAR", "TARDAR", "TATEAR", "TATUAR", "TECLAR", "TEIMAR",
                 "TENDER", "TENSOR", "TENTAR", "TERROR", "TESTAR", "TINGIR", "TOLHER", "TOMBAR", "TORCER", "TORNAR",
                 "TORRAR", "TOSSIR", "TOSTAR", "TRAGAR", "TRAJAR", "TRATAR", "TRATOR", "TRAVAR", "TRAZER", "TRACAR",
                 "TREMER", "TREMOR", "TREPAR", "TROCAR", "TROTAR", "TROCAR", "TURBAR", "TURVAR", "UFANAR", "ULULAR",
                 "URETER", "URINAR", "VADEAR", "VADIAR", "VARIAR", "VARRER", "VENCER", "VENDAR", "VENDER", "VENTAR",
                 "VERSAR", "VERTER", "VESTIR", "VIAJAR", "VIBRAR", "VICIAR", "VIDRAR", "VIGIAR", "VINCAR", "VINGAR",
                 "VIOLAR", "VIUVAR", "VOADOR", "VOLTAR", "VOLVER", "VULGAR", "WALTER", "XAVIER", "XINGAR", "ZANGAR",
                 "ZANZAR", "ZARPAR", "ZOMBAR", "ZUMBIR", "ZURRAR"]
