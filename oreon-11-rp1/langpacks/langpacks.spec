%global source0_hash none
Name:      langpacks
Version:   4.3
Release:        1%{?dist}
Summary:        Langpacks meta-package
License:   GPL-2.0-or-later
BuildArch: noarch
# oreon:deps
BuildRequires:  fontconfig
BuildRequires:  libappstream-glib
BuildRequires:  python3
# /oreon:deps
%description
Langpack meta-package to provide individual langpacks packages.

# The following language list is generated based on
# 1) take the languages where anaconda translations are available
# ls /usr/share/locale/*/LC_MESSAGES/anaconda.mo
# Then pick those languages which provides at least a single langpack
# Now, Added exception for dz and ku languages which have no anaconda.mo
# 2) Added br ga he nn nr ss tn ts ve xh
# as per requested in https://bugzilla.redhat.com/show_bug.cgi?id=1310538
# 3) Enabled en langpack https://bugzilla.redhat.com/show_bug.cgi?id=1312890
# 4) Enabled eo langpack https://bugzilla.redhat.com/show_bug.cgi?id=1644736
# 5) Enabled bo, dz, ka, km, ku, my, yi
# 6) Enabled zh_HK to set its own input method
# 7) Enabled chr, dv, hy, iu, lo so that its default font be installed at least

# package list
#
# Writing this in LUA to make it more visible and easy to maintain.
#
# lang: language identifier
# fclang: language identifier in fontconfig. lang will be used if not present
# default: default font sets
#  face: default typeface for default-fonts-<language code>.
#  sans: default sans-serif font package
#  serif: default serif font package
#  mono: default monospace font package
# recommends: recommended font packages to be installed
#             only activated for Fedora
# inputmethod: input method to be pulled by core meta package
# meta: dependencies foe langpacks meta package
#  requires: required packages by meta package
#  recommends: recommended packages by meta package
#
# Adding fedora_ prefix to inputmethod and meta.requires/meta.recommends will be available for Fedora only.
#
# See defcorepkg, deffontpkg, and defmetapkg for package template

# Note: Adding new ll_cc code (not ll) may needs extra work in gnome-software
#       to pick them up properly.
#       See https://gitlab.gnome.org/GNOME/gnome-software/-/blob/main/plugins/fedora-langpacks/gs-plugin-fedora-langpacks.c?ref_type=heads#L48
#

%{lua:
local core_font_package_list
if tonumber(rpm.expand("0%{?rhel}")) ~= 0 and tonumber(rpm.expand("0%{?rhel}")) > 9 then
core_font_package_list = {
  default={
    sans={ "redhat-text-vf-fonts", "google-noto-sans-vf-fonts" },
    serif={ "google-noto-serif-vf-fonts" },
    mono={ "redhat-mono-vf-fonts", "google-noto-sans-mono-vf-fonts" },
    emoji={ "google-noto-emoji-color-fonts" },
    math={ "google-noto-sans-math-fonts", "stix-fonts", "google-noto-sans-symbols-vf-fonts", "google-noto-sans-symbols-2-fonts" }
  },
  cjk={
    sans={ "google-noto-sans-cjk-vf-fonts" },
    serif={ "google-noto-serif-cjk-vf-fonts" },
    mono={ "google-noto-sans-mono-cjk-vf-fonts" },
  },
}
else
core_font_package_list = {
  default={
    sans={ "abattis-cantarell-vf-fonts", "google-noto-sans-vf-fonts" },
    serif={ "google-noto-serif-vf-fonts" },
    mono={ "google-noto-sans-mono-vf-fonts" },
    emoji={ "google-noto-emoji-color-fonts" },
    math={ "google-noto-sans-math-fonts", "stix-fonts", "google-noto-sans-symbols-vf-fonts", "google-noto-sans-symbols-2-fonts" }
  },
  cjk={
    sans={ "google-noto-sans-cjk-vf-fonts" },
    serif={ "google-noto-serif-cjk-vf-fonts" },
    mono={ "google-noto-sans-mono-cjk-vf-fonts" },
  },
}
end
local langpacks_package_list = {
 { lang="af", fclang="", langname="Afrikaans", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="am", fclang="", langname="Amharic", default={
                sans="google-noto-sans-ethiopic-vf-fonts",
                serif="google-noto-serif-ethiopic-vf-fonts",
                mono="" },
   recommends={ "senamirmir-washra-fantuwua-fonts",
                "senamirmir-washra-fonts",
                "senamirmir-washra-hiwua-fonts",
                "senamirmir-washra-jiret-fonts",
                "senamirmir-washra-tint-fonts",
                "senamirmir-washra-wookianos-fonts",
                "senamirmir-washra-yebse-fonts",
                "senamirmir-washra-yigezu-bisrat-goffer-fonts",
                "senamirmir-washra-yigezu-bisrat-gothic-fonts",
                "senamirmir-washra-zelan-fonts",
                "xorg-x11-fonts-ethiopic",
                "sil-abyssinica-fonts"
                },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ar", fclang="", langname="Arabic", default={
                sans="google-noto-sans-arabic-vf-fonts",
                serif="google-noto-naskh-arabic-vf-fonts",
                mono="" },
   recommends={ "paktype-naqsh-fonts",
                "paktype-tehreer-fonts",
                "kacst-art-fonts",
                "kacst-book-fonts",
                "kacst-decorative-fonts",
                "kacst-digital-fonts",
                "kacst-farsi-fonts",
                "kacst-letter-fonts",
                "kacst-naskh-fonts",
                "kacst-office-fonts",
                "kacst-one-fonts",
                "kacst-pen-fonts",
                "kacst-poster-fonts",
                "kacst-qurn-fonts",
                "kacst-screen-fonts",
                "kacst-title-fonts",
                "kacst-titlel-fonts"
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="as", fclang="", langname="Assamese", default={
                sans="google-noto-sans-bengali-vf-fonts",
                serif="google-noto-serif-bengali-vf-fonts",
                mono="" },
   recommends={ "google-noto-sans-bengali-ui-vf-fonts",
                "lohit-assamese-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ast", fclang="", langname="Asturian", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="be", fclang="", langname="Belarusian", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="bg", fclang="", langname="Bulgarian", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="bn", fclang="", langname="Bengali", default={
                sans="google-noto-sans-bengali-vf-fonts",
                serif="google-noto-serif-bengali-vf-fonts",
                mono="" },
   recommends={ "google-noto-sans-bengali-ui-vf-fonts",
                "lohit-bengali-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="bo", fclang="", langname="Tibetan", default={
                sans="jomolhari-fonts",
                serif="",
                mono="" },
   recommends={ "tibetan-machine-uni-fonts"
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="br", fclang="", langname="Breton", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="bs", fclang="", langname="Bosnian", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ca", fclang="", langname="Catalan", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="chr", fclang="", langname="Cherokee", default={
                sans="google-noto-sans-cherokee-vf-fonts",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="cs", fclang="", langname="Czech", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="cy", fclang="", langname="Welsh", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="da", fclang="", langname="Danish", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="de", fclang="", langname="German", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="dv", fclang="", langname="Divehi", default={
                sans="google-noto-sans-thaana-vf-fonts",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="dz", fclang="", langname="Bhutanese", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="el", fclang="", langname="Greek", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="en", fclang="", langname="English", default={
                sans="", -- Do not add anything here. default-fonts-en is equivalent to default-fonts-core-sans
                serif="",
                mono="" },
   recommends={ "liberation-sans-fonts",
                "liberation-serif-fonts",
                "liberation-mono-fonts",
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="en_GB", fclang="en", langname="English (United Kingdom)", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="eo", fclang="", langname="Esperanto", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="es", fclang="", langname="Spanish", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="et", fclang="", langname="Estonian", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="eu", fclang="", langname="Basque", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="fa", fclang="", langname="Persian", default={
                sans="vazirmatn-vf-fonts",
                serif="google-noto-naskh-arabic-vf-fonts",
                mono="" },
   recommends={ "google-noto-naskh-arabic-vf-fonts"
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="fi", fclang="", langname="Finnish", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="fr", fclang="", langname="French", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ga", fclang="", langname="Irish", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="gl", fclang="", langname="Galician", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="got", fclang="", langname="Gothic", default={
                sans="google-noto-sans-gothic-fonts",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="gu", fclang="", langname="Gujarati", default={
                sans="google-noto-sans-gujarati-vf-fonts",
                serif="google-noto-serif-gujarati-vf-fonts",
                mono="" },
   recommends={ "google-noto-sans-gujarati-ui-fonts",
                "lohit-gujarati-fonts",
                "samyak-gujarati-fonts"
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="he", fclang="", langname="Hebrew", default={
                sans="google-noto-sans-hebrew-vf-fonts",
                serif="google-noto-serif-hebrew-vf-fonts",
                mono="" },
   recommends={ "culmus-aharoni-clm-fonts",
                "culmus-caladings-clm-fonts",
                "culmus-david-clm-fonts",
                "culmus-drugulin-clm-fonts",
                "culmus-ellinia-clm-fonts",
                "culmus-frank-ruehl-clm-fonts",
                "culmus-hadasim-clm-fonts",
                "culmus-keteryg-fonts",
                "culmus-miriam-clm-fonts",
                "culmus-miriam-mono-clm-fonts",
                "culmus-nachlieli-clm-fonts",
                "culmus-simple-clm-fonts",
                "culmus-stamashkenaz-clm-fonts",
                "culmus-stamsefarad-clm-fonts",
                "culmus-yehuda-clm-fonts",
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="hi", fclang="", langname="Hindi", default={
                sans="google-noto-sans-devanagari-vf-fonts",
                serif="google-noto-serif-devanagari-vf-fonts",
                mono="" },
   recommends={ "google-noto-sans-devanagari-ui-vf-fonts",
                "lohit-devanagari-fonts",
                "samyak-devanagari-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="hr", fclang="", langname="Croatian", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="hu", fclang="", langname="Hungarian", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="hy", fclang="", langname="Armenian", default={
                sans="google-noto-sans-armenian-vf-fonts",
                serif="google-noto-serif-armenian-vf-fonts",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ia", fclang="", langname="Interlingua", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="id", fclang="", langname="Indonesian", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ii", fclang="ii", langname="Sichuan Yi", default={
                sans="google-noto-sans-yi-fonts",
                serif="",
                mono="" },
   recommends={ "sil-nuosu-fonts"
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="is", fclang="", langname="Icelandic", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="it", fclang="", langname="Italian", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="iu", fclang="", langname="Inuktitut", default={
                sans="google-noto-sans-canadian-aboriginal-vf-fonts",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ja", fclang="", langname="Japanese", default={
                sans="", -- Use core_font_package_list if you want to have common fonts for CJK
                serif="",
                mono="" },
   recommends={},
   inputmethod="ibus-anthy",
   meta={ requires={},
          recommends={},
          fedora_recommends={ "(uim-anthy if uim)" }
   },
 },
 { lang="kab", fclang="", langname="Kabyle", default={
                 sans="",
                 serif="",
                 mono="" },
   recommends={ "google-noto-sans-tifinagh-fonts" },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ka", fclang="", langname="Georgian", default={
                sans="google-noto-sans-georgian-vf-fonts",
                serif="google-noto-serif-georgian-vf-fonts",
                mono="" },
   recommends={ "bpg-chveulebrivi-fonts",
                "bpg-courier-fonts",
                "bpg-glaho-fonts",
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="kk", fclang="", langname="Kazakh", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="km", fclang="", langname="Khmer", default={
                sans="google-noto-sans-khmer-vf-fonts",
                serif="google-noto-serif-khmer-vf-fonts",
                mono="" },
   recommends={ "khmer-os-system-fonts",
                "khmer-os-battambang-fonts",
                "khmer-os-bokor-fonts",
                "khmer-os-content-fonts",
                "khmer-os-fasthand-fonts",
                "khmer-os-freehand-fonts",
                "khmer-os-handwritten-fonts",
                "khmer-os-metal-chrieng-fonts",
                "khmer-os-muol-fonts-all",
                "khmer-os-siemreap-fonts",
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="kn", fclang="", langname="Kannada", default={
                sans="google-noto-sans-kannada-vf-fonts",
                serif="google-noto-serif-kannada-vf-fonts",
                mono="" },
   recommends={ "google-noto-sans-kannada-ui-vf-fonts",
                "gubbi-fonts",
                "lohit-kannada-fonts",
                "navilu-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ko", fclang="", langname="Korean", default={
                sans="", -- Use core_font_package_list if you want to have common fonts for CJK
                serif="",
                mono="" },
   recommends={},
   inputmethod="ibus-hangul",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ku", fclang="", langname="Kurdish", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="lo", fclang="", langname="Lao", default={
                sans="google-noto-sans-lao-vf-fonts",
                serif="google-noto-serif-lao-vf-fonts",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="lt", fclang="", langname="Lithuanian", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="lv", fclang="", langname="Latvian", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="mai", fclang="", langname="Maithili", default={
                sans="google-noto-sans-devanagari-vf-fonts",
                serif="google-noto-serif-devanagari-vf-fonts",
                mono="" },
   recommends={ "google-noto-sans-devanagari-ui-vf-fonts",
                "lohit-devanagari-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="mk", fclang="", langname="Macedonian", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ml", fclang="", langname="Malayalam", default={
                sans="rit-meera-new-fonts",
                serif="rit-rachana-fonts",
                mono="" },
   recommends={ "google-noto-sans-malayalam-vf-fonts",
                "google-noto-sans-malayalam-ui-vf-fonts",
                "google-noto-serif-malayalam-vf-fonts",
                "lohit-malayalam-fonts",
                "samyak-malayalam-fonts",
                "smc-anjalioldlipi-fonts",
                "smc-dyuthi-fonts",
                "smc-raghumalayalamsans-fonts",
                "smc-suruma-fonts",
                "rit-sundar-fonts",
                "rit-panmana-fonts",
                "rit-ezhuthu-fonts",
                "rit-tn-joy-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="mni", fclang="", langname="Manipuri", default={
                sans="google-noto-sans-meetei-mayek-vf-fonts",
                serif="",
                mono="" },
   recommends={},
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="mr", fclang="", langname="Marathi", default={
                sans="google-noto-sans-devanagari-vf-fonts",
                serif="google-noto-serif-devanagari-vf-fonts",
                mono="" },
   recommends={ "google-noto-sans-devanagari-ui-vf-fonts",
                "lohit-marathi-fonts",
                "samyak-devanagari-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ms", fclang="", langname="Malay", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="my", fclang="", langname="Burmese", default={
                sans="sil-padauk-fonts",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="nb", fclang="", langname="Norwegian", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ne", fclang="", langname="Nepali", default={
                sans="madan-fonts",
                serif="",
                mono="" },
   recommends={ "google-noto-sans-devanagari-vf-fonts",
                "google-noto-sans-devanagari-ui-vf-fonts",
                "google-noto-serif-devanagari-vf-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="nl", fclang="", langname="Dutch", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="nn", fclang="", langname="Nynorsk", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="nqo", fclang="", langname="N'Ko", default={
                 sans="google-noto-sans-nko-fonts",
                 serif="",
                 mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="nr", fclang="", langname="Southern Ndebele", default={
                sans="",
                serif="",
                mono="" },
   recommends={},
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="nso", fclang="", langname="Northern Sotho", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="or", fclang="", langname="Odia", default={
                sans="google-noto-sans-oriya-vf-fonts",
                serif="google-noto-serif-oriya-vf-fonts",
                mono="" },
   recommends={ "samyak-odia-fonts",
                "lohit-odia-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="pa", fclang="", langname="Punjabi", default={
                sans="google-noto-sans-gurmukhi-vf-fonts",
                serif="google-noto-serif-gurmukhi-vf-fonts",
                mono="" },
   recommends={ "saab-fonts",
                "lohit-gurmukhi-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="pl", fclang="", langname="Polish", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="pt_BR", fclang="pt", langname="Portuguese (Brazil)", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="pt", fclang="", langname="Portuguese", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ro", fclang="", langname="Romanian", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ru", fclang="", langname="Russian", default={
                sans="",
                serif="",
                mono="" },
   recommends={ "pt-sans-fonts",
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="sat", fclang="", langname="Santali", default={
                sans="google-noto-sans-ol-chiki-vf-fonts",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="si", fclang="", langname="Sinhala", default={
                sans="google-noto-sans-sinhala-vf-fonts",
                serif="google-noto-serif-sinhala-vf-fonts",
                mono="" },
   recommends={
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="sk", fclang="", langname="Slovak", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="sl", fclang="", langname="Slovenian", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="sq", fclang="", langname="Albanian", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="sr", fclang="", langname="Serbian", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ss", fclang="", langname="Swati", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="sv", fclang="", langname="Swedish", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="syr", fclang="", langname="Syriac", default={
                 sans="google-noto-sans-syriac-vf-fonts",
                 serif="",
                 mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ta", fclang="", langname="Tamil", default={
                sans="google-noto-sans-tamil-vf-fonts",
                serif="google-noto-serif-tamil-vf-fonts",
                mono="" },
   recommends={ "google-noto-sans-tamil-ui-vf-fonts",
                "lohit-tamil-fonts",
                "samyak-tamil-fonts",
                "serafettin-cartoon-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="te", fclang="", langname="Telugu", default={
                sans="google-noto-sans-telugu-vf-fonts",
                serif="google-noto-serif-telugu-vf-fonts",
                mono="" },
   recommends={ "google-noto-sans-telugu-ui-vf-fonts",
                "lohit-telugu-fonts",
                "pothana2000-fonts",
                "vemana2000-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="th", fclang="", langname="Thai", default={
                sans="google-noto-sans-thai-vf-fonts",
                serif="google-noto-serif-thai-vf-fonts",
                mono="" },
   recommends={ "tlwg-garuda-fonts",
                "tlwg-kinnari-fonts",
                "tlwg-laksaman-fonts",
                "tlwg-loma-fonts",
                "tlwg-mono-fonts",
                "tlwg-norasi-fonts",
                "tlwg-purisa-fonts",
                "tlwg-sawasdee-fonts",
                "tlwg-typewriter-fonts",
                "tlwg-typist-fonts",
                "tlwg-typo-fonts",
                "tlwg-umpush-fonts",
                "tlwg-waree-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="tn", fclang="", langname="Tswana", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="tr", fclang="", langname="Turkish", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ts", fclang="", langname="Tsonga", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="uk", fclang="", langname="Ukrainian", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ur", fclang="", langname="Urdu", default={
                sans="paktype-naskh-basic-fonts",
                serif="google-noto-naskh-arabic-vf-fonts",
                mono="" },
   recommends={ "nafees-nastaleeq-fonts",
                "nafees-web-naskh-fonts",
              },
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="ve", fclang="", langname="Venda", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="vi", fclang="", langname="Vietnamese", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   fedora_inputmethod="ibus-unikey",
   inputmethod="ibus-m17n",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="xh", fclang="", langname="Xhosa", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="yi", fclang="", langname="Yiddish", default={
                sans="google-noto-sans-hebrew-vf-fonts",
                serif="google-noto-serif-hebrew-vf-fonts",
                mono="" },
   recommends={ "culmus-aharoni-clm-fonts",
                "culmus-caladings-clm-fonts",
                "culmus-david-clm-fonts",
                "culmus-drugulin-clm-fonts",
                "culmus-ellinia-clm-fonts",
                "culmus-frank-ruehl-clm-fonts",
                "culmus-hadasim-clm-fonts",
                "culmus-keteryg-fonts",
                "culmus-miriam-clm-fonts",
                "culmus-miriam-mono-clm-fonts",
                "culmus-nachlieli-clm-fonts",
                "culmus-simple-clm-fonts",
                "culmus-stamashkenaz-clm-fonts",
                "culmus-stamsefarad-clm-fonts",
                "culmus-yehuda-clm-fonts",
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="zh_CN", fclang="", langname="Simplified Chinese", default={
                sans="", -- Use core_font_package_list if you want to have common fonts for CJK
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="ibus-libpinyin",
   meta={ requires={},
          recommends={}
   },
 },
 { lang="zh_HK", fclang="", langname="Hong Kong Traditional Chinese", default={
                sans="", -- Use core_font_package_list if you want to have common fonts for CJK
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="ibus-table-chinese-cangjie",
   meta={ requires={},
          recommends={ "ibus-table-chinese-quick" },
          fedora_recommends={ "ibus-table-chinese-quick",
                              "ibus-cangjie-engine-cangjie",
                              "ibus-cangjie-engine-quick",
                            }
   },
 },
 { lang="zh_TW", fclang="", langname="Taiwan", default={
                sans="", -- Use core_font_package_list if you want to have common fonts for CJK
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="ibus-chewing",
   meta={ requires={},
          recommends={ "ibus-table-chinese-cangjie",
                       "ibus-table-chinese-quick"
          }
   },
 },
 { lang="zu", fclang="", langname="Zulu", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
--[[
 { lang="", fclang="", langname="", default={
                sans="",
                serif="",
                mono="" },
   recommends={
              },
   inputmethod="",
   meta={ requires={},
          recommends={}
   },
 },
]]
}

--Miscellaneous functions
local function is_nonlatin(lang)
  local latinlang = { "af", "az", "bs", "ca", "cs", "cy", "da", "de", "en", "es", "et", "fil", "fi", "fo", "fr", "ga", "gd", "gl", "hr", "hu", "id", "is", "it", "kk", "ky", "lb", "lt", "lv", "mk", "mont", "ms", "mt", "nl", "no", "pl", "pt", "ro", "sk", "sl", "sq", "sr", "sv", "sw", "tg", "tk", "tr", "uz" }

  for i = 1, #latinlang do
    n, _ = string.find(lang, latinlang[i] .. "[_%a]*")
      if n == 1 then
        return false
      end
  end
  return true
end

local function is_cjk(lang)
  local pat = { "ja", "ko", "zh" }
  for i = 1, #pat do
    n, _ = string.find(lang, pat[i] .. "[_%a]*")
    if n == 1 then
      return true
    end
  end
  return false
end

local function build_deps(deps, tag, pkgs)
  local ret = ""
  for i = 1, #pkgs do
    ret = ret .. (pkgs[i] ~= "" and (tag .. ":   " .. pkgs[i] .. "\n") or "")
  end
  return deps .. ret
end

local function drop_duplicate(pkgs)
  local hash = {}
  local ret = {}
  for _, v in ipairs(pkgs) do
    if (not hash[v]) then
      table.insert(ret, v)
      hash[v] = true
    end
  end
  return ret
end

local function append_fontprov(deps, lang)
  return deps .. (lang ~= "" and ("Provides:   font(:lang=" .. lang .. ")\n") or "")
end

local function append_obsolete(deps, pkg)
  return deps .. build_deps("", "Obsoletes", {pkg .. " < %{version}-%{release}"}) .. build_deps("", "Provides", {pkg .. " = %{version}-%{release}"})
end

--
--Package template for langpacks-core-<lang>
--
local function defcorepkg(lang, fontlang, langname, inputmethod)
  local templ = [[
%package core-%{_lang}
Summary: %{_langname} langpacks core meta-package
Requires: default-fonts-%{_fontlang}
%{?_req}
%description core-%{_lang}
This package provides %{_langname} core langpacks packages.

%package -n %{_pkgname}
Summary:    Metapackage to install %{_summary1} for %{_summary2}
%{?_req}
%description -n %{_pkgname}
This package provides %{_summary1} package set(s) for %{_summary2}

%package %{_lang}
Summary: %{_langname} langpacks meta-package
Requires: %{name}-core-%{_lang}
Requires: %{name}-fonts-%{_fontlang}
%{?_req}
%description %{_lang}
This package provides %{_langname} langpacks meta-package.

%package -n default-fonts
Summary: Meta package to install all the default fonts
Requires: default-fonts-core = %{version}-%{release}
Requires: default-fonts-cjk = %{version}-%{release}
Requires: default-fonts-other = %{version}-%{release}
%description -n default-fonts
This package provides easier way to install all the default fonts meta packages
for all the languages.

%package -n default-fonts-core
Summary: Meta package to install sans/serif/mono/emoji/math default fonts meta packages for Western characters
Requires: default-fonts-core-sans = %{version}-%{release}
Requires: default-fonts-core-serif = %{version}-%{release}
Requires: default-fonts-core-mono = %{version}-%{release}
Requires: default-fonts-core-emoji = %{version}-%{release}
Requires: default-fonts-core-math = %{version}-%{release}
%description -n default-fonts-core
This package provides easier way to install all variants of default fonts
meta packages for Western characters.

%package -n default-fonts-cjk
Summary: Meta package to install sans/serif/mono/emoji/math default fonts meta packages for CJK
Requires: default-fonts-cjk-sans = %{version}-%{release}
Requires: default-fonts-cjk-serif = %{version}-%{release}
Requires: default-fonts-cjk-mono = %{version}-%{release}
%description -n default-fonts-cjk
This package provides easier way to install all variants of default fonts
meta packages for CJK languages.

%package -n default-fonts-other
Summary: Meta package to install sans/serif/mono/emoji/math default fonts meta packages for non-CJK
Requires: default-fonts-other-sans = %{version}-%{release}
Requires: default-fonts-other-serif = %{version}-%{release}
Requires: default-fonts-other-mono = %{version}-%{release}
%description -n default-fonts-other
This package provides easier way to install all variants of default fonts
meta packages for non-CJK languages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# nothing to prep

%build

%{langpacks_metainfo_lpc}
%{langpacks_metainfo_lp}
%{langpacks_metainfo_df}
%{langpacks_metainfo_lf}
%install
mkdir -p %{buildroot}/usr/share/metainfo
DESTDIR=%{buildroot} appstream-util split-appstream org.fedoraproject.LangPacks-Core.xml
DESTDIR=%{buildroot} appstream-util split-appstream org.fedoraproject.LangPacks.xml
DESTDIR=%{buildroot} appstream-util split-appstream org.fedoraproject.default-fonts.xml
DESTDIR=%{buildroot} appstream-util split-appstream org.fedoraproject.langpacks-fonts.xml
%oreon_autofiles default-fonts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles default-fonts-core usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles default-fonts-cjk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles default-fonts-other usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n langpacks-fonts-af -f %{oreon_filedir}/langpacks-fonts-af.list
%files -n langpacks-core-af -f %{oreon_filedir}/langpacks-core-af.list
%files -n langpacks-af -f %{oreon_filedir}/langpacks-af.list
%files -n default-fonts-am -f %{oreon_filedir}/default-fonts-am.list
%files -n langpacks-fonts-am -f %{oreon_filedir}/langpacks-fonts-am.list
%files -n langpacks-core-am -f %{oreon_filedir}/langpacks-core-am.list
%files -n langpacks-am -f %{oreon_filedir}/langpacks-am.list
%files -n default-fonts-ar -f %{oreon_filedir}/default-fonts-ar.list
%files -n langpacks-fonts-ar -f %{oreon_filedir}/langpacks-fonts-ar.list
%files -n langpacks-core-ar -f %{oreon_filedir}/langpacks-core-ar.list
%files -n langpacks-ar -f %{oreon_filedir}/langpacks-ar.list
%files -n default-fonts-as -f %{oreon_filedir}/default-fonts-as.list
%files -n langpacks-fonts-as -f %{oreon_filedir}/langpacks-fonts-as.list
%files -n langpacks-core-as -f %{oreon_filedir}/langpacks-core-as.list
%files -n langpacks-as -f %{oreon_filedir}/langpacks-as.list
%files -n default-fonts-ast -f %{oreon_filedir}/default-fonts-ast.list
%files -n langpacks-fonts-ast -f %{oreon_filedir}/langpacks-fonts-ast.list
%files -n langpacks-core-ast -f %{oreon_filedir}/langpacks-core-ast.list
%files -n langpacks-ast -f %{oreon_filedir}/langpacks-ast.list
%files -n default-fonts-be -f %{oreon_filedir}/default-fonts-be.list
%files -n langpacks-fonts-be -f %{oreon_filedir}/langpacks-fonts-be.list
%files -n langpacks-core-be -f %{oreon_filedir}/langpacks-core-be.list
%files -n langpacks-be -f %{oreon_filedir}/langpacks-be.list
%files -n default-fonts-bg -f %{oreon_filedir}/default-fonts-bg.list
%files -n langpacks-fonts-bg -f %{oreon_filedir}/langpacks-fonts-bg.list
%files -n langpacks-core-bg -f %{oreon_filedir}/langpacks-core-bg.list
%files -n langpacks-bg -f %{oreon_filedir}/langpacks-bg.list
%files -n default-fonts-bn -f %{oreon_filedir}/default-fonts-bn.list
%files -n langpacks-fonts-bn -f %{oreon_filedir}/langpacks-fonts-bn.list
%files -n langpacks-core-bn -f %{oreon_filedir}/langpacks-core-bn.list
%files -n langpacks-bn -f %{oreon_filedir}/langpacks-bn.list
%files -n default-fonts-bo -f %{oreon_filedir}/default-fonts-bo.list
%files -n langpacks-fonts-bo -f %{oreon_filedir}/langpacks-fonts-bo.list
%files -n langpacks-core-bo -f %{oreon_filedir}/langpacks-core-bo.list
%files -n langpacks-bo -f %{oreon_filedir}/langpacks-bo.list
%files -n default-fonts-br -f %{oreon_filedir}/default-fonts-br.list
%files -n langpacks-fonts-br -f %{oreon_filedir}/langpacks-fonts-br.list
%files -n langpacks-core-br -f %{oreon_filedir}/langpacks-core-br.list
%files -n langpacks-br -f %{oreon_filedir}/langpacks-br.list
%files -n langpacks-fonts-bs -f %{oreon_filedir}/langpacks-fonts-bs.list
%files -n langpacks-core-bs -f %{oreon_filedir}/langpacks-core-bs.list
%files -n langpacks-bs -f %{oreon_filedir}/langpacks-bs.list
%files -n langpacks-fonts-ca -f %{oreon_filedir}/langpacks-fonts-ca.list
%files -n langpacks-core-ca -f %{oreon_filedir}/langpacks-core-ca.list
%files -n langpacks-ca -f %{oreon_filedir}/langpacks-ca.list
%files -n default-fonts-chr -f %{oreon_filedir}/default-fonts-chr.list
%files -n langpacks-fonts-chr -f %{oreon_filedir}/langpacks-fonts-chr.list
%files -n langpacks-core-chr -f %{oreon_filedir}/langpacks-core-chr.list
%files -n langpacks-chr -f %{oreon_filedir}/langpacks-chr.list
%files -n langpacks-fonts-cs -f %{oreon_filedir}/langpacks-fonts-cs.list
%files -n langpacks-core-cs -f %{oreon_filedir}/langpacks-core-cs.list
%files -n langpacks-cs -f %{oreon_filedir}/langpacks-cs.list
%files -n langpacks-fonts-cy -f %{oreon_filedir}/langpacks-fonts-cy.list
%files -n langpacks-core-cy -f %{oreon_filedir}/langpacks-core-cy.list
%files -n langpacks-cy -f %{oreon_filedir}/langpacks-cy.list
%files -n langpacks-fonts-da -f %{oreon_filedir}/langpacks-fonts-da.list
%files -n langpacks-core-da -f %{oreon_filedir}/langpacks-core-da.list
%files -n langpacks-da -f %{oreon_filedir}/langpacks-da.list
%files -n langpacks-fonts-de -f %{oreon_filedir}/langpacks-fonts-de.list
%files -n langpacks-core-de -f %{oreon_filedir}/langpacks-core-de.list
%files -n langpacks-de -f %{oreon_filedir}/langpacks-de.list
%files -n default-fonts-dv -f %{oreon_filedir}/default-fonts-dv.list
%files -n langpacks-fonts-dv -f %{oreon_filedir}/langpacks-fonts-dv.list
%files -n langpacks-core-dv -f %{oreon_filedir}/langpacks-core-dv.list
%files -n langpacks-dv -f %{oreon_filedir}/langpacks-dv.list
%files -n default-fonts-dz -f %{oreon_filedir}/default-fonts-dz.list
%files -n langpacks-fonts-dz -f %{oreon_filedir}/langpacks-fonts-dz.list
%files -n langpacks-core-dz -f %{oreon_filedir}/langpacks-core-dz.list
%files -n langpacks-dz -f %{oreon_filedir}/langpacks-dz.list
%files -n default-fonts-el -f %{oreon_filedir}/default-fonts-el.list
%files -n langpacks-fonts-el -f %{oreon_filedir}/langpacks-fonts-el.list
%files -n langpacks-core-el -f %{oreon_filedir}/langpacks-core-el.list
%files -n langpacks-el -f %{oreon_filedir}/langpacks-el.list
%files -n langpacks-fonts-en -f %{oreon_filedir}/langpacks-fonts-en.list
%files -n langpacks-core-en -f %{oreon_filedir}/langpacks-core-en.list
%files -n langpacks-en -f %{oreon_filedir}/langpacks-en.list
%files -n langpacks-core-en_GB -f %{oreon_filedir}/langpacks-core-en_GB.list
%files -n langpacks-en_GB -f %{oreon_filedir}/langpacks-en_GB.list
%files -n default-fonts-eo -f %{oreon_filedir}/default-fonts-eo.list
%files -n langpacks-fonts-eo -f %{oreon_filedir}/langpacks-fonts-eo.list
%files -n langpacks-core-eo -f %{oreon_filedir}/langpacks-core-eo.list
%files -n langpacks-eo -f %{oreon_filedir}/langpacks-eo.list
%files -n langpacks-fonts-es -f %{oreon_filedir}/langpacks-fonts-es.list
%files -n langpacks-core-es -f %{oreon_filedir}/langpacks-core-es.list
%files -n langpacks-es -f %{oreon_filedir}/langpacks-es.list
%files -n langpacks-fonts-et -f %{oreon_filedir}/langpacks-fonts-et.list
%files -n langpacks-core-et -f %{oreon_filedir}/langpacks-core-et.list
%files -n langpacks-et -f %{oreon_filedir}/langpacks-et.list
%files -n default-fonts-eu -f %{oreon_filedir}/default-fonts-eu.list
%files -n langpacks-fonts-eu -f %{oreon_filedir}/langpacks-fonts-eu.list
%files -n langpacks-core-eu -f %{oreon_filedir}/langpacks-core-eu.list
%files -n langpacks-eu -f %{oreon_filedir}/langpacks-eu.list
%files -n default-fonts-fa -f %{oreon_filedir}/default-fonts-fa.list
%files -n langpacks-fonts-fa -f %{oreon_filedir}/langpacks-fonts-fa.list
%files -n langpacks-core-fa -f %{oreon_filedir}/langpacks-core-fa.list
%files -n langpacks-fa -f %{oreon_filedir}/langpacks-fa.list
%files -n langpacks-fonts-fi -f %{oreon_filedir}/langpacks-fonts-fi.list
%files -n langpacks-core-fi -f %{oreon_filedir}/langpacks-core-fi.list
%files -n langpacks-fi -f %{oreon_filedir}/langpacks-fi.list
%files -n langpacks-fonts-fr -f %{oreon_filedir}/langpacks-fonts-fr.list
%files -n langpacks-core-fr -f %{oreon_filedir}/langpacks-core-fr.list
%files -n langpacks-fr -f %{oreon_filedir}/langpacks-fr.list
%files -n langpacks-fonts-ga -f %{oreon_filedir}/langpacks-fonts-ga.list
%files -n langpacks-core-ga -f %{oreon_filedir}/langpacks-core-ga.list
%files -n langpacks-ga -f %{oreon_filedir}/langpacks-ga.list
%files -n langpacks-fonts-gl -f %{oreon_filedir}/langpacks-fonts-gl.list
%files -n langpacks-core-gl -f %{oreon_filedir}/langpacks-core-gl.list
%files -n langpacks-gl -f %{oreon_filedir}/langpacks-gl.list
%files -n default-fonts-got -f %{oreon_filedir}/default-fonts-got.list
%files -n langpacks-fonts-got -f %{oreon_filedir}/langpacks-fonts-got.list
%files -n langpacks-core-got -f %{oreon_filedir}/langpacks-core-got.list
%files -n langpacks-got -f %{oreon_filedir}/langpacks-got.list
%files -n default-fonts-gu -f %{oreon_filedir}/default-fonts-gu.list
%files -n langpacks-fonts-gu -f %{oreon_filedir}/langpacks-fonts-gu.list
%files -n langpacks-core-gu -f %{oreon_filedir}/langpacks-core-gu.list
%files -n langpacks-gu -f %{oreon_filedir}/langpacks-gu.list
%files -n default-fonts-he -f %{oreon_filedir}/default-fonts-he.list
%files -n langpacks-fonts-he -f %{oreon_filedir}/langpacks-fonts-he.list
%files -n langpacks-core-he -f %{oreon_filedir}/langpacks-core-he.list
%files -n langpacks-he -f %{oreon_filedir}/langpacks-he.list
%files -n default-fonts-hi -f %{oreon_filedir}/default-fonts-hi.list
%files -n langpacks-fonts-hi -f %{oreon_filedir}/langpacks-fonts-hi.list
%files -n langpacks-core-hi -f %{oreon_filedir}/langpacks-core-hi.list
%files -n langpacks-hi -f %{oreon_filedir}/langpacks-hi.list
%files -n langpacks-fonts-hr -f %{oreon_filedir}/langpacks-fonts-hr.list
%files -n langpacks-core-hr -f %{oreon_filedir}/langpacks-core-hr.list
%files -n langpacks-hr -f %{oreon_filedir}/langpacks-hr.list
%files -n langpacks-fonts-hu -f %{oreon_filedir}/langpacks-fonts-hu.list
%files -n langpacks-core-hu -f %{oreon_filedir}/langpacks-core-hu.list
%files -n langpacks-hu -f %{oreon_filedir}/langpacks-hu.list
%files -n default-fonts-hy -f %{oreon_filedir}/default-fonts-hy.list
%files -n langpacks-fonts-hy -f %{oreon_filedir}/langpacks-fonts-hy.list
%files -n langpacks-core-hy -f %{oreon_filedir}/langpacks-core-hy.list
%files -n langpacks-hy -f %{oreon_filedir}/langpacks-hy.list
%files -n default-fonts-ia -f %{oreon_filedir}/default-fonts-ia.list
%files -n langpacks-fonts-ia -f %{oreon_filedir}/langpacks-fonts-ia.list
%files -n langpacks-core-ia -f %{oreon_filedir}/langpacks-core-ia.list
%files -n langpacks-ia -f %{oreon_filedir}/langpacks-ia.list
%files -n langpacks-fonts-id -f %{oreon_filedir}/langpacks-fonts-id.list
%files -n langpacks-core-id -f %{oreon_filedir}/langpacks-core-id.list
%files -n langpacks-id -f %{oreon_filedir}/langpacks-id.list
%files -n default-fonts-ii -f %{oreon_filedir}/default-fonts-ii.list
%files -n langpacks-fonts-ii -f %{oreon_filedir}/langpacks-fonts-ii.list
%files -n langpacks-core-ii -f %{oreon_filedir}/langpacks-core-ii.list
%files -n langpacks-ii -f %{oreon_filedir}/langpacks-ii.list
%files -n langpacks-fonts-is -f %{oreon_filedir}/langpacks-fonts-is.list
%files -n langpacks-core-is -f %{oreon_filedir}/langpacks-core-is.list
%files -n langpacks-is -f %{oreon_filedir}/langpacks-is.list
%files -n langpacks-fonts-it -f %{oreon_filedir}/langpacks-fonts-it.list
%files -n langpacks-core-it -f %{oreon_filedir}/langpacks-core-it.list
%files -n langpacks-it -f %{oreon_filedir}/langpacks-it.list
%files -n default-fonts-iu -f %{oreon_filedir}/default-fonts-iu.list
%files -n langpacks-fonts-iu -f %{oreon_filedir}/langpacks-fonts-iu.list
%files -n langpacks-core-iu -f %{oreon_filedir}/langpacks-core-iu.list
%files -n langpacks-iu -f %{oreon_filedir}/langpacks-iu.list
%files -n langpacks-fonts-ja -f %{oreon_filedir}/langpacks-fonts-ja.list
%files -n langpacks-core-ja -f %{oreon_filedir}/langpacks-core-ja.list
%files -n langpacks-ja -f %{oreon_filedir}/langpacks-ja.list
%files -n default-fonts-kab -f %{oreon_filedir}/default-fonts-kab.list
%files -n langpacks-fonts-kab -f %{oreon_filedir}/langpacks-fonts-kab.list
%files -n langpacks-core-kab -f %{oreon_filedir}/langpacks-core-kab.list
%files -n langpacks-kab -f %{oreon_filedir}/langpacks-kab.list
%files -n default-fonts-ka -f %{oreon_filedir}/default-fonts-ka.list
%files -n langpacks-fonts-ka -f %{oreon_filedir}/langpacks-fonts-ka.list
%files -n langpacks-core-ka -f %{oreon_filedir}/langpacks-core-ka.list
%files -n langpacks-ka -f %{oreon_filedir}/langpacks-ka.list
%files -n langpacks-fonts-kk -f %{oreon_filedir}/langpacks-fonts-kk.list
%files -n langpacks-core-kk -f %{oreon_filedir}/langpacks-core-kk.list
%files -n langpacks-kk -f %{oreon_filedir}/langpacks-kk.list
%files -n default-fonts-km -f %{oreon_filedir}/default-fonts-km.list
%files -n langpacks-fonts-km -f %{oreon_filedir}/langpacks-fonts-km.list
%files -n langpacks-core-km -f %{oreon_filedir}/langpacks-core-km.list
%files -n langpacks-km -f %{oreon_filedir}/langpacks-km.list
%files -n default-fonts-kn -f %{oreon_filedir}/default-fonts-kn.list
%files -n langpacks-fonts-kn -f %{oreon_filedir}/langpacks-fonts-kn.list
%files -n langpacks-core-kn -f %{oreon_filedir}/langpacks-core-kn.list
%files -n langpacks-kn -f %{oreon_filedir}/langpacks-kn.list
%files -n langpacks-fonts-ko -f %{oreon_filedir}/langpacks-fonts-ko.list
%files -n langpacks-core-ko -f %{oreon_filedir}/langpacks-core-ko.list
%files -n langpacks-ko -f %{oreon_filedir}/langpacks-ko.list
%files -n default-fonts-ku -f %{oreon_filedir}/default-fonts-ku.list
%files -n langpacks-fonts-ku -f %{oreon_filedir}/langpacks-fonts-ku.list
%files -n langpacks-core-ku -f %{oreon_filedir}/langpacks-core-ku.list
%files -n langpacks-ku -f %{oreon_filedir}/langpacks-ku.list
%files -n default-fonts-lo -f %{oreon_filedir}/default-fonts-lo.list
%files -n langpacks-fonts-lo -f %{oreon_filedir}/langpacks-fonts-lo.list
%files -n langpacks-core-lo -f %{oreon_filedir}/langpacks-core-lo.list
%files -n langpacks-lo -f %{oreon_filedir}/langpacks-lo.list
%files -n langpacks-fonts-lt -f %{oreon_filedir}/langpacks-fonts-lt.list
%files -n langpacks-core-lt -f %{oreon_filedir}/langpacks-core-lt.list
%files -n langpacks-lt -f %{oreon_filedir}/langpacks-lt.list
%files -n langpacks-fonts-lv -f %{oreon_filedir}/langpacks-fonts-lv.list
%files -n langpacks-core-lv -f %{oreon_filedir}/langpacks-core-lv.list
%files -n langpacks-lv -f %{oreon_filedir}/langpacks-lv.list
%files -n default-fonts-mai -f %{oreon_filedir}/default-fonts-mai.list
%files -n langpacks-fonts-mai -f %{oreon_filedir}/langpacks-fonts-mai.list
%files -n langpacks-core-mai -f %{oreon_filedir}/langpacks-core-mai.list
%files -n langpacks-mai -f %{oreon_filedir}/langpacks-mai.list
%files -n langpacks-fonts-mk -f %{oreon_filedir}/langpacks-fonts-mk.list
%files -n langpacks-core-mk -f %{oreon_filedir}/langpacks-core-mk.list
%files -n langpacks-mk -f %{oreon_filedir}/langpacks-mk.list
%files -n default-fonts-ml -f %{oreon_filedir}/default-fonts-ml.list
%files -n langpacks-fonts-ml -f %{oreon_filedir}/langpacks-fonts-ml.list
%files -n langpacks-core-ml -f %{oreon_filedir}/langpacks-core-ml.list
%files -n langpacks-ml -f %{oreon_filedir}/langpacks-ml.list
%files -n default-fonts-mni -f %{oreon_filedir}/default-fonts-mni.list
%files -n langpacks-fonts-mni -f %{oreon_filedir}/langpacks-fonts-mni.list
%files -n langpacks-core-mni -f %{oreon_filedir}/langpacks-core-mni.list
%files -n langpacks-mni -f %{oreon_filedir}/langpacks-mni.list
%files -n default-fonts-mr -f %{oreon_filedir}/default-fonts-mr.list
%files -n langpacks-fonts-mr -f %{oreon_filedir}/langpacks-fonts-mr.list
%files -n langpacks-core-mr -f %{oreon_filedir}/langpacks-core-mr.list
%files -n langpacks-mr -f %{oreon_filedir}/langpacks-mr.list
%files -n langpacks-fonts-ms -f %{oreon_filedir}/langpacks-fonts-ms.list
%files -n langpacks-core-ms -f %{oreon_filedir}/langpacks-core-ms.list
%files -n langpacks-ms -f %{oreon_filedir}/langpacks-ms.list
%files -n default-fonts-my -f %{oreon_filedir}/default-fonts-my.list
%files -n langpacks-fonts-my -f %{oreon_filedir}/langpacks-fonts-my.list
%files -n langpacks-core-my -f %{oreon_filedir}/langpacks-core-my.list
%files -n langpacks-my -f %{oreon_filedir}/langpacks-my.list
%files -n default-fonts-nb -f %{oreon_filedir}/default-fonts-nb.list
%files -n langpacks-fonts-nb -f %{oreon_filedir}/langpacks-fonts-nb.list
%files -n langpacks-core-nb -f %{oreon_filedir}/langpacks-core-nb.list
%files -n langpacks-nb -f %{oreon_filedir}/langpacks-nb.list
%files -n default-fonts-ne -f %{oreon_filedir}/default-fonts-ne.list
%files -n langpacks-fonts-ne -f %{oreon_filedir}/langpacks-fonts-ne.list
%files -n langpacks-core-ne -f %{oreon_filedir}/langpacks-core-ne.list
%files -n langpacks-ne -f %{oreon_filedir}/langpacks-ne.list
%files -n langpacks-fonts-nl -f %{oreon_filedir}/langpacks-fonts-nl.list
%files -n langpacks-core-nl -f %{oreon_filedir}/langpacks-core-nl.list
%files -n langpacks-nl -f %{oreon_filedir}/langpacks-nl.list
%files -n default-fonts-nn -f %{oreon_filedir}/default-fonts-nn.list
%files -n langpacks-fonts-nn -f %{oreon_filedir}/langpacks-fonts-nn.list
%files -n langpacks-core-nn -f %{oreon_filedir}/langpacks-core-nn.list
%files -n langpacks-nn -f %{oreon_filedir}/langpacks-nn.list
%files -n default-fonts-nqo -f %{oreon_filedir}/default-fonts-nqo.list
%files -n langpacks-fonts-nqo -f %{oreon_filedir}/langpacks-fonts-nqo.list
%files -n langpacks-core-nqo -f %{oreon_filedir}/langpacks-core-nqo.list
%files -n langpacks-nqo -f %{oreon_filedir}/langpacks-nqo.list
%files -n default-fonts-nr -f %{oreon_filedir}/default-fonts-nr.list
%files -n langpacks-fonts-nr -f %{oreon_filedir}/langpacks-fonts-nr.list
%files -n langpacks-core-nr -f %{oreon_filedir}/langpacks-core-nr.list
%files -n langpacks-nr -f %{oreon_filedir}/langpacks-nr.list
%files -n default-fonts-nso -f %{oreon_filedir}/default-fonts-nso.list
%files -n langpacks-fonts-nso -f %{oreon_filedir}/langpacks-fonts-nso.list
%files -n langpacks-core-nso -f %{oreon_filedir}/langpacks-core-nso.list
%files -n langpacks-nso -f %{oreon_filedir}/langpacks-nso.list
%files -n default-fonts-or -f %{oreon_filedir}/default-fonts-or.list
%files -n langpacks-fonts-or -f %{oreon_filedir}/langpacks-fonts-or.list
%files -n langpacks-core-or -f %{oreon_filedir}/langpacks-core-or.list
%files -n langpacks-or -f %{oreon_filedir}/langpacks-or.list
%files -n default-fonts-pa -f %{oreon_filedir}/default-fonts-pa.list
%files -n langpacks-fonts-pa -f %{oreon_filedir}/langpacks-fonts-pa.list
%files -n langpacks-core-pa -f %{oreon_filedir}/langpacks-core-pa.list
%files -n langpacks-pa -f %{oreon_filedir}/langpacks-pa.list
%files -n langpacks-fonts-pl -f %{oreon_filedir}/langpacks-fonts-pl.list
%files -n langpacks-core-pl -f %{oreon_filedir}/langpacks-core-pl.list
%files -n langpacks-pl -f %{oreon_filedir}/langpacks-pl.list
%files -n langpacks-core-pt_BR -f %{oreon_filedir}/langpacks-core-pt_BR.list
%files -n langpacks-pt_BR -f %{oreon_filedir}/langpacks-pt_BR.list
%files -n langpacks-fonts-pt -f %{oreon_filedir}/langpacks-fonts-pt.list
%files -n langpacks-core-pt -f %{oreon_filedir}/langpacks-core-pt.list
%files -n langpacks-pt -f %{oreon_filedir}/langpacks-pt.list
%files -n langpacks-fonts-ro -f %{oreon_filedir}/langpacks-fonts-ro.list
%files -n langpacks-core-ro -f %{oreon_filedir}/langpacks-core-ro.list
%files -n langpacks-ro -f %{oreon_filedir}/langpacks-ro.list
%files -n default-fonts-ru -f %{oreon_filedir}/default-fonts-ru.list
%files -n langpacks-fonts-ru -f %{oreon_filedir}/langpacks-fonts-ru.list
%files -n langpacks-core-ru -f %{oreon_filedir}/langpacks-core-ru.list
%files -n langpacks-ru -f %{oreon_filedir}/langpacks-ru.list
%files -n default-fonts-sat -f %{oreon_filedir}/default-fonts-sat.list
%files -n langpacks-fonts-sat -f %{oreon_filedir}/langpacks-fonts-sat.list
%files -n langpacks-core-sat -f %{oreon_filedir}/langpacks-core-sat.list
%files -n langpacks-sat -f %{oreon_filedir}/langpacks-sat.list
%files -n default-fonts-si -f %{oreon_filedir}/default-fonts-si.list
%files -n langpacks-fonts-si -f %{oreon_filedir}/langpacks-fonts-si.list
%files -n langpacks-core-si -f %{oreon_filedir}/langpacks-core-si.list
%files -n langpacks-si -f %{oreon_filedir}/langpacks-si.list
%files -n langpacks-fonts-sk -f %{oreon_filedir}/langpacks-fonts-sk.list
%files -n langpacks-core-sk -f %{oreon_filedir}/langpacks-core-sk.list
%files -n langpacks-sk -f %{oreon_filedir}/langpacks-sk.list
%files -n langpacks-fonts-sl -f %{oreon_filedir}/langpacks-fonts-sl.list
%files -n langpacks-core-sl -f %{oreon_filedir}/langpacks-core-sl.list
%files -n langpacks-sl -f %{oreon_filedir}/langpacks-sl.list
%files -n langpacks-fonts-sq -f %{oreon_filedir}/langpacks-fonts-sq.list
%files -n langpacks-core-sq -f %{oreon_filedir}/langpacks-core-sq.list
%files -n langpacks-sq -f %{oreon_filedir}/langpacks-sq.list
%files -n langpacks-fonts-sr -f %{oreon_filedir}/langpacks-fonts-sr.list
%files -n langpacks-core-sr -f %{oreon_filedir}/langpacks-core-sr.list
%files -n langpacks-sr -f %{oreon_filedir}/langpacks-sr.list
%files -n default-fonts-ss -f %{oreon_filedir}/default-fonts-ss.list
%files -n langpacks-fonts-ss -f %{oreon_filedir}/langpacks-fonts-ss.list
%files -n langpacks-core-ss -f %{oreon_filedir}/langpacks-core-ss.list
%files -n langpacks-ss -f %{oreon_filedir}/langpacks-ss.list
%files -n langpacks-fonts-sv -f %{oreon_filedir}/langpacks-fonts-sv.list
%files -n langpacks-core-sv -f %{oreon_filedir}/langpacks-core-sv.list
%files -n langpacks-sv -f %{oreon_filedir}/langpacks-sv.list
%files -n default-fonts-syr -f %{oreon_filedir}/default-fonts-syr.list
%files -n langpacks-fonts-syr -f %{oreon_filedir}/langpacks-fonts-syr.list
%files -n langpacks-core-syr -f %{oreon_filedir}/langpacks-core-syr.list
%files -n langpacks-syr -f %{oreon_filedir}/langpacks-syr.list
%files -n default-fonts-ta -f %{oreon_filedir}/default-fonts-ta.list
%files -n langpacks-fonts-ta -f %{oreon_filedir}/langpacks-fonts-ta.list
%files -n langpacks-core-ta -f %{oreon_filedir}/langpacks-core-ta.list
%files -n langpacks-ta -f %{oreon_filedir}/langpacks-ta.list
%files -n default-fonts-te -f %{oreon_filedir}/default-fonts-te.list
%files -n langpacks-fonts-te -f %{oreon_filedir}/langpacks-fonts-te.list
%files -n langpacks-core-te -f %{oreon_filedir}/langpacks-core-te.list
%files -n langpacks-te -f %{oreon_filedir}/langpacks-te.list
%files -n default-fonts-th -f %{oreon_filedir}/default-fonts-th.list
%files -n langpacks-fonts-th -f %{oreon_filedir}/langpacks-fonts-th.list
%files -n langpacks-core-th -f %{oreon_filedir}/langpacks-core-th.list
%files -n langpacks-th -f %{oreon_filedir}/langpacks-th.list
%files -n default-fonts-tn -f %{oreon_filedir}/default-fonts-tn.list
%files -n langpacks-fonts-tn -f %{oreon_filedir}/langpacks-fonts-tn.list
%files -n langpacks-core-tn -f %{oreon_filedir}/langpacks-core-tn.list
%files -n langpacks-tn -f %{oreon_filedir}/langpacks-tn.list
%files -n langpacks-fonts-tr -f %{oreon_filedir}/langpacks-fonts-tr.list
%files -n langpacks-core-tr -f %{oreon_filedir}/langpacks-core-tr.list
%files -n langpacks-tr -f %{oreon_filedir}/langpacks-tr.list
%files -n default-fonts-ts -f %{oreon_filedir}/default-fonts-ts.list
%files -n langpacks-fonts-ts -f %{oreon_filedir}/langpacks-fonts-ts.list
%files -n langpacks-core-ts -f %{oreon_filedir}/langpacks-core-ts.list
%files -n langpacks-ts -f %{oreon_filedir}/langpacks-ts.list
%files -n default-fonts-uk -f %{oreon_filedir}/default-fonts-uk.list
%files -n langpacks-fonts-uk -f %{oreon_filedir}/langpacks-fonts-uk.list
%files -n langpacks-core-uk -f %{oreon_filedir}/langpacks-core-uk.list
%files -n langpacks-uk -f %{oreon_filedir}/langpacks-uk.list
%files -n default-fonts-ur -f %{oreon_filedir}/default-fonts-ur.list
%files -n langpacks-fonts-ur -f %{oreon_filedir}/langpacks-fonts-ur.list
%files -n langpacks-core-ur -f %{oreon_filedir}/langpacks-core-ur.list
%files -n langpacks-ur -f %{oreon_filedir}/langpacks-ur.list
%files -n default-fonts-ve -f %{oreon_filedir}/default-fonts-ve.list
%files -n langpacks-fonts-ve -f %{oreon_filedir}/langpacks-fonts-ve.list
%files -n langpacks-core-ve -f %{oreon_filedir}/langpacks-core-ve.list
%files -n langpacks-ve -f %{oreon_filedir}/langpacks-ve.list
%files -n default-fonts-vi -f %{oreon_filedir}/default-fonts-vi.list
%files -n langpacks-fonts-vi -f %{oreon_filedir}/langpacks-fonts-vi.list
%files -n langpacks-core-vi -f %{oreon_filedir}/langpacks-core-vi.list
%files -n langpacks-vi -f %{oreon_filedir}/langpacks-vi.list
%files -n default-fonts-xh -f %{oreon_filedir}/default-fonts-xh.list
%files -n langpacks-fonts-xh -f %{oreon_filedir}/langpacks-fonts-xh.list
%files -n langpacks-core-xh -f %{oreon_filedir}/langpacks-core-xh.list
%files -n langpacks-xh -f %{oreon_filedir}/langpacks-xh.list
%files -n default-fonts-yi -f %{oreon_filedir}/default-fonts-yi.list
%files -n langpacks-fonts-yi -f %{oreon_filedir}/langpacks-fonts-yi.list
%files -n langpacks-core-yi -f %{oreon_filedir}/langpacks-core-yi.list
%files -n langpacks-yi -f %{oreon_filedir}/langpacks-yi.list
%files -n langpacks-fonts-zh_CN -f %{oreon_filedir}/langpacks-fonts-zh_CN.list
%files -n langpacks-core-zh_CN -f %{oreon_filedir}/langpacks-core-zh_CN.list
%files -n langpacks-zh_CN -f %{oreon_filedir}/langpacks-zh_CN.list
%files -n langpacks-fonts-zh_HK -f %{oreon_filedir}/langpacks-fonts-zh_HK.list
%files -n langpacks-core-zh_HK -f %{oreon_filedir}/langpacks-core-zh_HK.list
%files -n langpacks-zh_HK -f %{oreon_filedir}/langpacks-zh_HK.list
%files -n langpacks-fonts-zh_TW -f %{oreon_filedir}/langpacks-fonts-zh_TW.list
%files -n langpacks-core-zh_TW -f %{oreon_filedir}/langpacks-core-zh_TW.list
%files -n langpacks-zh_TW -f %{oreon_filedir}/langpacks-zh_TW.list
%files -n default-fonts-zu -f %{oreon_filedir}/default-fonts-zu.list
%files -n langpacks-fonts-zu -f %{oreon_filedir}/langpacks-fonts-zu.list
%files -n langpacks-core-zu -f %{oreon_filedir}/langpacks-core-zu.list
%files -n langpacks-zu -f %{oreon_filedir}/langpacks-zu.list
%files -n default-fonts-cjk-sans -f %{oreon_filedir}/default-fonts-cjk-sans.list
%files -n default-fonts-other-sans -f %{oreon_filedir}/default-fonts-other-sans.list
%files -n default-fonts-other-serif -f %{oreon_filedir}/default-fonts-other-serif.list
%files -n default-fonts-cjk-serif -f %{oreon_filedir}/default-fonts-cjk-serif.list
%files -n default-fonts-other-mono -f %{oreon_filedir}/default-fonts-other-mono.list
%files -n default-fonts-cjk-mono -f %{oreon_filedir}/default-fonts-cjk-mono.list
%files -n default-fonts-core-sans -f %{oreon_filedir}/default-fonts-core-sans.list
%files -n default-fonts-core-serif -f %{oreon_filedir}/default-fonts-core-serif.list
%files -n default-fonts-core-mono -f %{oreon_filedir}/default-fonts-core-mono.list
%files -n default-fonts-core-emoji -f %{oreon_filedir}/default-fonts-core-emoji.list
%files -n default-fonts-core-math -f %{oreon_filedir}/default-fonts-core-math.list
%files -n default-fonts -f %{oreon_filedir}/default-fonts.list
%files -n default-fonts-core -f %{oreon_filedir}/default-fonts-core.list
%files -n default-fonts-cjk -f %{oreon_filedir}/default-fonts-cjk.list
%files -n default-fonts-other -f %{oreon_filedir}/default-fonts-other.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.3-1
- Prepare for Oreon 11 (RP1)
