%global projectname       scheherazade
BuildArch: noarch

Version:    3.300
Release:    8%{?dist}
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

Source0:    https://software.sil.org/downloads/r/scheherazade/ScheherazadeNew-%{version}.zip
Source1:    65-%{fontpkgname1}.conf

Name:       sil-scheherazade-fonts
Summary:    An Arabic script unicode font 
License:    OFL-1.1

%description
%wordwrap -v common_description

%fontpkg -a

%prep
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.300-8
- Import
