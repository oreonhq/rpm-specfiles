%global source1_hash 7afc88133bd244e4a8fc483363a849bdb91e1b8587508e3524baae84e4ec32b8
%global source0_hash 390632cffc561c32483af474aac50168a68f0fa382096552e37749923617884c
Name:           c2hs
Version:        0.28.8
Release:        1%{?dist}
Summary:        C to Haskell FFI tool that gives some cross-language type safety
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://hackage.haskell.org/package/c2hs
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}.cabal#/%{name}-%{version}.cabal
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-language-c-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
C->Haskell assists in the development of Haskell bindings to C libraries.
It extracts interface information from C header files and generates Haskell
code with foreign imports and marshaling. Unlike writing foreign imports by
hand (or using hsc2hs), this ensures that C functions are imported with the
correct Haskell types.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q
dos2unix -k -n %{SOURCE1} %{name}.cabal
# End cabal-rpm setup

%build

%ghc_bin_build
%install
%ghc_bin_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
