#!/bin/bash

# adapted from:
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=decklink-sdk

UA="User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Safari/537.36"
VER=16.0
VER_ID=47789a55dd7f4e848ec5352a4903d4e8
REF_ID=d60730b1035946f388928c256a4a03f9
REF_URL=https://www.blackmagicdesign.com/support/download/${REF_ID}/Linux
DL_URL=https://www.blackmagicdesign.com/api/register/us/download/${VER_ID}
SRC_URL=$(curl \
     -L \
     -s \
     -H "${UA}" \
     -H 'Content-Type: application/json;charset=UTF-8' \
     -H "Referer: ${REF_URL}" \
     --data-ascii "{ \
     \"platform\": \"Linux\", \
     \"country\": \"us\", \
     \"firstname\": \"Fedora\", \
     \"lastname\": \"Linux\", \
     \"email\": \"decklink-maintainers@fedoraproject.org\", \
     \"phone\": \"1-888-RED-HAT1\", \
     \"state\": \"North Carolina\", \
     \"city\": \"Raleigh\", \
     \"street\": \"100 E. Davie Street\", \
     \"policy\": true, \
     \"hasAgreedToTerms\": true, \
     \"product\": \"Desktop Video ${VER} SDK\" \
     }" --compressed "${DL_URL}")

curl \
     -H "${UA}" \
     -O \
     --compressed \
     "${SRC_URL}"

ZIP_FILE=$(echo ${SRC_URL} | cut -d'?' -f1 | cut -d/ -f6)

unzip -qq ${ZIP_FILE}
mv "Blackmagic DeckLink SDK ${VER}" decklink-${VER}

# include only Boost licensed files
tar czf decklink-${VER}.tar.gz decklink-${VER}/Linux/include
rm -r decklink-${VER}
