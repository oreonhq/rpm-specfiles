%global source0_hash db5b27df7bbb318036ebdb75acd3e98f1bd6eb6608fb70a67d478cd243d178dc
Version: 1.10
Release:        56%{?dist}
License: Bitstream-Vera
URL:     http://www.gnome.org/fonts/
BuildArch: noarch
%global source_name       bitstream-vera-fonts
%global foundry           Bitstream
%global fontlicenses      COPYRIGHT.TXT
%global fontdocs          *.TXT
%global fontdocsex        %{fontlicenses}
%global common_description %{expand:
The Vera font families are high-quality Latin typefaces donated by Bitstream.}
%global fontfamily1       Vera Sans
%global fontsummary1      Bitstream Vera Sans, a variable-width sans-serif font family
%global fontpkgheader1    %{expand:
Obsoletes: bitstream-vera-fonts-common < %{version}-%{release}
Suggests: font(dejavusans)
}
%global fonts1            *.ttf
%global fontconfngs1      %{SOURCE11}
%global fontsex1          %{fonts2} %{fonts3}
%global fontdescription1 %{expand:
%{common_description}
This package consists of the Bitstream Vera Sans sans-serif variable-width
font family.}
%global fontfamily2       Vera Serif
%global fontsummary2      Bitstream Vera Serif, a variable-width serif font family
%global fontpkgheader2    %{expand:
Suggests: font(dejavuserif)
}
%global fonts2            VeraSe*ttf
%global fontconfngs2      %{SOURCE12}
%global fontdescription2 %{expand:
%{common_description}
This package consists of the Bitstream Vera Serif serif variable-width font
family.}
%global fontfamily3       Vera Sans Mono
%global fontsummary3      Bitstream Vera Sans Mono, a mono-space sans-serif font family
%global fontpkgheader3    %{expand:
Suggests: font(dejavusansmono)
}
%global fonts3            VeraMo*ttf
%global fontconfngs3      %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}
This package consists of the Bitstream Vera Sans Mono mono-space sans-serif font
family.}
%global archivename ttf-bitstream-vera
Source0:        ftp://ftp.gnome.org/pub/GNOME/sources/%{archivename}/%{version}/%{archivename}-%{version}.tar.bz2
Source11: 55-%{fontpkgname1}.xml
Source12: 55-%{fontpkgname2}.xml
Source13: 55-%{fontpkgname3}.xml
Name:     bitstream-vera-fonts
Summary:        The Bitstream Vera font families
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}-%{version}

%build

%fontbuild -a
%install
%fontinstall -a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck -a
%fontfiles -a
%files -f %{oreon_filedir}/main.list
%files -n bitstream-vera-sans-fonts -f %{oreon_filedir}/bitstream-vera-sans-fonts.list
%files -n bitstream-vera-serif-fonts -f %{oreon_filedir}/bitstream-vera-serif-fonts.list
%files -n bitstream-vera-sans-mono-fonts -f %{oreon_filedir}/bitstream-vera-sans-mono-fonts.list
%files -n bitstream-vera-fonts-all -f %{oreon_filedir}/bitstream-vera-fonts-all.list

%changelog

%autochangelog
