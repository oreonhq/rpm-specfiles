%global source0_hash none

# SPDX-License-Identifier: MIT

%global fontname un-core
%global alphatag 080608
%global archivename un-fonts-core-%{version}-%{alphatag}

BuildArch: noarch

Version: 1.0.2
Release: 0.50.%{alphatag}%{?dist}
License: GPL-2.0-only
URL:     http://kldp.net/projects/unfonts/

%global foundry           Un
%global fontlicenses      COPYING
%global fontdocs          README

%global common_description %{expand:
The UN set of Korean TrueType fonts is derived from the HLaTeX Type1 fonts \
made by Koaunghi Un in 1998. They were converted to TrueType with \
FontForge(PfaEdit) by Won-kyu Park in 2003. \
The Un Core set is composed of: \
\
- UnBatang: serif \
- UnDinaru: fantasy \
- UnDotum: sans-serif \
- UnGraphic: sans-serif style \
- UnGungseo: cursive, brush-stroke \
- UnPilgi: script
}

%global fontfamily1       Un Core Batang
%global fontsummary1      Un Core fonts - UnBatang
%global fonts1            UnBatang.ttf UnBatangBold.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

This package includes UnBatang, a serif font.
}

%global fontfamily2       Un Core Dinaru
%global fontsummary2      Un Core fonts - UnDinaru
%global fonts2            UnDinaru.ttf UnDinaruLight.ttf UnDinaruBold.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

This package includes UnDinaru, a fantasy font.
}

%global fontfamily3       Un Core Dotum
%global fontsummary3      Un Core fonts - UnDotum
%global fontpkgheader3    %{expand:
Obsoletes:       %{name}-common < 1.0.2-0.43.080608
Provides:        %{name}-common = %{version}-%{release}
}
%global fonts3            UnDotum.ttf UnDotumBold.ttf
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

This package includes UnDotum, a sans-serif font.
}

%global fontfamily4       Un Core Graphic
%global fontsummary4      Un Core fonts - UnGraphic
%global fonts4            UnGraphic.ttf UnGraphicBold.ttf
%global fontconfs4        %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}

This package includes UnGraphic, a sans-serif font.
}

%global fontfamily5       Un Core Gungseo
%global fontsummary5      Un Core fonts - UnGungseo
%global fonts5            UnGungseo.ttf
%global fontconfs5        %{SOURCE15}
%global fontdescription5  %{expand:
%{common_description}

This package includes UnGungseo, a cursive font.
}

%global fontfamily6       Un Core Pilgi
%global fontsummary6      Un Core fonts - UnPilgi
%global fonts6            UnPilgi.ttf UnPilgiBold.ttf
%global fontconfs6        %{SOURCE16}
%global fontdescription6  %{expand:
%{common_description}

This package includes UnPilgi, a script font.
}

Source0:  http://kldp.net/frs/download.php/4695/%{archivename}.tar.gz
Source11: 67-un-core-batang-fonts.conf
Source12: 67-un-core-dinaru-fonts.conf
Source13: 67-un-core-dotum-fonts.conf
Source14: 67-un-core-graphic-fonts.conf
Source15: 67-un-core-gungseo-fonts.conf
Source16: 67-un-core-pilgi-fonts.conf

Name:     %{fontname}-fonts
Summary:  Un Core family of Korean TrueType fonts
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep
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
