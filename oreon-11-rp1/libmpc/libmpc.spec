%global source0_hash none
%global source1_hash none

# build compat-libmpc for bootstrapping purposes
%global bootstrap 0
%global bootstrap_version 0.9

Summary: C library for multiple precision complex arithmetic
Name: libmpc
Version: 1.3.1
Release: 9%{?dist}
# LGPL-3.0-or-later: the library
# FSFAP: README and NEWS
License: LGPL-3.0-or-later AND FSFAP
URL: https://www.multiprecision.org/mpc/
Source0: https://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.gz
%if 0%{?bootstrap}
Source1: https://ftp.gnu.org/gnu/mpc/mpc-%{bootstrap_version}.tar.gz
%endif

BuildRequires: gcc
BuildRequires: gmp-devel >= 5.0.0
BuildRequires: mpfr-devel >= 4.1.0
BuildRequires: make

%if 0%{?bootstrap} == 0
Obsoletes: compat-libmpc < %{version}-1
Provides: compat-libmpc = %{version}-%{release}
%endif

%description
MPC is a C library for the arithmetic of complex numbers with arbitrarily high
precision and correct rounding of the result.  It is built upon and follows
the same principles as Mpfr.

%package devel
Summary: Headers and shared development libraries for MPC
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gmp-devel%{?_isa}
Requires: mpfr-devel%{?_isa}

%description devel
Header files and shared library symlinks for the MPC library.

%package doc
Summary: Documentation for the MPC library
License: GFDL-1.3-no-invariants-or-later
BuildArch: noarch

%description doc
Documentation for the MPC library.

%if 0%{?bootstrap}
%package -n compat-libmpc
Summary: compat/bootstrap mpc-%{bootstrap_version} library

%description -n compat-libmpc
Contains the .so files for mpc version %{bootstrap-version}.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%setup -q -n mpc-%{version}
%if 0%{?bootstrap}
%setup -q -n mpc-%{version} -a 1
%endif

%build
%configure --disable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%if 0%{?bootstrap}
export CPPFLAGS="%{optflags} -std=gnu99"
export CFLAGS="%{optflags} -std=gnu99"
export EGREP=egrep

pushd mpc-%{bootstrap_version}
%configure --disable-static
%make_build
popd
%endif

%install
%if 0%{?bootstrap}
%make_install -C mpc-%{bootstrap_version}

## remove everything but shlib
rm -fv %{buildroot}%{_libdir}/libmpc.so
rm -fv %{buildroot}%{_includedir}/*
rm -fv %{buildroot}%{_infodir}/*
%endif

%make_install
rm -f %{buildroot}%{_infodir}/dir

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make check

%files
%license COPYING.LESSER
%doc README NEWS
%{_libdir}/libmpc.so.3{,.*}

%files devel
%{_libdir}/libmpc.so
%{_includedir}/mpc.h

%files doc
%doc AUTHORS
%{_infodir}/*.info*

%if 0%{?bootstrap}
%files -n compat-libmpc
%{_libdir}/libmpc.so.2{,.*}
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-9
- Prepare for Oreon 11 (RP1)
