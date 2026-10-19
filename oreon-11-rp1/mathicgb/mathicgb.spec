%global source0_hash c2d29521e26fa6024c1be85c5f8273324e2e3bed874327c0b07652986a7ede89
Name:           mathicgb
Version:        1.4
Release:        1%{?dist}
Summary:        Groebner basis computations
License:        GPL-2.0-or-later
URL:            https://github.com/Macaulay2/mathicgb
VCS:            git:%{url}.git
Source0:        https://github.com/Macaulay2/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(mathic)
BuildRequires:  pkgconfig(tbb)
# /oreon:deps
%description
Mathicgb is a program for computing Groebner basis and signature Groebner
bases.  Mathicgb is based on the fast data structures from mathic.

%package devel
Summary:        Development files for mathicgb
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Files for developing applications that use mathicgb.

%package libs
Summary:        Mathicgb libraries
%description libs
Library interface to mathicgb.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%conf
# Fix end-of-line encoding
sed -i.orig 's/\r//' doc/description.txt
touch -r doc/description.txt.orig doc/description.txt
rm -f doc/description.txt.orig

# Fix the URL in the pkgconfig file
sed -i 's/broune/Macaulay2/' build/autotools/mathicgb.pc.in

# Upstream doesn't generate the configure script
autoreconf -fi

%build

export GTEST_PATH=%{_prefix}
%configure --disable-static --enable-shared --with-gtest=yes
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool
sed -i 's|g++$|& -Wl,--as-needed|' Makefile
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LD_LIBRARY_PATH=$PWD/.libs
make check
%files -f %{oreon_filedir}/main.list
%files -n mathicgb-devel -f %{oreon_filedir}/mathicgb-devel.list
%files -n mathicgb-libs -f %{oreon_filedir}/mathicgb-libs.list

%changelog

%autochangelog
