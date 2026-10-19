%global source1_hash 5fe145041c594689e6e7cf4cd623d5f2b7c36261708be8c9a72aed72cf67acce
%global source0_hash 5fe145041c594689e6e7cf4cd623d5f2b7c36261708be8c9a72aed72cf67acce
%global giturl  https://github.com/SRI-CSL/yices2
Name:           yices
Version:        2.7.0
Release:        1%{?dist}
Summary:        SMT solver
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            http://yices.csl.sri.com/
VCS :           git:%{giturl}.git
Source0:        %{giturl}/archive/%{name}-%{version}.tar.gz
Source1:        https://github.com/ivmai/cudd/archive/cudd-3.0.0.tar.gz
Patch:          %{name}-cryptominisat.patch
Patch:          implicit-int.patch
ExcludeArch:    %{ix86}
Provides:       bundled(cudd) = 3.0.0
# oreon:deps
BuildRequires:  cadical-devel
BuildRequires:  cryptominisat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gperf
BuildRequires:  kissat-devel
BuildRequires:  latexmk
BuildRequires:  libpoly-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  tex(latex)
BuildRequires:  texlive-courier
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-times
# /oreon:deps
%description
Yices 2 is an efficient SMT solver that decides the satisfiability of formulas
containing uninterpreted function symbols with equality, linear real and
integer arithmetic, bitvectors, scalar types, and tuples.

Yices 2 can process input written in the SMT-LIB notation (both versions 2.0
and 1.2 are supported).

Alternatively, you can write specifications using the Yices 2 specification
language, which includes tuples and scalar types.

Yices 2 can also be used as a library in other software.

%package devel
Summary:        Development files for yices
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
%description devel
This package contains the header files necessary for developing programs which
use yices.

%package tools
Summary:        Command line tools that use the yices library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
Command line tools that use the yices library.

%package doc
License:        GPL-3.0-or-later AND BSD-2-Clause AND MIT AND OFL-1.1-RFN AND Knuth-CTAN AND LPPL-1.3a AND AGPL-3.0-only
Summary:        Documentation for yices
BuildArch:      noarch
%description doc
This package contains yices documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n yices2-yices-%{version} -a 1 -p1

%conf
# Do not try to avoid -fstack-protector
sed -i 's/@NO_STACK_PROTECTOR@//' make.include.in

# Do not override our build flags
sed -i 's/ -O3//;s/ -fomit-frame-pointer//' src/Makefile tests/unit/Makefile

# Use $SOURCE_DATE_EPOCH (or current date)
sed -i "s/^now=.*/now=$(date +%Y-%m-%d ${SOURCE_DATE_EPOCH:+--date=@$SOURCE_DATE_EPOCH})/" \
  utils/make_source_version

# Generate the configure scripts
autoreconf -fi
cd cudd-cudd-3.0.0
autoreconf -fi
cd -

# Fix end of line encodings
sed -i 's/\r//' examples/{jinpeng,problem_with_input}.ys

# Fix permissions
sed -i 's/cp/install -m 0644/' utils/make_source_version

%build

cd cudd-cudd-3.0.0
%configure CFLAGS='%{build_cflags} -fPIC' CXXFLAGS='%{build_cxxflags} -fPIC'
%make_build
cd -
export CPPFLAGS="-I$PWD/cudd-cudd-3.0.0/cudd -DHAVE_CADICAL -DHAVE_CRYPTOMINISAT -DHAVE_KISSAT"
export LDFLAGS="%{build_ldflags} -L$PWD/cudd-cudd-3.0.0/cudd/.libs"
export LIBS='-lcadical -lcryptominisat5 -lkissat'
%configure --enable-mcsat
guess=$(./config.guess)
if [ "%{_host}" != "$guess" ]; then
  mv configs/make.include.%{_host} configs/make.include.${guess}
fi
%make_build MODE=debug
make doc
make -C doc/sphinx html
rm doc/sphinx/build/html/.buildinfo
%install
make install prefix=%{buildroot}%{_prefix} exec_prefix=%{buildroot}%{_prefix} \
     bindir=%{buildroot}%{_bindir} libdir=%{buildroot}%{_libdir} \
     includedir=%{buildroot}%{_includedir}/%{name} MODE=debug
rm -f %{buildroot}%{_libdir}/libyices.a
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/*.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check MODE=debug
%files -f %{oreon_filedir}/main.list
%files -n yices-devel -f %{oreon_filedir}/yices-devel.list
%files -n yices-tools -f %{oreon_filedir}/yices-tools.list
%files -n yices-doc -f %{oreon_filedir}/yices-doc.list

%changelog

%autochangelog
