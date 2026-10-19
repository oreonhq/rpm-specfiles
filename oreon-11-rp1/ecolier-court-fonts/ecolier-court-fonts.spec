%global source0_hash none
Version: 20070702
Release:        50%{?dist}
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
Source0:        lisez_moi.txt
Source1:  README-Fedora.txt
Source10: ec_cour.ttf
Source11: ecl_cour.ttf
Source20: 61-%{fontpkgname0}.xml
Source21: 61-%{fontpkgname1}.xml
%fontpkg -a
%fontmetapkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%prep

%setup -q -c -T
install -m 0644 -p %{SOURCE0} %{SOURCE1} .
%linuxtext *.txt

%build

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
