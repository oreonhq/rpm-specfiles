%global source0_hash none

# SPDX-License-Identifier: MIT

Name:    ibm-plex-fonts
Version: 6.4.0
Release: 5%{?dist}
Summary: IBM Plex, the new IBM set of coordinated grotesque corporate fonts

License: OFL-1.1
URL:     https://www.ibm.com/plex/

BuildArch: noarch

%global foundry           IBM
%global fontlicense       OFL
%global fontlicenses      IBM-Plex-Sans/license.txt
#global fontdocs          *.md

%global common_description %{expand:
IBM wanted Plex to be a distinctive, yet timeless workhorse — an alternative to
its previous corporate font family, “Helvetica Neue”, for this new era. The
Grotesque style was the perfect fit. Not only do Grotesque font families
balance human and rational elements, the Grotesque style also came about during
the Industrial Age, when IBM was born.
}

%global fontfamily1       Plex Sans
%global fontsummary1      IBM Plex Sans
%global fonts1            IBM-Plex-Sans/*.otf IBM-Plex-Sans-Condensed/*.otf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}
This package provides IBM Plex Sans.}

%global fontfamily2       Plex Serif
%global fontsummary2      IBM Plex Serif
%global fonts2            IBM-Plex-Serif/*.otf
%global fontconfngs2      %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}
This package provides IBM Plex Serif.}

%global fontfamily3       Plex Mono
%global fontsummary3      IBM Plex Mono
%global fonts3            IBM-Plex-Mono/*.otf
%global fontconfngs3      %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}
This package provides IBM Plex Mono.}

%global fontfamily4       Plex Sans Arabic
%global fontsummary4      IBM Plex Sans Arabic
%global fonts4            IBM-Plex-Sans-Arabic/*.otf
%global fontconfngs4      %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}
This package provides IBM Plex Sans Arabic.}

%global fontfamily5       Plex Sans Devanagari
%global fontsummary5      IBM Plex Sans Devanagari
%global fonts5            IBM-Plex-Sans-Devanagari/*.otf
%global fontconfngs5      %{SOURCE15}
%global fontdescription5  %{expand:
%{common_description}
This package provides IBM Plex Sans Devanagari.}

%global fontfamily6       Plex Sans Hebrew
%global fontsummary6      IBM Plex Sans Hebrew
%global fonts6            IBM-Plex-Sans-Hebrew/*.otf
%global fontconfngs6      %{SOURCE16}
%global fontdescription6  %{expand:
%{common_description}
This package provides IBM Plex Sans Hebrew.}

%global fontfamily7       Plex Sans Thai
%global fontsummary7      IBM Plex Sans Thai
%global fonts7            IBM-Plex-Sans-Thai/*.otf
%global fontconfngs7      %{SOURCE17}
%global fontdescription7  %{expand:
%{common_description}
This package provides IBM Plex Sans Thai.}

%global fontfamily8       Plex Sans Thai Looped
%global fontsummary8      IBM Plex Sans Thai Looped, a formal variant of IBM Plex Sans for Thai
%global fonts8            IBM-Plex-Sans-Thai-Looped/*.otf
%global fontconfngs8      %{SOURCE18}
%global fontdescription8  %{expand:
%{common_description}
This package provides IBM Plex Sans Thai Looped.}

Source0:  https://github.com/IBM/plex/releases/download/v%{version}/OpenType.zip#/%{name}-%{version}.zip
Source11: 58-%{fontpkgname1}.xml
Source12: 58-%{fontpkgname2}.xml
Source13: 58-%{fontpkgname3}.xml
Source14: 59-%{fontpkgname4}.xml
Source15: 59-%{fontpkgname5}.xml
Source16: 59-%{fontpkgname6}.xml
Source17: 59-%{fontpkgname7}.xml
Source18: 59-%{fontpkgname8}.xml

%description
%{common_description}

%fontpkg -a

%fontmetapkg

%prep
%setup -n OpenType

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
