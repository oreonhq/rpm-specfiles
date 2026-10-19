%global source0_hash e5f78133e5b529b81f6563cb6d96f39ee978e8a1cb942107f78a31fca0ddcc72
%global pkg_name yesod-form
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        1.7.11
Release:        1%{?dist}
Summary:        Form handling support for Yesod Web Framework
License:        MIT
URL:            https://hackage.haskell.org/package/yesod-form
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-blaze-markup-prof
BuildRequires:  ghc-byteable-devel
BuildRequires:  ghc-byteable-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-email-validate-devel
BuildRequires:  ghc-email-validate-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-persistent-devel
BuildRequires:  ghc-persistent-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-shakespeare-devel
BuildRequires:  ghc-shakespeare-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-xss-sanitize-devel
BuildRequires:  ghc-xss-sanitize-prof
BuildRequires:  ghc-yesod-core-devel
BuildRequires:  ghc-yesod-core-prof
BuildRequires:  ghc-yesod-persistent-devel
BuildRequires:  ghc-yesod-persistent-prof
# /oreon:deps
%description
Form handling for Yesod, in the same style as formlets.
See the forms chapter of the Yesod book.

This package provides a set of basic form inputs such as text, number, time,
checkbox, select, textarea, and etc. via Yesod.Form.Fields module.

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
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-yesod-form-devel -f %{oreon_filedir}/ghc-yesod-form-devel.list
%files -n ghc-yesod-form-doc -f %{oreon_filedir}/ghc-yesod-form-doc.list
%files -n ghc-yesod-form-prof -f %{oreon_filedir}/ghc-yesod-form-prof.list

%changelog

%autochangelog
