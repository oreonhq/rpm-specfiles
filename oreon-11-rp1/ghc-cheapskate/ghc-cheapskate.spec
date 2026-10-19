%global source1_hash b8ae3cbb826610ea45e6840b7fde0af2c2ea6690cb311edfe9683f61c0a50d96
%global source0_hash ed374897c39391fcf760552e6468def39fe36c3185708ca83056660ca3a2c69e
%global pkg_name cheapskate
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.1.1.2
Release:        1%{?dist}
Summary:        Experimental markdown processor
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/cheapskate
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
Patch0:         cheapskate-mtl-2.3.patch
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-syb-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-uniplate-devel
BuildRequires:  ghc-uniplate-prof
BuildRequires:  ghc-xss-sanitize-devel
BuildRequires:  ghc-xss-sanitize-prof
# /oreon:deps
%description
This is an experimental Markdown processor in pure Haskell. It aims to process
Markdown efficiently and in the most forgiving possible way. It is designed to
deal with any input, including garbage, with linear performance.
Output is sanitized by default for protection against XSS attacks.

Several markdown extensions are implemented, including fenced code blocks,
significant list start numbers, and autolinked URLs. See README.markdown for
details.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development files.

%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem
%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif

%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)
%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
cp -bp %{SOURCE1} %{pkg_name}.cabal
%autopatch -p1
# End cabal-rpm setup
cabal-tweak-dep-ver containers '<0.7' '<0.8'
cabal-tweak-dep-ver data-default '< 0.8' '< 0.9'
cabal-tweak-dep-ver mtl '<2.3' '<2.4'
cabal-tweak-dep-ver text '1.3' '2.2'

%build

%ghc_lib_build
%install
%ghc_lib_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 -p -t %{buildroot}%{_mandir}/man1/ ./man/man1/cheapskate.1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-cheapskate-devel -f %{oreon_filedir}/ghc-cheapskate-devel.list
%files -n ghc-cheapskate-doc -f %{oreon_filedir}/ghc-cheapskate-doc.list
%files -n ghc-cheapskate-prof -f %{oreon_filedir}/ghc-cheapskate-prof.list

%changelog

%autochangelog
