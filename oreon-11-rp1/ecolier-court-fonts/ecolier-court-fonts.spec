%global source0_hash none

# SPDX-License-Identifier: MIT
Version: 20070702
Release: 50%{?dist}
# This used to be published here, copies are all over the web now
#URL:     http://perso.orange.fr/jm.douteau/page_ecolier.htm

%global fontlicense       OFL-1.1
%global fontlicenses      lisez_moi.txt
%global fontdocs          README-Fedora.txt

%global common_description %{expand:
The Écolier court font families were created by Jean-Marie Douteau to mimic the
traditional cursive writing French children are taught in school.

He kindly released two of them under the OFL, which are redistributed in this
package.}

%global fontfamily0       Ecolier Court
%global fontsummary0      Écolier Court, a schoolchildren cursive Latin font family
%global fontpkgheader0    %{expand:
Obsoletes: ecolier-court-fonts-common < %{version}-%{release}
}
%global fonts0            %{SOURCE10}
%global fontconfngs0      %{SOURCE20}
%global fontdescription0  %{expand:
%{common_description}}

%global fontfamily1       Ecolier Lignes Court
%global fontsummary1      Écolier Lignes Court, a schoolchildren cursive Latin font family with lines
%global fontpkgheader1    %{expand:
Obsoletes: ecolier-court-lignes-fonts < %{version}-%{release}
}
%global fonts1            %{SOURCE11}
%global fontconfngs1      %{SOURCE21}

%global fontdescription1  %{expand:
%{common_description}

The « lignes » (lines) Écolier Court font variant includes the Seyes lining
commonly used on schoolchildren notepads.}

Source0:  lisez_moi.txt
Source1:  README-Fedora.txt
Source10: ec_cour.ttf
Source11: ecl_cour.ttf
Source20: 61-%{fontpkgname0}.xml
Source21: 61-%{fontpkgname1}.xml

%fontpkg -a

%fontmetapkg

%prep
%setup -q -c -T
install -m 0644 -p %{SOURCE0} %{SOURCE1} .
%linuxtext *.txt

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
%autochangelog
