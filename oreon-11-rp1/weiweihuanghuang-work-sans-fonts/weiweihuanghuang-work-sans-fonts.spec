%global source0_hash none
%global forgeurl    https://github.com/weiweihuanghuang/Work-Sans
%global commit      dcd044c29b6f92f101a94777f744fa0f051da14b
%forgemeta
Version: 2.07
Release:        23%{?dist}
URL:     %{forgeurl}
%global foundry           weiweihuanghuang
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}
%global fontfamily        Work Sans
%global fontsummary       Work Sans, a font family in the early grotesque style
%global fonts             fonts/variable/*ttf fonts/static/OTF/*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Work Sans is a font family based loosely on early Grotesques — i.e. Stephenson
Blake, Miller & Richard and Bauersche Gießerei. The core of the fonts are
optimized for on-screen medium-sized text usage,  but can still be used in
print. The fonts at the extreme weights are designed more for display use.
Overall, features are simplified and optimized for screen resolutions – for
example, diacritic marks are larger than how they would be in print.}
Source0:        %{forgeurl}/archive/%{commit}/Work-Sans-%{commit}.tar.gz
Source10: 58-%{fontpkgname}.xml
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep

%forgesetup
chmod 644 %{fontdocs} %{fontlicenses}

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
