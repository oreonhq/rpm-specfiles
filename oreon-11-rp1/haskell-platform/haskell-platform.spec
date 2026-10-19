%global source0_hash none
Name:           haskell-platform
Version:        2024.1
Release:        1%{?dist}
Summary:        Standard Haskell distribution
License:        BSD-3-Clause
URL:            https://www.haskell.org/
Requires:       ghc
Requires:       alex
Requires:       cabal-install
Requires:       happy
Requires:       hscolour
Requires:       stack
# oreon:deps
BuildRequires:  alex
BuildRequires:  cabal-install
BuildRequires:  ghc
BuildRequires:  happy
BuildRequires:  hscolour
BuildRequires:  stack
# /oreon:deps
%description
Haskell Platform is a set of stable and well used Haskell tools.
It provides a good starting environment for Haskell development.

%prep

%build

%install

%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
