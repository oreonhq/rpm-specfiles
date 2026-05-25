# SPDX-License-Identifier: MIT

BuildArch: noarch
BuildRequires: bdftopcf fonttosfnt
BuildRequires: make

%global fontname bitmap
%global fontconf 66-%{fontname}

Version: 0.3
Release: 54%{?dist}
License: GPL-2.0-only AND MIT AND LicenseRef-Lucida

%global foundry           Bitmap

%global common_description %{expand:
The bitmap-fonts package provides a number of bitmap fonts selected\
from the xorg package designed for use locations such as\
terminals.
}

%global fontfamily1       Lucida Typewriter
%global fontsummary1      Selected CJK bitmap fonts for Anaconda
%global fontlicense1      LicenseRef-Lucida
%global fontlicenses1     LU_LEGALNOTICE
%global fontpkgheader1    %{expand:
Provides: %{name}-cjk = %{version}-%{release}
Conflicts: bitmap-lucida-typewriter-opentype-fonts
}
%global fonts1            lut*.pcf.gz
%global fontconfs1        %{SOURCE17}
%global fontdescription1  %{expand:
%{common_description}
}

%global fontfamily2       Lucida Typewriter OpenType
%global fontsummary2      Selected CJK bitmap fonts for Anaconda (OpenType version)
%global fontlicense2      LicenseRef-Lucida
%global fontlicenses2     LU_LEGALNOTICE
%global fontpkgheader2    %{expand:
Conflicts: bitmap-lucida-typewriter-fonts
}
%global fonts2            lut*.otb
%global fontconfs2        %{SOURCE18}
%global fontdescription2  %{expand:
%{common_description}
}

%global fontfamily3       Fangsongti
%global fontsummary3      Selected CJK bitmap fonts for Anaconda
%global fontlicense3      MIT
%global fontlicenses3     LICENSE
%global fontpkgheader3    %{expand:
Provides: %{name}-cjk = %{version}-%{release}
Conflicts: bitmap-fangsongti-opentype-fonts
}
%global fonts3            fangsongti*.pcf.gz
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}
}

%global fontfamily4       Fangsongti OpenType
%global fontsummary4      Selected CJK bitmap fonts for Anaconda (OpenType version)
%global fontlicense4      MIT
%global fontlicenses4     LICENSE
%global fontpkgheader4    %{expand:
Conflicts: bitmap-fangsongti-fonts
}
%global fonts4            fangsongti*.otb
%global fontconfs4        %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}
}

%global fontfamily5       Console
%global fontsummary5      Selected set of bitmap fonts
%global fontlicense5      GPL-2.0-only
%global fontlicenses5     COPYING
%global fontpkgheader5    %{expand:
Conflicts: bitmap-console-opentype-fonts
}
%global fonts5            fixfont-3.5/console8x16*.pcf.gz
%global fontconfs5        %{SOURCE11}
%global fontdescription5  %{expand:
%{common_description}
}

%global fontfamily6       Console OpenType
%global fontsummary6      Selected set of bitmap fonts (OpenType version)
%global fontlicense6      GPL-2.0-only
%global fontlicenses6     COPYING
%global fontpkgheader6    %{expand:
Conflicts: bitmap-console-fonts
}
%global fonts6            fixfont-3.5/console8x16*.otb
%global fontconfs6        %{SOURCE12}
%global fontdescription6  %{expand:
%{common_description}
}

%global fontfamily7       Fixed
%global fontsummary7      Selected set of bitmap fonts
%global fontlicense7      GPL-2.0-only
%global fontlicenses7     COPYING
%global fontpkgheader7    %{expand:
Conflicts: bitmap-fixed-opentype-fonts
}
%global fonts7            fixfont-3.5/console9*.pcf.gz
%global fontconfs7        %{SOURCE15}
%global fontdescription7  %{expand:
%{common_description}
}

%global fontfamily8       Fixed OpenType
%global fontsummary8      Selected set of bitmap fonts (OpenType version)
%global fontlicense8      GPL-2.0-only
%global fontlicenses8     COPYING
%global fontpkgheader8    %{expand:
Conflicts: bitmap-fixed-fonts
}
%global fonts8            fixfont-3.5/console9*.otb
%global fontconfs8        %{SOURCE16}
%global fontdescription8  %{expand:
%{common_description}
}


Source0:  bitmap-fonts-%{version}.tar.bz2
Source1:  fixfont-3.5.tar.bz2
Source2:  LICENSE
Source3:  COPYING
Source11: 66-bitmap-console.conf
Source12: 66-bitmap-console-opentype.conf
Source13: 66-bitmap-fangsongti.conf
Source14: 66-bitmap-fangsongti-opentype.conf
Source15: 66-bitmap-fixed.conf
Source16: 66-bitmap-fixed-opentype.conf
Source17: 66-bitmap-lucida-typewriter.conf
Source18: 66-bitmap-lucida-typewriter-opentype.conf

Name:     bitmap-fonts
Summary:  Selected set of bitmap fonts
%description
%wordwrap -v common_description

%package -n %{fontname}-fonts-all
Summary: Compatibility files of bitmap-font families
Provides: bitmap-fonts = %{version}-%{release}
Obsoletes: bitmap-fonts < %{version}-%{release}
Provides: bitmap-fonts-compat = %{version}-%{release}
Obsoletes: bitmap-fonts-compat < %{version}-%{release}
Requires: %{fontname}-lucida-typewriter-fonts = %{version}-%{release}
Requires: %{fontname}-fangsongti-fonts = %{version}-%{release}
Requires: %{fontname}-console-fonts = %{version}-%{release}
Requires: %{fontname}-fixed-fonts = %{version}-%{release}
Requires: ucs-miscfixed-fonts
Conflicts: %{fontname}-opentype-fonts-all

%description -n %{fontname}-fonts-all %common_description
Meta-package for installing all font families of bitmap.

%files -n %{fontname}-fonts-all

%package -n %{fontname}-opentype-fonts-all
Summary:  Compatibility files of bitmap-font families (opentype version)
Provides: bitmap-opentype-fonts-compat = %{version}-%{release}
Obsoletes: bitmap-opentype-fonts-compat < %{version}-%{release}
Requires: %{fontname}-lucida-typewriter-opentype-fonts = %{version}-%{release}
Requires: %{fontname}-fangsongti-opentype-fonts = %{version}-%{release}
Requires: %{fontname}-console-opentype-fonts = %{version}-%{release}
Requires: %{fontname}-fixed-opentype-fonts = %{version}-%{release}
Requires: ucs-miscfixed-opentype-fonts
Conflicts: %{fontname}-fonts-all

%description -n %{fontname}-opentype-fonts-all %common_description
Meta-package for installing all font families of opentype bitmap.

%files -n %{fontname}-opentype-fonts-all


%fontpkg -a

%prep
%setup -q -a 1
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .


%build
make all

make -C fixfont-3.5 all

# Convert to OpenType Bitmap Font
# rm [0-9]*.bdf fixfont-3.5/[0-9]*.bdf

for bdf in `ls *.bdf`;
do fonttosfnt -b -c -g 2 -m 2 -o ${bdf%%bdf}otb  $bdf;
done

pushd fixfont-3.5
for bdf in `ls *.bdf`;
do fonttosfnt -b -c -g 2 -m 2 -o ${bdf%%bdf}otb  $bdf;
done
# For console9x15.otb
fonttosfnt -b -c -g 2 -m 2 -o console9x15.otb console9x15.pcf
popd

gzip *.pcf fixfont-3.5/*.pcf

%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3-54
- Import
