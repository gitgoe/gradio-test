from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "data": [
            {
                "type": "urn:api:edi:batch",
                "id": "7954af59-b154-4280-b241-f87e8736e0bd",
                "attributes": {
                    "creationDateTime": "2026-01-05T14:00:20.620Z",
                    "timeStamp": "2026-01-05-15.00.20.392654",
                    "action": "IMPRESSION-1234",
                    "streamWeaverScriptName": "NA",
                    "applicationGroupOD": "CheckGED",
                    "packageName": "afpscheckod.pub",
                    "indexKey": "NA",
                    "refDocList": "NA",
                    "serviceName": "lu.lefoyer.services.BatchStarterApp",
                    "fileName": "INTP_LEXVC100_CHECKGED.dat",
                    "runShellSript": "std_dia_ged.sh",
                    "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
                    "nbrOfCopies": "1",
                    "recipients": "NA",
                    "docType": "NA",
                    "dialogueEngine": "/data/soft/Engine",
                    "applicationOD": "CheckGED",
                    "status": -1
                }
            },
            {
                "type": "urn:api:edi:batch",
                "id": "b25a0a7c-bffe-48f7-b63a-7e8719863cc5",
                "attributes": {
                    "creationDateTime": "2026-01-05T17:05:36.412Z",
                    "timeStamp": "2026-01-05-18.05.35.072663",
                    "action": "IMPRESSION",
                    "streamWeaverScriptName": "std_codebarre.con",
                    "applicationGroupOD": "NOARCHIVE",
                    "packageName": "afpdgdprconsmark.pub",
                    "indexKey": "NA",
                    "refDocList": "NA",
                    "serviceName": "lu.lefoyer.services.BatchStarterApp",
                    "fileName": "INTP_LSIMJ140_IEBGENE1_GDPR_COMMUNIQ.dat",
                    "runShellSript": "std_dia_ged_sw.sh",
                    "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
                    "nbrOfCopies": "1",
                    "recipients": "NA",
                    "docType": "NA",
                    "dialogueEngine": "/data/soft/Engine",
                    "applicationOD": "NA",
                    "status": -1
                }
            },
            {
                "type": "urn:api:edi:batch",
                "id": "b3f7a83f-b031-4a1d-b4b3-8f9c524918cf",
                "attributes": {
                    "creationDateTime": "2026-01-05T17:05:39.209Z",
                    "timeStamp": "2026-01-05-18.05.38.903051",
                    "action": "IMPRESSION",
                    "streamWeaverScriptName": "std_codebarre.con",
                    "applicationGroupOD": "NA",
                    "packageName": "afpdsammypdfreco.pub",
                    "indexKey": "NA",
                    "refDocList": "NA",
                    "serviceName": "lu.lefoyer.services.BatchStarterApp",
                    "fileName": "INTP_LSMMJ100_IEBGENE1_SAMMY_COMMUNIQ.dat",
                    "runShellSript": "std_dia_ged_sw.sh",
                    "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
                    "nbrOfCopies": "1",
                    "recipients": "NA",
                    "docType": "NA",
                    "dialogueEngine": "/data/soft/Engine",
                    "applicationOD": "NOARCHIVE",
                    "status": -1
                }
            },
            {
                "type": "urn:api:edi:batch",
                "id": "b845df79-db53-4b8c-a923-1c990345afb5",
                "attributes": {
                    "creationDateTime": "2026-01-05T17:05:48.462Z",
                    "timeStamp": "2026-01-05-18.05.48.178243",
                    "action": "IMPRESSION",
                    "streamWeaverScriptName": "std_codebarre.con",
                    "applicationGroupOD": "NOARCHIVE",
                    "packageName": "afpdsepamandats.pub",
                    "indexKey": "NA",
                    "refDocList": "NA",
                    "serviceName": "lu.lefoyer.services.BatchStarterApp",
                    "fileName": "#LLNVRELE1010#INTP_LECLI108_EC00P70B_MANDATS_IARD.dat",
                    "runShellSript": "std_dia_ged_sw.sh",
                    "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
                    "nbrOfCopies": "1",
                    "recipients": "NA",
                    "docType": "NA",
                    "dialogueEngine": "/data/soft/Engine",
                    "applicationOD": "NA",
                    "status": -1
                }
            },
            {
                "type": "urn:api:edi:batch",
                "id": "dce114ed-ec81-4627-b20c-35016f14eb6e",
                "attributes": {
                    "creationDateTime": "2026-01-05T17:05:50.736Z",
                    "timeStamp": "2026-01-05-18.05.50.551021",
                    "action": "IMPRESSION",
                    "streamWeaverScriptName": "std_codebarre.con",
                    "applicationGroupOD": "NOARCHIVE",
                    "packageName": "afpdsepamandats.pub",
                    "indexKey": "NA",
                    "refDocList": "NA",
                    "serviceName": "lu.lefoyer.services.BatchStarterApp",
                    "fileName": "#LLNVRELE1011#INTP_LECLI108_EC00P70B_MANDATS_SANTE.dat",
                    "runShellSript": "std_dia_ged_sw.sh",
                    "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
                    "nbrOfCopies": "1",
                    "recipients": "NA",
                    "docType": "NA",
                    "dialogueEngine": "/data/soft/Engine",
                    "applicationOD": "NA",
                    "status": -1
                }
            },
            {
                "type": "urn:api:edi:batch",
                "id": "d9e8dddf-147c-430c-931a-013a4f051629",
                "attributes": {
                    "creationDateTime": "2026-01-05T17:07:33.748Z",
                    "timeStamp": "2026-01-05-18.07.32.153814",
                    "action": "IMPRESSION",
                    "streamWeaverScriptName": "NA",
                    "applicationGroupOD": "SINCRExpertise",
                    "packageName": "afpssincrexpert.pub",
                    "indexKey": "NA",
                    "refDocList": "NA",
                    "serviceName": "lu.lefoyer.services.BatchStarterApp",
                    "fileName": "INTP_LSILI130_SIN24960_FICSINEX.dat",
                    "runShellSript": "std_dia_ged_sw.sh",
                    "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
                    "nbrOfCopies": "1",
                    "recipients": "SINCRExpertise",
                    "docType": "NA",
                    "dialogueEngine": "/data/soft/Engine",
                    "applicationOD": "SINCRExpertise",
                    "status": -1
                }
            },
            {
                "type": "urn:api:edi:batch",
                "id": "e1141727-11b4-485e-8a72-5ea0a2f61a95",
                "attributes": {
                    "creationDateTime": "2026-01-05T17:07:37.649Z",
                    "timeStamp": "2026-01-05-18.07.37.408760",
                    "action": "IMPRESSION",
                    "streamWeaverScriptName": "NA",
                    "applicationGroupOD": "SINCRExpertise",
                    "packageName": "afpssincrexpert.pub",
                    "indexKey": "NA",
                    "refDocList": "NA",
                    "serviceName": "lu.lefoyer.services.BatchStarterApp",
                    "fileName": "INTP_LSILI131_SIN24970_FICSINEX.dat",
                    "runShellSript": "std_dia_ged_sw.sh",
                    "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
                    "nbrOfCopies": "1",
                    "recipients": "SINCRExpertise",
                    "docType": "NA",
                    "dialogueEngine": "/data/soft/Engine",
                    "applicationOD": "SINCRExpertise",
                    "status": -1
                }
            },
            {
                "type": "urn:api:edi:batch",
                "id": "10b8eebe-a6f1-4b15-a9e3-113f330e000b",
                "attributes": {
                    "creationDateTime": "2026-01-05T17:07:49.666Z",
                    "timeStamp": "2026-01-05-18.07.49.452974",
                    "action": "IMPRESSION",
                    "streamWeaverScriptName": "NA",
                    "applicationGroupOD": "FardesSin",
                    "packageName": "afpssinfardes.pub",
                    "indexKey": "NA",
                    "refDocList": "NA",
                    "serviceName": "lu.lefoyer.services.BatchStarterApp",
                    "fileName": "INTP_LSIMJ122_SORT01.dat",
                    "runShellSript": "std_dia_ged.sh",
                    "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
                    "nbrOfCopies": "1",
                    "recipients": "NA",
                    "docType": "NA",
                    "dialogueEngine": "/data/soft/Engine",
                    "applicationOD": "FardesSin",
                    "status": -1
                }
            },
            {
                "type": "urn:api:edi:batch",
                "id": "7de4071d-af8c-4751-ae3d-06d6c6f32fe3",
                "attributes": {
                    "creationDateTime": "2026-01-05T17:08:03.458Z",
                    "timeStamp": "2026-01-05-18.08.03.207956",
                    "action": "IMPRESSION",
                    "streamWeaverScriptName": "NA",
                    "applicationGroupOD": "NOARCHIVE",
                    "packageName": "afpdsinavisano.pub",
                    "indexKey": "NA",
                    "refDocList": "NA",
                    "serviceName": "lu.lefoyer.services.BatchStarterApp",
                    "fileName": "INTP_LSIEX103_SIN88960_LSIDATAO.dat",
                    "runShellSript": "std_dia_ged_sw.sh",
                    "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
                    "nbrOfCopies": "1",
                    "recipients": "sinistresANO",
                    "docType": "NA",
                    "dialogueEngine": "/data/soft/Engine",
                    "applicationOD": "NA",
                    "status": -1
                }
            },
            {
                "type": "urn:api:edi:batch",
                "id": "755d9d53-bbd2-4cc1-98c6-0cbf2fb4096a",
                "attributes": {
                    "creationDateTime": "2026-01-05T17:08:43.568Z",
                    "timeStamp": "2026-01-05-18.08.43.307413",
                    "action": "IMPRESSION",
                    "streamWeaverScriptName": "NA",
                    "applicationGroupOD": "RDRAccordRegl",
                    "packageName": "afpssinreglrdr.pub",
                    "indexKey": "NA",
                    "refDocList": "NA",
                    "serviceName": "lu.lefoyer.services.BatchStarterApp",
                    "fileName": "INTP_LSILI105_SIN88060_LSIACRDR.dat",
                    "runShellSript": "std_dia_ged.sh",
                    "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
                    "nbrOfCopies": "1",
                    "recipients": "NA",
                    "docType": "NA",
                    "dialogueEngine": "/data/soft/Engine",
                    "applicationOD": "RDRAccordRegl",
                    "status": -1
                }
            }
        ],
        "links": {
            "self": "http://localhost:9000/batch",
            "first": "http://localhost:9000/batch?page[number]=0&page[size]=10",
            "prev": "http://localhost:9000/batch?page[number]=0&page[size]=10",
            "next": "http://localhost:9000/batch?page[number]=1&page[size]=10",
            "last": "http://localhost:9000/batch?page[number]=53&page[size]=10"
        },
        "meta": {
            "totalPages": 54,
            "totalRecords": 536,
            "page": {
                "number": 0,
                "size": 10
            }
        }
    }


@app.get("/batch/{name}")
async def say_hello(name: str):
    return {
  "data": [
    {
      "type": "urn:api:edi:batch",
      "id": "7954af59-b154-4280-b241-f87e8736e0bd",
      "attributes": {
        "creationDateTime": "2026-01-05T14:00:20.620Z",
        "timeStamp": "2026-01-05-15.00.20.392654",
        "action": "IMPRESSION",
        "streamWeaverScriptName": "NA",
        "applicationGroupOD": "CheckGED",
        "packageName": "afpscheckod.pub",
        "indexKey": "NA",
        "refDocList": "NA",
        "serviceName": "lu.lefoyer.services.BatchStarterApp",
        "fileName": "INTP_LEXVC100_CHECKGED.dat",
        "runShellSript": "std_dia_ged.sh",
        "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
        "nbrOfCopies": "1",
        "recipients": "NA",
        "docType": "NA",
        "dialogueEngine": "/data/soft/Engine",
        "applicationOD": "CheckGED",
        "status": -1
      }
    },
    {
      "type": "urn:api:edi:batch",
      "id": "b25a0a7c-bffe-48f7-b63a-7e8719863cc5",
      "attributes": {
        "creationDateTime": "2026-01-05T17:05:36.412Z",
        "timeStamp": "2026-01-05-18.05.35.072663",
        "action": "IMPRESSION",
        "streamWeaverScriptName": "std_codebarre.con",
        "applicationGroupOD": "NOARCHIVE",
        "packageName": "afpdgdprconsmark.pub",
        "indexKey": "NA",
        "refDocList": "NA",
        "serviceName": "lu.lefoyer.services.BatchStarterApp",
        "fileName": "INTP_LSIMJ140_IEBGENE1_GDPR_COMMUNIQ.dat",
        "runShellSript": "std_dia_ged_sw.sh",
        "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
        "nbrOfCopies": "1",
        "recipients": "NA",
        "docType": "NA",
        "dialogueEngine": "/data/soft/Engine",
        "applicationOD": "NA",
        "status": -1
      }
    },
    {
      "type": "urn:api:edi:batch",
      "id": "b3f7a83f-b031-4a1d-b4b3-8f9c524918cf",
      "attributes": {
        "creationDateTime": "2026-01-05T17:05:39.209Z",
        "timeStamp": "2026-01-05-18.05.38.903051",
        "action": "IMPRESSION",
        "streamWeaverScriptName": "std_codebarre.con",
        "applicationGroupOD": "NA",
        "packageName": "afpdsammypdfreco.pub",
        "indexKey": "NA",
        "refDocList": "NA",
        "serviceName": "lu.lefoyer.services.BatchStarterApp",
        "fileName": "INTP_LSMMJ100_IEBGENE1_SAMMY_COMMUNIQ.dat",
        "runShellSript": "std_dia_ged_sw.sh",
        "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
        "nbrOfCopies": "1",
        "recipients": "NA",
        "docType": "NA",
        "dialogueEngine": "/data/soft/Engine",
        "applicationOD": "NOARCHIVE",
        "status": -1
      }
    },
    {
      "type": "urn:api:edi:batch",
      "id": "b845df79-db53-4b8c-a923-1c990345afb5",
      "attributes": {
        "creationDateTime": "2026-01-05T17:05:48.462Z",
        "timeStamp": "2026-01-05-18.05.48.178243",
        "action": "IMPRESSION",
        "streamWeaverScriptName": "std_codebarre.con",
        "applicationGroupOD": "NOARCHIVE",
        "packageName": "afpdsepamandats.pub",
        "indexKey": "NA",
        "refDocList": "NA",
        "serviceName": "lu.lefoyer.services.BatchStarterApp",
        "fileName": "#LLNVRELE1010#INTP_LECLI108_EC00P70B_MANDATS_IARD.dat",
        "runShellSript": "std_dia_ged_sw.sh",
        "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
        "nbrOfCopies": "1",
        "recipients": "NA",
        "docType": "NA",
        "dialogueEngine": "/data/soft/Engine",
        "applicationOD": "NA",
        "status": -1
      }
    },
    {
      "type": "urn:api:edi:batch",
      "id": "dce114ed-ec81-4627-b20c-35016f14eb6e",
      "attributes": {
        "creationDateTime": "2026-01-05T17:05:50.736Z",
        "timeStamp": "2026-01-05-18.05.50.551021",
        "action": "IMPRESSION",
        "streamWeaverScriptName": "std_codebarre.con",
        "applicationGroupOD": "NOARCHIVE",
        "packageName": "afpdsepamandats.pub",
        "indexKey": "NA",
        "refDocList": "NA",
        "serviceName": "lu.lefoyer.services.BatchStarterApp",
        "fileName": "#LLNVRELE1011#INTP_LECLI108_EC00P70B_MANDATS_SANTE.dat",
        "runShellSript": "std_dia_ged_sw.sh",
        "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
        "nbrOfCopies": "1",
        "recipients": "NA",
        "docType": "NA",
        "dialogueEngine": "/data/soft/Engine",
        "applicationOD": "NA",
        "status": -1
      }
    },
    {
      "type": "urn:api:edi:batch",
      "id": "d9e8dddf-147c-430c-931a-013a4f051629",
      "attributes": {
        "creationDateTime": "2026-01-05T17:07:33.748Z",
        "timeStamp": "2026-01-05-18.07.32.153814",
        "action": "IMPRESSION",
        "streamWeaverScriptName": "NA",
        "applicationGroupOD": "SINCRExpertise",
        "packageName": "afpssincrexpert.pub",
        "indexKey": "NA",
        "refDocList": "NA",
        "serviceName": "lu.lefoyer.services.BatchStarterApp",
        "fileName": "INTP_LSILI130_SIN24960_FICSINEX.dat",
        "runShellSript": "std_dia_ged_sw.sh",
        "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
        "nbrOfCopies": "1",
        "recipients": "SINCRExpertise",
        "docType": "NA",
        "dialogueEngine": "/data/soft/Engine",
        "applicationOD": "SINCRExpertise",
        "status": -1
      }
    },
    {
      "type": "urn:api:edi:batch",
      "id": "e1141727-11b4-485e-8a72-5ea0a2f61a95",
      "attributes": {
        "creationDateTime": "2026-01-05T17:07:37.649Z",
        "timeStamp": "2026-01-05-18.07.37.408760",
        "action": "IMPRESSION",
        "streamWeaverScriptName": "NA",
        "applicationGroupOD": "SINCRExpertise",
        "packageName": "afpssincrexpert.pub",
        "indexKey": "NA",
        "refDocList": "NA",
        "serviceName": "lu.lefoyer.services.BatchStarterApp",
        "fileName": "INTP_LSILI131_SIN24970_FICSINEX.dat",
        "runShellSript": "std_dia_ged_sw.sh",
        "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
        "nbrOfCopies": "1",
        "recipients": "SINCRExpertise",
        "docType": "NA",
        "dialogueEngine": "/data/soft/Engine",
        "applicationOD": "SINCRExpertise",
        "status": -1
      }
    },
    {
      "type": "urn:api:edi:batch",
      "id": "10b8eebe-a6f1-4b15-a9e3-113f330e000b",
      "attributes": {
        "creationDateTime": "2026-01-05T17:07:49.666Z",
        "timeStamp": "2026-01-05-18.07.49.452974",
        "action": "IMPRESSION",
        "streamWeaverScriptName": "NA",
        "applicationGroupOD": "FardesSin",
        "packageName": "afpssinfardes.pub",
        "indexKey": "NA",
        "refDocList": "NA",
        "serviceName": "lu.lefoyer.services.BatchStarterApp",
        "fileName": "INTP_LSIMJ122_SORT01.dat",
        "runShellSript": "std_dia_ged.sh",
        "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
        "nbrOfCopies": "1",
        "recipients": "NA",
        "docType": "NA",
        "dialogueEngine": "/data/soft/Engine",
        "applicationOD": "FardesSin",
        "status": -1
      }
    },
    {
      "type": "urn:api:edi:batch",
      "id": "7de4071d-af8c-4751-ae3d-06d6c6f32fe3",
      "attributes": {
        "creationDateTime": "2026-01-05T17:08:03.458Z",
        "timeStamp": "2026-01-05-18.08.03.207956",
        "action": "IMPRESSION",
        "streamWeaverScriptName": "NA",
        "applicationGroupOD": "NOARCHIVE",
        "packageName": "afpdsinavisano.pub",
        "indexKey": "NA",
        "refDocList": "NA",
        "serviceName": "lu.lefoyer.services.BatchStarterApp",
        "fileName": "INTP_LSIEX103_SIN88960_LSIDATAO.dat",
        "runShellSript": "std_dia_ged_sw.sh",
        "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
        "nbrOfCopies": "1",
        "recipients": "sinistresANO",
        "docType": "NA",
        "dialogueEngine": "/data/soft/Engine",
        "applicationOD": "NA",
        "status": -1
      }
    },
    {
      "type": "urn:api:edi:batch",
      "id": "755d9d53-bbd2-4cc1-98c6-0cbf2fb4096a",
      "attributes": {
        "creationDateTime": "2026-01-05T17:08:43.568Z",
        "timeStamp": "2026-01-05-18.08.43.307413",
        "action": "IMPRESSION",
        "streamWeaverScriptName": "NA",
        "applicationGroupOD": "RDRAccordRegl",
        "packageName": "afpssinreglrdr.pub",
        "indexKey": "NA",
        "refDocList": "NA",
        "serviceName": "lu.lefoyer.services.BatchStarterApp",
        "fileName": "INTP_LSILI105_SIN88060_LSIACRDR.dat",
        "runShellSript": "std_dia_ged.sh",
        "streamWeaverEngine": "/usr/lib/StreamWeaver-6.6.2/bin64",
        "nbrOfCopies": "1",
        "recipients": "NA",
        "docType": "NA",
        "dialogueEngine": "/data/soft/Engine",
        "applicationOD": "RDRAccordRegl",
        "status": -1
      }
    }
  ],
  "links": {
    "self": "http://localhost:9000/batch",
    "first": "http://localhost:9000/batch?page[number]=0&page[size]=10",
    "prev": "http://localhost:9000/batch?page[number]=0&page[size]=10",
    "next": "http://localhost:9000/batch?page[number]=1&page[size]=10",
    "last": "http://localhost:9000/batch?page[number]=53&page[size]=10"
  },
  "meta": {
    "totalPages": 54,
    "totalRecords": 536,
    "page": {
      "number": 0,
      "size": 10
    }
  }
}
