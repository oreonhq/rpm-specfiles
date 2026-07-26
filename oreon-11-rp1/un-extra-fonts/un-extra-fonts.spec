%global source0_hash 32a56acc06f264653bd151ec48c0811d07c198c2561e9f2efa8845e45b6b7407

# SPDX-License-Identifier: MIT

%global fontname    un-extra
%global alphatag    080608
%global archivename un-fonts-extra

BuildArch: noarch

Version: 1.0.2
Release: 0.43.%{alphatag}%{?dist}
License: GPL-2.0-only
URL:     http://kldp.net/projects/unfonts/

%global foundry           Un
%global fontlicenses      COPYING
%global fontdocs          README

%global common_description %{expand:
The UN set of Korean TrueType fonts is derived from the HLaTeX Type1 fonts \
made by Koaunghi Un in 1998. They were converted to TrueType with \
FontForge(PfaEdit) by Won-kyu Park in 2003. \
The Un Extra set is composed of: \
\
- UnPen, UnPenheulim: script \
- UnTaza: typewriter style \
- UnBom: decorative \
- UnShinmun \
- UnYetgul: old Korean printing style \
- UnJamoSora, UnJamoNovel, UnJamoDotum, UnJamoBatang \
- UnVada \
- UnPilgia: script
}

%global fontfamily1       Un Extra Bom
%global fontsummary1      Un Extra fonts - UnBom
%global fonts1            UnBom.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

This package includes UnBom, a decorative font.
}

%global fontfamily2       Un Extra JamoBatang
%global fontsummary2      Un Extra fonts - UnJamoBatang
%global fonts2            UnJamoBatang.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

This package includes the UnJamoBatang font.
}

%global fontfamily3       Un Extra JamoDotum
%global fontsummary3      Un Extra fonts - UnJamoDotum
%global fonts3            UnJamoDotum.ttf
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

This package includes the UNJamoDotum font.
}

%global fontfamily4       Un Extra JamoNovel
%global fontsummary4      Un Extra fonts - UnJamoNovel
%global fonts4            UnJamoNovel.ttf
%global fontconfs4        %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}

This package includes the UNJamoNovel font.
}

%global fontfamily5       Un Extra JamoSora
%global fontsummary5      Un Extra fonts - UnJamoSora
%global fonts5            UnJamoSora.ttf
%global fontconfs5        %{SOURCE15}
%global fontdescription5  %{expand:
%{common_description}

This package includes the UNJamoSora font.
}

%global fontfamily6       Un Extra Pen
%global fontsummary6      Un Extra fonts - UnPen
%global fonts6            UnPen.ttf
%global fontconfs6        %{SOURCE16}
%global fontdescription6  %{expand:
%{common_description}

This package includes UnPen, a script font.
}

%global fontfamily7       Un Extra Penheulim
%global fontsummary7      Un Extra fonts - UnPenheulim
%global fonts7            UnPenheulim.ttf
%global fontconfs7        %{SOURCE17}
%global fontdescription7  %{expand:
%{common_description}

This package includes UnPenheulim, a script font.
}

%global fontfamily8       Un Extra Pilgia
%global fontsummary8      Un Extra fonts - UnPilgia
%global fonts8            UnPilgia.ttf
%global fontconfs8        %{SOURCE18}
%global fontdescription8  %{expand:
%{common_description}

This package includes UnPilgia, a script font.
}

%global fontfamily9       Un Extra Shinmun
%global fontsummary9      Un Extra fonts - UnShinmun
%global fonts9            UnShinmun.ttf
%global fontconfs9        %{SOURCE19}
%global fontdescription9  %{expand:
%{common_description}

This package includes the UnShinmun font.
}

%global fontfamily10       Un Extra Taza
%global fontsummary10      Un Extra fonts - UnTaza
%global fontpkgheader10    %{expand:
Obsoletes:       %{name}-common < 1.0.2-0.36.080608
Provides:        %{name}-common = %{version}-%{release}
}
%global fonts10            UnTaza.ttf
%global fontconfs10        %{SOURCE20}
%global fontdescription10  %{expand:
%{common_description}

This package includes UnTaza, a typewriter font.
}

%global fontfamily11       Un Extra Vada
%global fontsummary11      Un Extra fonts - UnVada
%global fonts11            UnVada.ttf
%global fontconfs11        %{SOURCE21}
%global fontdescription11  %{expand:
%{common_description}

This package includes the UnVada font.
}

%global fontfamily12       Un Extra Yetgul
%global fontsummary12      Un Extra fonts - UnYetgul
%global fonts12            UnYetgul.ttf
%global fontconfs12        %{SOURCE22}
%global fontdescription12  %{expand:
%{common_description}

This package includes UnYetgul, an old Korean printing font.
}

Source0:  http://kldp.net/frs/download.php/4696/%{archivename}-%{version}-%{alphatag}.tar.gz
Source11: 67-un-extra-bom-fonts.conf
Source12: 67-un-extra-jamobatang-fonts.conf
Source13: 67-un-extra-jamodotum-fonts.conf
Source14: 67-un-extra-jamonovel-fonts.conf
Source15: 67-un-extra-jamosora-fonts.conf
Source16: 67-un-extra-pen-fonts.conf
Source17: 67-un-extra-penheulim-fonts.conf
Source18: 67-un-extra-pilgia-fonts.conf
Source19: 67-un-extra-shinmun-fonts.conf
Source20: 67-un-extra-taza-fonts.conf
Source21: 67-un-extra-vada-fonts.conf
Source22: 67-un-extra-yetgul-fonts.conf

Name:     %{fontname}-fonts
Summary:  Un Extra family of Korean TrueType fonts
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n un-fonts
%linuxtext COPYING README

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
