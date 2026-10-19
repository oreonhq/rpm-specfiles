%global source0_hash 0550623c85aa37897638a6b10d267c311a788d137509692d8d858fba10a852da
%global giturl  https://github.com/flintlib/flint
Name:           flint
Version:        3.6.0
Release:        1%{?dist}
Summary:        Fast Library for Number Theory
License:        LGPL-3.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later AND (LGPL-3.0-or-later OR GPL-2.0-or-later) AND BSD-2-Clause
URL:            https://flintlib.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch:          %{name}-arch.patch
Patch:          %{giturl}/pull/2506.patch
ExcludeArch:    %{ix86}
Obsoletes:      antic < 3.0.0
Obsoletes:      arb < 3.0.0
Obsoletes:      arb-doc < 3.0.0
Obsoletes:      flint-static < 3.0.0
Provides:       antic = %{version}-%{release}
Provides:       arb = %{version}-%{release}
Provides:       arb-doc = %{version}-%{release}
Provides:       flint-static = %{version}-%{release}
# oreon:deps
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  ntl-devel
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  python3dist(sphinx)
BuildRequires:  tex(latex)
# /oreon:deps
%description
FLINT is a C library for doing number theory, written by William Hart and
David Harvey.

%package        devel
Summary:        Development files for FLINT
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      antic-devel < 3.0.0
Provides:       antic-devel = %{version}-%{release}
Obsoletes:      arb-devel < 3.0.0
Provides:       arb-devel = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# sanitize header files
ln -sf $PWD flint
# sanitize references to external headers
for fil in $(find src -name \*.c -o -name \*.h -o -name \*.in); do
  sed -ri.orig 's/"((gc|math|mpfr)\.h)"/<\1>/' $fil
  fixtimestamp $fil
done
# sanitize references to project headers
for fil in $(find src -name \*.c -o -name \*.h); do
  sed -ri.orig 's@"(\.\./)?([^"]+\.h])"@<flint/\2>@' $fil
  fixtimestamp $fil
done
# "

# Use the classic sphinx theme
sed -i "s/'default'/'classic'/" doc/source/conf.py

# Look for flexiblas
sed -i 's/openblas/flexiblas/' configure

# FLINT builds and passes all tests without this using GCC <= 14
# Tests fail with incorrect answers using GCC >= 15.0
CFLAGS='%{build_cflags} -fno-strict-aliasing'
CXXFLAGS='%{build_cxxflags} -fno-strict-aliasing'
%configure \
  --disable-static \
  --with-blas-include=%{_includedir}/flexiblas \
  --with-ntl-include=%{_includedir}/NTL

%build

%make_build
make -C doc html
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export FLEXIBLAS=netlib
make check
%files -f %{oreon_filedir}/main.list
%files -n flint-devel -f %{oreon_filedir}/flint-devel.list

%changelog

%autochangelog
