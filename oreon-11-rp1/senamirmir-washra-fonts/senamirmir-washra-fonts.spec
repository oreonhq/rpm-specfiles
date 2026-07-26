%global source0_hash 6fb4961aeb2878fa855413eebbdbf3821a092faac0817d2c2ea63ef8dee0cf82

# SPDX-License-Identifier: MIT
%global archivename washra_fonts4-1

Version: 4.1
Release: 41%{?dist}
URL:     http://www.senamirmir.org/projects/typography/typeface.html

%global foundry           Senamirmir
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global common_description %{expand:
A set of high quality Unicode fonts for the  Geʼez (Ethiopic) script published
by the Senamirmir project. They can be used to write Ethiopic and Eritrean
languages (Amharic, Blin, Geʼez, Harari, Meʼen, Tigre, Tigrinya…).}

%global fontsummary a font family for the Geʼez (Ethiopic) script

%global fontfamily0       WashRa
%global fontsummary0      Senamirmir WashRa, %{fontsummary}
%global fontpkgheader0    %{expand:
Obsoletes: senamirmir-washra-fonts-common < %{version}-%{release}
}
%global fonts0            washrab.ttf washrasb.ttf
%global fontconfngs0      %{SOURCE10}
%global fontdescription   %{common_description}

%global fontfamily1       Fantuwua
%global fontsummary1      Senamirmir Fantuwua, %{fontsummary}
%global fontpkgheader1    %{expand:
Obsoletes: senamirmir-washra-fantuwua-fonts < %{version}-%{release}
}
%global fonts1            fantuwua.ttf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}
This package consists of the “Ethiopic Fantuwua” font family.}

%global fontfamily2       Hiwua
%global fontsummary2      Senamirmir Hiwua, %{fontsummary}
%global fontpkgheader2    %{expand:
Obsoletes: senamirmir-washra-hiwua-fonts < %{version}-%{release}
}
%global fonts2            hiwua.ttf
%global fontconfngs2      %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}
This package consists of the “Ethiopic Hiwua” font family.}

%global fontfamily3       Jiret
%global fontsummary3      Senamirmir Jiret, %{fontsummary}
%global fontpkgheader3    %{expand:
Obsoletes: senamirmir-washra-jiret-fonts < %{version}-%{release}
}
%global fonts3            jiret.ttf
%global fontconfngs3      %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}
This package consists of the “Ethiopic Jiret” font family.}

%global fontfamily4       Tint
%global fontsummary4      Senamirmir Tint, %{fontsummary}
%global fontpkgheader4    %{expand:
Obsoletes: senamirmir-washra-tint-fonts < %{version}-%{release}
}
%global fonts4            tint.ttf
%global fontconfngs4      %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}
This package consists of the “Ethiopic Tint” font family.}

%global fontfamily5       Wookianos
%global fontsummary5      Senamirmir Wookianos, %{fontsummary}
%global fontpkgheader5    %{expand:
Obsoletes: senamirmir-washra-wookianos-fonts < %{version}-%{release}
}
%global fonts5            wookianos.ttf
%global fontconfngs5      %{SOURCE15}
%global fontdescription5  %{expand:
%{common_description}
This package consists of the “Ethiopic Wookianos” font family.}

%global fontfamily6       Yebse
%global fontsummary6      Senamirmir Yebse, %{fontsummary}
%global fontpkgheader6    %{expand:
Obsoletes: senamirmir-washra-yebse-fonts < %{version}-%{release}
}
%global fonts6            yebse.ttf
%global fontconfngs6      %{SOURCE16}
%global fontdescription6  %{expand:
%{common_description}
This package consists of the “Ethiopic Yebse” font family.}

%global fontfamily7       Yigezu Bisrat Goffer
%global fontsummary7      Senamirmir Yigezu Bisrat Goffer, %{fontsummary}
%global fontpkgheader7    %{expand:
Obsoletes: senamirmir-washra-yigezu-bisrat-goffer-fonts < %{version}-%{release}
}
%global fonts7            goffer.ttf
%global fontconfngs7      %{SOURCE17}
%global fontdescription7  %{expand:
%{common_description}
This package consists of the “Ethiopic Yigezu Bisrat Goffer” font, a “Gothic
Goffer” decorative font. It is dedicated to Ato Yigezu Bisrat, whose 1963 book
“Ye-Ethiopia khine tsehifet” (Ethiopian Typography) provided the original
design that served as inspiration for this work.}

%global fontfamily8       Yigezu Bisrat Gothic
%global fontsummary8      Senamirmir Yigezu Bisrat Gothic, %{fontsummary}
%global fontpkgheader8    %{expand:
Obsoletes: senamirmir-washra-yigezu-bisrat-gothic-fonts < %{version}-%{release}
}
%global fonts8            yigezubisratgothic.ttf
%global fontconfngs8      %{SOURCE18}
%global fontdescription8  %{expand:
%{common_description}
This package consists of the “Ethiopic Yigezu Bisrat Gothic” font, a “Gothic”
decorative font. It is dedicated to Ato Yigezu Bisrat, whose 1963 book
“Ye-Ethiopia khine tsehifet” (Ethiopian Typography) provided inspiration for
this work.}

%global fontfamily9       Zelan
%global fontsummary9      Senamirmir Zelan, %{fontsummary}
%global fontpkgheader9    %{expand:
Obsoletes: senamirmir-washra-zelan-fonts < %{version}-%{release}
}
%global fonts9            zelan.ttf
%global fontconfngs9      %{SOURCE19}
%global fontdescription9  %{expand:
%{common_description}
This package consists of the “Ethiopic Zelan” font.}

Source0: http://www.senamirmir.org/downloads/%{archivename}.zip
# We need upstream or someone who knows local Ethiopian usage to suggest a
# classification we could relay to fontconfig. In the meanwhile, only three
# font families classified
Source10: 65-%{fontpkgname0}.xml
Source11: 65-%{fontpkgname1}.xml
Source12: 65-%{fontpkgname2}.xml
Source13: 65-%{fontpkgname3}.xml
Source14: 65-%{fontpkgname4}.xml
Source15: 65-%{fontpkgname5}.xml
Source16: 65-%{fontpkgname6}.xml
Source17: 65-%{fontpkgname7}.xml
Source18: 65-%{fontpkgname8}.xml
Source19: 65-%{fontpkgname9}.xml

%fontpkg -a

%fontmetapkg

%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q
%linuxtext *.txt

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%files doc
%license OFL.txt
%doc *.doc *.pdf

%changelog
%autochangelog
