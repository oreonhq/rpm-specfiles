%global source0_hash 98c699b6e47b257dff85d49d59e39858462598008e074460c8bfacaa3e2a43ba
%global pkg_name double-conversion
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        2.0.5.0
Release:        1%{?dist}
Summary:        Fast conversion between single and double precision floating point and text
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/double-conversion
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Patch0:         use-system-lib.diff
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  double-conversion-devel
BuildRequires:  gcc-c++
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
# /oreon:deps
%description
A library that performs fast, accurate conversion between floating point and
text.

This library is implemented as bindings to the C++ 'double-conversion' library
written by Florian Loitsch at Google:
<https://github.com/floitsch/double-conversion>.

Now it can convert single precision numbers, and also it can create Builder,
instead of bytestring or text.

The 'Text' versions of these functions are about 30 times faster than the
default 'show' implementation for the 'Double' type.

The 'ByteString' versions are have very close speed to the 'Text' versions;

Builder versions (both for Text and Bytestring) are slower on single value, but
they are much faster on large number of values (up to 20x faster on list with
20000 doubles).

As a final note, be aware that the 'bytestring-show' package is about 50%
slower than simply using 'show'.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       double-conversion-devel%{?_isa}
Requires:       gcc-c++
%description devel
This package provides the Haskell %{pkg_name} library development
files.

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
%autopatch -p1
# End cabal-rpm setup
cabal-tweak-flag embedded_double_conversion False

# remove bundled library
rm -r double-conversion

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-double-conversion-devel -f %{oreon_filedir}/ghc-double-conversion-devel.list
%files -n ghc-double-conversion-doc -f %{oreon_filedir}/ghc-double-conversion-doc.list
%files -n ghc-double-conversion-prof -f %{oreon_filedir}/ghc-double-conversion-prof.list

%changelog

%autochangelog
