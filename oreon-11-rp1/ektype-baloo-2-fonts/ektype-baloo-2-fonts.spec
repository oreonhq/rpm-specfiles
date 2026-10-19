%global source0_hash 8cb7e0ddd4af8a56bc447e6d8d66954f27b99b8538f52004bab173924f86f15b
Version: 1.640
Release:        1%{?dist}
URL:     https://ektype.in/baloo-family.html
%global foundry         ektype
%global fontlicense     OFL-1.1
%global fontlicenses    OFL.txt
%global fontdocs        README.md AUTHORS.txt CONTRIBUTORS.txt Copyright.txt
%global fontdocsex      %{fontlicenses}
%global common_description %{expand:
The Baloo 2 project consists of nine font families with unique local names for
each of the nine Indic scripts. Each family supports one Indic script plus
Latin, Latin Extended, and Vietnamese.
- Baloo 2 for Devanagari
- Baloo Bhai 2 for Gujarati
- Baloo Bhaina 2 for Odia
- Baloo Chettan 2 for Malayalam
- Baloo Da 2 for Bengali
- Baloo Paaji 2 for Gurmukhi
- Baloo Tamma 2 for Kannada
- Baloo Tammudu 2 for Telugu
- Baloo Thambi 2 for Tamil
It took a team of committed type designers to rear Baloo and raise it to be the
typeface we love. The Gurmukhi is designed by Shuchita Grover; Bangla by Noopur
Datye and Sulekha Rajkumar; Odia by Yesha Goshar, Manish Minz, and Shuchita
Grover; Gujarati by Noopur Datye and Supriya Tembe; Kannada by Divya Kowshik
and Shuchita Grover; Telugu by Maithili Shingre and Omkar Shende; Malayalam by
Maithili Shingre and Unnati Kotecha; and Tamil by Aadarsh Rajan. Baloo
Devanagari and Latin are collaboratively designed by Ek Type. Font engineering
and type design assistance by Girish Dalvi.}
%global fontfamily0       Baloo 2
%global fontsummary0      Baloo 2 Devanagari fonts
%global fonts0            TTF/Baloo2*.ttf
%global fontconfs0        %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}
Devanagari and latin fonts.}
%global fontfamily1       Baloo Bhai 2
%global fontsummary1      Baloo 2 Gujarati fonts
%global fonts1            TTF/BalooBhai2*.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}
Gujarati and latin fonts.}
%global fontfamily2       Baloo Bhaina 2
%global fontsummary2      Baloo 2 Odia fonts
%global fonts2            TTF/BalooBhaina2*.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}
Odia and latin fonts.}
%global fontfamily3       Baloo Chettan 2
%global fontsummary3      Baloo 2 Malayalam fonts
%global fonts3            TTF/BalooChettan2*.ttf
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}
Malayalam and latin fonts.}
%global fontfamily4       Baloo Da 2
%global fontsummary4      Baloo 2 Bengali fonts
%global fonts4            TTF/BalooDa2*.ttf
%global fontconfs4        %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}
Bengali and latin fonts.}
%global fontfamily5       Baloo Paaji 2
%global fontsummary5      Baloo 2 Gumurkhi fonts
%global fonts5            TTF/BalooPaaji2*.ttf
%global fontconfs5        %{SOURCE15}
%global fontdescription5  %{expand:
%{common_description}
Gumurkhi and latin fonts.}
%global fontfamily6       Baloo Tamma 2
%global fontsummary6      Baloo 2 Kannada fonts
%global fonts6            TTF/BalooTamma2*.ttf
%global fontconfs6        %{SOURCE16}
%global fontdescription6  %{expand:
%{common_description}
Kannada and latin fonts.}
%global fontfamily7       Baloo Tammudu 2
%global fontsummary7      Baloo 2 Telugu fonts
%global fonts7            TTF/BalooTammudu2*.ttf
%global fontconfs7        %{SOURCE17}
%global fontdescription7  %{expand:
%{common_description}
Telugu and latin fonts.}
%global fontfamily8       Baloo Thambi 2
%global fontsummary8      Baloo 2 Tamil fonts
%global fonts8            TTF/BalooThambi2*.ttf
%global fontconfs8        %{SOURCE18}
%global fontdescription8  %{expand:
%{common_description}
Tamil and latin fonts.}
Source0:        https://github.com/EkType/Baloo2/archive/%{version}/Baloo2-%{version}.tar.gz
Source10: 67-ektype-baloo-2-fonts.conf
Source11: 67-ektype-baloo-bhai-2-fonts.conf
Source12: 67-ektype-baloo-bhaina-2-fonts.conf
Source13: 67-ektype-baloo-chettan-2-fonts.conf
Source14: 67-ektype-baloo-da-2-fonts.conf
Source15: 67-ektype-baloo-paaji-2-fonts.conf
Source16: 67-ektype-baloo-tamma-2-fonts.conf
Source17: 67-ektype-baloo-tammudu-2-fonts.conf
Source18: 67-ektype-baloo-thambi-2-fonts.conf
%fontpkg -a
%fontmetapkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
BuildRequires:  fonttools
# /oreon:deps
%prep

%setup -n Baloo2-%{version}
%linuxtext *.txt

%build

for file in TTX/*;
  do  ttx $file;
done
mkdir TTF
mv TTX/*.ttf TTF
%fontbuild -a
%install
%fontinstall -a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck -a
%fontfiles -a
%files -f %{oreon_filedir}/main.list
%files -n bitmap-lucida-typewriter-fonts -f %{oreon_filedir}/bitmap-lucida-typewriter-fonts.list
%files -n bitmap-lucida-typewriter-opentype-fonts -f %{oreon_filedir}/bitmap-lucida-typewriter-opentype-fonts.list
%files -n bitmap-fangsongti-fonts -f %{oreon_filedir}/bitmap-fangsongti-fonts.list
%files -n bitmap-fangsongti-opentype-fonts -f %{oreon_filedir}/bitmap-fangsongti-opentype-fonts.list
%files -n bitmap-console-fonts -f %{oreon_filedir}/bitmap-console-fonts.list
%files -n bitmap-console-opentype-fonts -f %{oreon_filedir}/bitmap-console-opentype-fonts.list
%files -n bitmap-fixed-fonts -f %{oreon_filedir}/bitmap-fixed-fonts.list
%files -n bitmap-fixed-opentype-fonts -f %{oreon_filedir}/bitmap-fixed-opentype-fonts.list
%files -n bitmap-ecolier-court-fonts-all -f %{oreon_filedir}/bitmap-ecolier-court-fonts-all.list

%changelog

%autochangelog
