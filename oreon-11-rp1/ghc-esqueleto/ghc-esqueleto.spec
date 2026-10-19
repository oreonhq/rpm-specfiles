%global source1_hash 508f2600353722fa043b69066102d7b2fa526f04769981c5a5a0cdc0173f6082
%global source0_hash 45cacb39f91c4f8842e1e778ffb02fbd3c551438558cf540654a9a48ab4a027e
%global pkg_name esqueleto
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        3.6.0.3
Release:        1%{?dist}
Summary:        Type-safe EDSL for SQL queries on persistent backends
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/esqueleto
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-monad-logger-prof
BuildRequires:  ghc-persistent-devel
BuildRequires:  ghc-persistent-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-unliftio-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
# /oreon:deps
%description
'esqueleto' is a bare bones, type-safe EDSL for SQL queries that works with
unmodified 'persistent' SQL backends. Its language closely resembles SQL, so
you don't have to learn new concepts, just new syntax, and it's fairly easy to
predict the generated SQL and optimize it for your backend. Most kinds of
errors committed when writing SQL are caught as compile-time errors---although
it is possible to write type-checked 'esqueleto' queries that fail at runtime.

'persistent' is a library for type-safe data serialization. It has many kinds
of backends, such as SQL backends ('persistent-mysql', 'persistent-postgresql',
'persistent-sqlite') and NoSQL backends ('persistent-mongoDB'). While
'persistent' is a nice library for storing and retrieving records, including
with filters, it does not try to support some of the features that are specific
to SQL backends. In particular, 'esqueleto' is the recommended library for
type-safe 'JOIN's on 'persistent' SQL backends. (The alternative is using raw
SQL, but that's error prone and does not offer any composability.)

Currently, 'SELECT's, 'UPDATE's, 'INSERT's and 'DELETE's are supported.
Not all SQL features are available, but most of them can be easily added
(especially functions), so please open an issue or send a pull request if you
need anything that is not covered by 'esqueleto' on
<https://github.com/bitemyapp/esqueleto>.

The name of this library means "skeleton" in Portuguese and contains all three
SQL letters in the correct order =). It was inspired by Scala's Squeryl but
created from scratch.

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
dos2unix -k -n %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-esqueleto-devel -f %{oreon_filedir}/ghc-esqueleto-devel.list
%files -n ghc-esqueleto-doc -f %{oreon_filedir}/ghc-esqueleto-doc.list
%files -n ghc-esqueleto-prof -f %{oreon_filedir}/ghc-esqueleto-prof.list

%changelog

%autochangelog
