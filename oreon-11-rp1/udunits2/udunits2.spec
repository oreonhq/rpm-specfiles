%global source0_hash 590baec83161a3fd62c00efa66f6113cec8a7c461e3f61a5182167e0cc5d579e

Name: udunits2
Version: 2.2.28
Release: 13%{?dist}
Summary: A library for manipulating units of physical quantities
License: UCAR
URL: http://www.unidata.ucar.edu/software/udunits/
Source0: ftp://ftp.unidata.ucar.edu/pub/udunits/udunits-%{version}.tar.gz
# default_udunits2_xml_path() is buggy and broken
Patch0: udunits-2.2.28-fix-xml-path-logic.patch
BuildRequires: make
BuildRequires: gcc-c++, groff, byacc, expat-devel, CUnit-devel
BuildRequires: chrpath
BuildRequires: /usr/bin/makeinfo
BuildRequires: /usr/bin/texi2dvi
# workaround touching configure during build by the %%configure macro on ppc64le RHEL 7
# can go away when upstream refreshes the autoconf/libtool files
%if 0%{?rhel} == 7
%ifarch ppc64le
BuildRequires: texinfo-tex
%endif
%endif

%description
The Unidata units utility, udunits2, supports conversion of unit specifications 
between formatted and binary forms, arithmetic manipulation of unit 
specifications, and conversion of values between compatible scales of 
measurement. A unit is the amount by which a physical quantity is measured. For 
example:

                  Physical Quantity   Possible Unit
                  _________________   _____________
                        time              weeks
                      distance         centimeters
                        power             watts

This utility works interactively and has two modes. In one mode, both an input 
and output unit specification are given, causing the utility to print the 
conversion between them. In the other mode, only an input unit specification is 
given. This causes the utility to print the definition -- in standard units -- 
of the input unit.

%package devel
Summary: Headers and libraries for udunits2
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the files needed for compiling programs using
the udunits2 library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n udunits-%{version}
%patch -P0 -p1 -b .bad-logic

%build
%configure --disable-static --docdir %{_docdir}/%{name}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install install-html install-pdf
# Remove rpath
chrpath -d %{buildroot}%{_bindir}/*
# Install info and doc
mkdir -p %{buildroot}%{_infodir}/
install -p -m0644 %{name}.info %{buildroot}%{_infodir}
# we get this in %%license
rm -rf %{buildroot}%{_docdir}/%{name}/COPYRIGHT

# We need to do this to avoid conflicting with udunits v1
mkdir -p %{buildroot}%{_includedir}/%{name}/
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/%{name}/
rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_infodir}/dir

%check
make check

%files
%license COPYRIGHT
%{_bindir}/%{name}
%{_datadir}/udunits/
%{_infodir}/%{name}*.info*
%{_libdir}/libudunits2.so.*
%doc %{_docdir}/%{name}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libudunits2.so

%changelog
%autochangelog
