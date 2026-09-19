%global source0_hash 474852d6715ddc3b6969e28de5e1a5fbaff9e8ece6aebb9dc1cc63e9e88e89ab

Name:           libmatheval
Version:        1.1.11
Release:        28%{?dist}
Summary:        Library for parsing and evaluating symbolic expressions input as text

License:        GPL-3.0-or-later
URL:            http://www.gnu.org/software/libmatheval/
Source0:        http://ftp.gnu.org/gnu/libmatheval/libmatheval-%{version}.tar.gz

BuildRequires:  gcc-gfortran, compat-guile18-devel, bison, flex, flex-static, texinfo
BuildRequires: make

%description
GNU libmatheval is a library (callable from C and Fortran) to parse
and evaluate symbolic expressions input as text.  It supports
expressions in any number of variables of arbitrary names, decimal and
symbolic constants, basic unary and binary operators, and elementary
mathematical functions.  In addition to parsing and evaluation,
libmatheval can also compute symbolic derivatives and output
expressions to strings.

%package devel
Summary:        Development files for libmatheval
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package contains the development files for libmatheval.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
export GUILE=/usr/bin/guile1.8
export GUILE_CONFIG=/usr/bin/guile1.8-config
export GUILE_TOOLS=/usr/bin/guile1.8-tools
%configure F77=gfortran --disable-static
make %{?_smp_mflags}

%check
make check ||:

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%ldconfig_scriptlets

%files
%doc COPYING AUTHORS README
%{_libdir}/*.so.*

%files devel
%doc NEWS 
%{_includedir}/*
%{_libdir}/*.so
%{_infodir}/libmatheval.info*
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
