%global source0_hash 49c789c21305bed13d90d7500877b50d62db1e8e4d6f7715178e556319ddbda9

%global projectname       scheherazade
BuildArch: noarch

Version:    4.500
Release:    1%{?dist}
URL:        https://software.sil.org/%{projectname}/

%global foundry           SIL
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          FONTLOG.txt README.txt OFL-FAQ.txt documentation/*
%global fontdocsex        %{fontlicenses}

%global fontfamily1        Scheherazade New
%global fontsummary1       An Arabic script unicode font
%global fontpkgheader1    %{expand:
Provides: sil-scheherazade-fonts = %{version}-%{release}
Obsoletes: sil-scheherazade-fonts < %{version}-%{release}
}
%global fonts1             *.ttf
%global fontconfs1         %{SOURCE1}
%global fontdescription1   %{expand:
Scheherazade, named after the heroine of the classic Arabian Nights tale, is
designed in a similar style to traditional typefaces such as Monotype Naskh,
extended to cover the full Unicode Arabic repertoire.
}

Source0:        https://software.sil.org/downloads/r/scheherazade/ScheherazadeNew-%{version}.zip
Source1:    65-sil-scheherazade-new-fonts.conf

Name:       sil-scheherazade-fonts
Summary:    An Arabic script unicode font 
License:    OFL-1.1

%description
%wordwrap -v common_description

%fontpkg -a

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n ScheherazadeNew-%{version}
rm -rf documentation/source documentation/pdf
%linuxtext FONTLOG.txt OFL.txt OFL-FAQ.txt README.txt documentation/DOCUMENTATION.txt documentation/assets/css/*

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Fri Sep 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.500-1
- Update to 4.500

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.300-8
- Import
