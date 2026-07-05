%global source0_hash a0f986da26ec03599aa74b4782dfb5ebcd232ed615ec4aba67edec86c5fac2d2

%bcond bootstrap 0

Name:           subunit
Version:        1.4.6
Release:        1%{?dist}
Summary:        C bindings for subunit
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/testing-cabal/subunit
Source0:        https://github.com/testing-cabal/subunit/archive/%{version}/subunit-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  python3-devel
%if %{without bootstrap}
BuildRequires:  pkgconfig(check)
%endif

%description
Subunit C bindings for test result streaming.

%package devel
Summary:        Header files for subunit
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and pkg-config data for libsubunit.

%package static
Summary:        Static C library for subunit
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static libsubunit for statically linked test cases.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

sed "/^tests_LDADD/i libcppunit_subunit_la_LIBADD = -lcppunit libsubunit.la\n" -i Makefile.am
sed -i 's/AC_PROG_LIBTOOL/LT_INIT/' configure.ac
%if %{with bootstrap}
sed -i '/PKG_CHECK_MODULES.*CHECK/d' configure.ac
%endif
autoreconf -fi

%build
export PYTHON=%{_bindir}/python3
%configure --enable-shared --enable-static
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool
%make_build

%install
%make_install INSTALL="%{_bindir}/install -p"

%check
%if %{without bootstrap}
make check
%endif

%files
%doc NEWS README.md
%license Apache-2.0 BSD COPYING
%{_libdir}/libsubunit.so.0{,.*}

%files devel
%doc c/README
%{_includedir}/subunit/child.h
%{_libdir}/libsubunit.so
%{_libdir}/pkgconfig/libsubunit.pc

%files static
%{_libdir}/libsubunit.a
