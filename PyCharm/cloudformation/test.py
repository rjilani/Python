import json



model = json.loads('''{
  "assetClasses": [
    {
      "secondAssetClasses": [
        {
          "thirdAssetClasses": [
            {
              "name": "Large Cap Growth",
              "weight": 5
            },
            {
              "name": "Large Cap Value",
              "weight": 5
            }
          ],
          "name": "US Large Cap",
          "weight": 10
        },
        {
          "thirdAssetClasses": [
            {
              "name": "Mid Cap Growth",
              "weight": 8
            },
            {
              "name": "Mid Cap Value",
              "weight": 4
            }
          ],
          "name": "US Mid Cap",
          "weight": 12
        },
        {
          "thirdAssetClasses": [
            {
              "name": "Small Cap Stock",
              "weight": 13
            }
          ],
          "name": "US Small Cap",
          "weight": 13
        }
      ],
      "name": "US Equity",
      "weight": 35
    },
    {
      "secondAssetClasses": [
        {
          "thirdAssetClasses": [
            {
              "name": "International Core",
              "weight": 10
            }
          ],
          "name": "Non US Developed",
          "weight": 10
        },
        {
          "thirdAssetClasses": [
            {
              "name": "Emerging Market",
              "weight": 15
            }
          ],
          "name": "Non US Emerging",
          "weight": 15
        }
      ],
      "name": "Non-US Equity",
      "weight": 25
    },
    {
      "secondAssetClasses": [
        {
          "thirdAssetClasses": [
            {
              "name": "Real Assets Equity",
              "weight": 15
            }
          ],
          "name": "Real Assets Equity",
          "weight": 15
        }
      ],
      "name": "Real Assets Equity",
      "weight": 10
    },
    {
      "secondAssetClasses": [
        {
          "thirdAssetClasses": [
            {
              "name": "Investment Grade",
              "weight": 5
            }
          ],
          "name": "Fixed Income Core",
          "weight": 5
        },
        {
          "thirdAssetClasses": [
            {
              "name": "International Bond",
              "weight": 5
            },
            {
              "name": "High Yield",
              "weight": 7
            },
            {
              "name": "Emerging Market Bond",
              "weight": 6
            }
          ],
          "name": "Fixed Income Plus",
          "weight": 18
        },
        {
          "thirdAssetClasses": [
            {
              "name": "Conservative Fixed Income",
              "weight": 2
            }
          ],
          "name": "Conservative Fixed Income",
          "weight": 2
        }
      ],
      "name": "Fixed Income",
      "weight": 25
    }
  ]
}''')

for key, value in model.items():
    print (key, value)
