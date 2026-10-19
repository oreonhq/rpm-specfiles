%global source0_hash 6bd2fd41d95efb0bf599aa5c6bc406f0d6fff803fccfe854db4835041c6267ee
Name:           mathic
Version:        1.5
Release:        1%{?dist}
Summary:        Data structures for Groebner basis computations
License:        LGPL-2.0-or-later
URL:            https://github.com/Macaulay2/mathic
VCS:            git:%{url}.git
Source0:        https://github.com/Macaulay2/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(memtailor)
# /oreon:deps
%description
Mathic is a C++ library of fast data structures designed for use in Groebner
basis computation.  This includes data structures for ordering S-pairs,
performing divisor queries and ordering polynomial terms during polynomial
reduction.

With Mathic you get to use highly optimized code with little effort so that
you can focus more of your time on whatever part of your Groebner basis
implementation that you are interested in.  The data structures use templates
to allow you to use them with whatever representation of monomials/terms and
coefficients that your code uses.  In fact the only places where Mathic
defines its own monomials/terms is in the test code and example code.
Currently only dense representations of terms/monomials are suitable since
Mathic will frequently ask "what is the exponent of variable number x in this
term/monomial?".

%package devel
Summary:        Development files for mathic
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       memtailor-devel%{?_isa}
%description devel
Files for developing applications that use mathic.

%package tools
Summary:        Mathic-based tools
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
Mathic-based tools.  Currently this contains:
- divsim: divisor query simulation
- pqsim: priority queue simulation

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Fix the URL in the pkgconfig file
sed -i 's/broune/Macaulay2/' build/autotools/mathic.pc.in

# Upstream doesn't generate the configure script
autoreconf -fi .

%build

export GTEST_PATH=%{_prefix}
export GTEST_VERSION=$(gtest-config --version)
%configure --disable-static --enable-shared --with-gtest=yes GTEST_LIBS=-lgtest
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool
%make_build
%make_build divsim pqsim
%install
%make_install
mkdir -p %{buildroot}%{_bindir}
cp -p .libs/{divsim,pqsim} %{buildroot}%{_bindir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LD_LIBRARY_PATH=$PWD/.libs
make check
%files -f %{oreon_filedir}/main.list
%files -n mathic-devel -f %{oreon_filedir}/mathic-devel.list
%files -n mathic-tools -f %{oreon_filedir}/mathic-tools.list

%changelog

%autochangelog
