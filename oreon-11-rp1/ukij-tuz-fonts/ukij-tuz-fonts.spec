%global source0_hash none

# SPDX-License-Identifier: MIT

%global fontname ukij-tuz

Version: 3.10
Release: 29%{?dist}
URL:     http://www.ukij.org/fonts/

%global foundry           UKIJ
%global fontlicense       OFL-1.1

%global fontfamily        UKIJ Tuz
%global fontsummary       Uyghur Computer Science Association (UKIJ) Unicode fonts
%global fonts             *.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Uyghur Computer Science Association (UKIJ) Unicode fonts
}

Source0:  http://www.ukij.org/fonts/fonts/UKIJTuz.ttf
Source10: 66-%{fontpkgname}.conf

%fontpkg

%prep
%setup -c -T
cp -p %{SOURCE0} .

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
%autochangelog
