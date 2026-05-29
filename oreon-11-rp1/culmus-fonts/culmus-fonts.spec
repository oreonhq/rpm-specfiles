%global source0_hash c0c6873742d07544f6bacf2ad52eb9cb392974d56427938dc1dfbc8399c64d05

BuildArch: noarch
BuildRequires: /usr/bin/makeotfexe
BuildRequires: fontforge

Version:   0.133
Release:   16%{?dist}
License:   GPL-2.0-only
URL:       http://culmus.sourceforge.net

%global common_description %{expand:
The culmus-fonts package contains fonts for the display of
Hebrew from the Culmus project.}

%global foundry           CLM
%global fontlicenses      LICENSE GNU-GPL LICENSE LICENSE-BITSTREAM
%global fontdocs          CHANGES
%global fontdocsex        %{fontlicenses}

%global fontfamily1       Aharoni CLM
%global fontsummary1      Aharoni CLM, a sans-serif font family
%global fontpkgheader1    %{expand:
Obsoletes: culmus-aharoni-clm-fonts < 0.133-1
Provides:  culmus-aharoni-clm-fonts = %{version}-%{release}
}
%global fonts1            AharoniCLM-*.otf
%global fontconfs1        %{SOURCE1}
%global fontdescription1  %{expand:
%{common_description}

This package provides Aharoni CLM, a sans-serif font family.
}

%global fontfamily2       Caladings CLM
%global fontsummary2      Caladings CLM, a fantasy font family
%global fontpkgheader2    %{expand:
Obsoletes: culmus-caladings-clm-fonts < 0.133-1
Provides:  culmus-caladings-clm-fonts = %{version}-%{release}
}
%global fonts2            CaladingsCLM.otf
%global fontconfs2        %{SOURCE2}
%global fontdescription2  %{expand:
%{common_description}

This package provides Caladings CLM, a fantasy font family.
}

%global fontfamily3       David CLM
%global fontsummary3      David CLM, a serif font family
%global fontpkgheader3    %{expand:
Obsoletes: culmus-david-clm-fonts < 0.133-1
Provides:  culmus-david-clm-fonts = %{version}-%{release}
}
%global fonts3            DavidCLM-*.otf
%global fontconfs3        %{SOURCE3}
%global fontdescription3  %{expand:
%{common_description}

This package provides David CLM, a serif font family.
}

%global fontfamily4       Drugulin CLM
%global fontsummary4      Drugulin CLM, a serif font family
%global fontpkgheader4    %{expand:
Obsoletes: culmus-drugulin-clm-fonts < 0.133-1
Provides:  culmus-drugulin-clm-fonts = %{version}-%{release}

}
%global fonts4            DrugulinCLM-*.otf
%global fontconfs4        %{SOURCE4}
%global fontdescription4  %{expand:
%{common_description}

This package provides Drugulin CLM, a serif font family.
}

%global fontfamily5       Ellinia CLM
%global fontsummary5      Ellinia CLM, a sans-serif font family
%global fontpkgheader5    %{expand:
Obsoletes: culmus-ellinia-clm-fonts < 0.133-1
Provides:  culmus-ellinia-clm-fonts = %{version}-%{release}

}
%global fonts5            ElliniaCLM-*.otf
%global fontconfs5        %{SOURCE5}
%global fontdescription5  %{expand:
%{common_description}

This package provides Ellinia CLM, a sans-serif font family.
}

%global fontfamily6       Frank Ruehl CLM
%global fontsummary6      Frank Ruehl CLM, a serif font family
%global fontpkgheader6    %{expand:
Obsoletes: culmus-frank-ruehl-clm-fonts < 0.133-1
Provides:  culmus-frank-ruehl-clm-fonts = %{version}-%{release}
}
%global fonts6            FrankRuehlCLM-*.ttf
%global fontconfs6        %{SOURCE6}
%global fontdescription6  %{expand:
%{common_description}

This package provides Frank Ruehl CLM, a serif font family.
}

%global fontfamily7       Hadasim CLM
%global fontsummary7      Hadasim CLM, a serif font family
%global fontpkgheader7    %{expand:
Obsoletes: culmus-hadasim-clm-fonts < 0.133-1
Provides:  culmus-hadasim-clm-fonts = %{version}-%{release}
}
%global fonts7            HadasimCLM-*.ttf
%global fontconfs7        %{SOURCE7}
%global fontdescription7  %{expand:
%{common_description}

This package provides Hadasim CLM, a serif font family.
}

%global fontfamily8       Keter YG
%global fontsummary8      Keter YG, a sans-serif font family
%global fontpkgheader8    %{expand:
Obsoletes: culmus-keteryg-fonts < 0.133-1
Provides:  culmus-keteryg-fonts = %{version}-%{release}
}
%global fonts8            KeterYG-*.ttf
%global fontconfs8        %{SOURCE8}
%global fontdescription8  %{expand:
%{common_description}

This package provides Keter YG, a sans-serif font family.
}

%global fontfamily9       Miriam CLM
%global fontsummary9      Miriam CLM, a sans-serif font family
%global fontpkgheader9    %{expand:
Obsoletes: culmus-miriam-clm-fonts < 0.133-1
Provides:  culmus-miriam-clm-fonts = %{version}-%{release}
}
%global fonts9            MiriamCLM-*.ttf
%global fontconfs9        %{SOURCE9}
%global fontdescription9  %{expand:
%{common_description}

This package provides Miriam CLM, a sans-serif font family.
}

%global fontfamily10       Miriam Mono CLM
%global fontsummary10      Miriam Mono CLM, a monospace font family
%global fontpkgheader10    %{expand:
Obsoletes: culmus-miriam-mono-clm-fonts < 0.133-1
Provides:  culmus-miriam-mono-clm-fonts = %{version}-%{release}
}
%global fonts10            MiriamMonoCLM-*.ttf
%global fontconfs10        %{SOURCE10}
%global fontdescription10  %{expand:
%{common_description}

This package provides Miriam Mono CLM, a monospace font family.
}

%global fontfamily11       Nachlieli CLM
%global fontsummary11      Nachlieli CLM, a sans-serif font family
%global fontpkgheader11    %{expand:
Obsoletes: culmus-nachlieli-clm-fonts < 0.133-1
Provides:  culmus-nachlieli-clm-fonts = %{version}-%{release}
}
%global fonts11            NachlieliCLM-*.otf
%global fontconfs11        %{SOURCE11}
%global fontdescription11  %{expand:
%{common_description}

This package provides Nachlieli CLM, a sans-serif font family.
}

%global fontfamily12       Shofar
%global fontsummary12      Shofar, a serif font family
%global fontpkgheader12    %{expand:
Obsoletes: culmus-shofar-clm-fonts < 0.133-1
Provides:  culmus-shofar-clm-fonts = %{version}-%{release}
}
%global fonts12            Shofar*.ttf
%global fontconfs12        %{SOURCE12}
%global fontdescription12  %{expand:
%{common_description}

This package provides Shofar, a serif font family.
}

%global fontfamily13       Simple CLM
%global fontsummary13      Simple CLM, a sans-serif font family
%global fontpkgheader13    %{expand:
Obsoletes: culmus-simple-clm-fonts < 0.133-1
Provides:  culmus-simple-clm-fonts = %{version}-%{release}
}
%global fonts13            SimpleCLM-*.ttf
%global fontconfs13        %{SOURCE13}
%global fontdescription13  %{expand:
%{common_description}

This package provides Simple CLM, a sans-serif font family.
}

%global fontfamily14       Stam Ashkenaz CLM
%global fontsummary14      Stam Ashkenaz CLM, a serif font family
%global fontpkgheader14    %{expand:
Obsoletes: culmus-stamashkenaz-clm-fonts < 0.133-1
Provides:  culmus-stamashkenaz-clm-fonts = %{version}-%{release}
}
%global fonts14            StamAshkenazCLM.ttf
%global fontconfs14        %{SOURCE14}
%global fontdescription14  %{expand:
%{common_description}

This package provides Stam Ashkenaz CLM, a serif font family.
}

%global fontfamily15       Stam Sefarad CLM
%global fontsummary15      Stam Sefarad CLM, a serif font family
%global fontpkgheader15    %{expand:
Obsoletes: culmus-stamsefarad-clm-fonts < 0.133-1
Provides:  culmus-stamsefarad-clm-fonts = %{version}-%{release}
}
%global fonts15            StamSefaradCLM.ttf
%global fontconfs15        %{SOURCE15}
%global fontdescription15  %{expand:
%{common_description}

This package provides Stam Sefarad CLM, a serif font family.
}

%global fontfamily16       Yehuda CLM
%global fontsummary16      Yehuda CLM, a sans-serif font family
%global fontpkgheader16    %{expand:
Obsoletes: culmus-yehuda-clm-fonts < 0.133-1
Provides:  culmus-yehuda-clm-fonts = %{version}-%{release}
}
%global fonts16            YehudaCLM-*.otf
%global fontconfs16        %{SOURCE16}
%global fontdescription16  %{expand:
%{common_description}

This package provides Yehuda CLM, a sans-serif font family.
}
Source0:        http://downloads.sourceforge.net/culmus/culmus-%{version}.tar.gz
Source1:   66-%{fontpkgname1}.conf
Source2:   66-%{fontpkgname2}.conf
Source3:   65-%{fontpkgname3}.conf
Source4:   66-%{fontpkgname4}.conf
Source5:   66-%{fontpkgname5}.conf
Source6:   66-%{fontpkgname6}.conf
Source7:   66-%{fontpkgname7}.conf
Source8:   66-%{fontpkgname8}.conf
Source9:   66-%{fontpkgname9}.conf
Source10:  66-%{fontpkgname10}.conf
Source11:  66-%{fontpkgname11}.conf
Source12:  66-%{fontpkgname12}.conf
Source13:  66-%{fontpkgname13}.conf
Source14:  66-%{fontpkgname14}.conf
Source15:  66-%{fontpkgname15}.conf
Source16:  66-%{fontpkgname16}.conf
Source17:  modify-font-metadata.pe

Name:      culmus-fonts
Summary:   Fonts for Hebrew from Culmus project
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n culmus-%{version}
cp -p %{SOURCE17} .

%build
# As per fonts packaging guidelines we cannot install non-opentype fonts
# hence lets use makeotf tool to convert them to otf type format
makeotfexe -f AharoniCLM-BoldOblique.pfa -b
makeotfexe -f AharoniCLM-Bold.pfa -b
makeotfexe -f AharoniCLM-BookOblique.pfa
makeotfexe -f AharoniCLM-Book.pfa
makeotfexe -f CaladingsCLM.pfa
makeotfexe -f DrugulinCLM-BoldItalic.pfa -bi
makeotfexe -f DrugulinCLM-Bold.pfa -b
makeotfexe -f ElliniaCLM-BoldItalic.pfa -bi
makeotfexe -f ElliniaCLM-Bold.pfa -b
makeotfexe -f ElliniaCLM-LightItalic.pfa -i
makeotfexe -f ElliniaCLM-Light.pfa
makeotfexe -f YehudaCLM-Bold.pfa -b
makeotfexe -f YehudaCLM-Light.pfa

fontforge ./modify-font-metadata.pe

%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.133-16
- Import
