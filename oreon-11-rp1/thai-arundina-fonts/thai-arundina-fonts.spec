%global source0_hash 4aa7c07b8174a08fd58c930552d3404edfebc2e0ac2b0420853e6a7471586719

# SPDX-License-Identifier: MIT

%global archivename fonts-sipa-arundina-%{version}

BuildArch: noarch
BuildRequires: fontforge make

Version: 0.2.2
Release: 19%{?dist}
License: Bitstream-Vera
URL:     http://linux.thai.net/projects/fonts-sipa-arundina

%global foundry           Thai
%global fontlicenses      COPYING
%global fontdocs          README AUTHORS NEWS

%global common_description %{expand:
Arundina fonts were created aiming at Bitstream Vera / Dejavu \
compatibility, under SIPA's initiation.  They were then further \
modified by TLWG for certain aspects, such as Latin glyph size \
compatibility and OpenType conformance.
}

%global fontfamily1       Arundina Sans
%global fontsummary1      Variable-width sans-serif Thai Arundina fonts
%global fontpkgheader1    %{expand:
Obsoletes:       %{name}-common < 0.2.2-13
Provides:        %{name}-common = %{version}-%{release}
}
%global fonts1            arundina/ArundinaSans.ttf arundina/ArundinaSans-Bold.ttf arundina/ArundinaSans-Oblique.ttf arundina/ArundinaSans-BoldOblique.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

This package consists of the Thai Arundina sans-serif variable-width
font faces.
}

%global fontfamily2       Arundina Serif
%global fontsummary2      Variable-width serif Thai Arundina fonts
%global fontpkgheader2    %{expand:
Obsoletes:       %{name}-common < 0.2.2-13
Provides:        %{name}-common = %{version}-%{release}
}
%global fonts2            arundina/ArundinaSerif.ttf arundina/ArundinaSerif-Bold.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

This package consists of the Thai Arundina serif variable-width
font faces.
}

%global fontfamily3       Arundina Sans Mono
%global fontsummary3      Monospace sans-serif Thai Arundina fonts
%global fontpkgheader3    %{expand:
Obsoletes:       %{name}-common < 0.2.2-13
Provides:        %{name}-common = %{version}-%{release}
}
%global fonts3            arundina/ArundinaSansMono.ttf arundina/ArundinaSansMono-Bold.ttf arundina/ArundinaSansMono-Oblique.ttf arundina/ArundinaSansMono-BoldOblique.ttf
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

This package consists of the Thai Arundina sans-serif monospace font
faces.
}

Source0:  http://linux.thai.net/pub/thailinux/software/fonts-sipa-arundina/%{archivename}.tar.xz
Source11: 67-thai-arundina-sans-fonts.conf
Source12: 67-thai-arundina-serif-fonts.conf
Source13: 67-thai-arundina-sans-mono-fonts.conf

Name:     thai-arundina-fonts
Summary:  Thai Arundina fonts
%description
%wordwrap -v common_description

%fontpkg -a

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}
%linuxtext %{fontdocs}

%build
%configure
make
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
