%global source0_hash none
%global forgeurl    https://github.com/alexeiva/Raleway
%global commit      98add575720aa077b7d253477e26c463a55e71da
%forgemeta
Version: 4.025
Release:        18%{?dist}
URL:     %{forgeurl}
%global foundry           Impallari
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt *.md
%global fontdocsex        %{fontlicenses}
%global fontfamily        Raleway
%global fontsummary       Raleway, an elegant sans-serif font family
%global fonts             fonts/TTF/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Raleway is an elegant sans-serif font family intended for headings and other
large size usage.
It features both old style and lining numerals, standard and discretionary
ligatures, a pretty complete set of diacritics, as well as a stylistic
alternate inspired by more geometric sans-serif typefaces than its
neo-grotesque inspired default character set.}
Source0:        %{forgeurl}/archive/%{commit}/%{fontfamily}-%{commit}.tar.gz
Source10: 58-%{fontpkgname}.xml
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%package doc
Summary:   Optional documentation files of %{fontpkgname}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{fontpkgname}.

%prep

%forgesetup
%linuxtext %{fontdocs} %{fontlicenses}

%build

%fontbuild
%install
%fontinstall
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck
%fontfiles
%files -f %{oreon_filedir}/main.list
%files -n adf-gillius-fonts-doc -f %{oreon_filedir}/adf-gillius-fonts-doc.list

%changelog

%autochangelog
