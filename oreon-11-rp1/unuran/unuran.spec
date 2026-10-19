%global source0_hash aba0846715a486ded86cb208b091ea92a043f27281241e96a01a126de1ca0a85
Name:		unuran
Version:	1.12.0
Release:        1%{?dist}
Summary:        Universal Non-Uniform Random number generator
License:	GPL-2.0-or-later
URL:		http://statistik.wu-wien.ac.at/unuran
Source0:        http://statistik.wu-wien.ac.at/unuran/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
UNU.RAN is an ANSI C library licensed under GPL.
It contains universal (also called automatic or black-box) algorithms
that can generate random numbers from large classes of continuous or
discrete distributions, and also from practically all standard
distributions.

The library and an extensive online documentation are available at:

	  -------------------------------------------
	     http://statistik.wu-wien.ac.at/unuran/
	  -------------------------------------------

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Header and object files for unuran
%description devel
Header and object files for unuran, and pdf docs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --enable-shared --disable-static
%make_build
%install
%make_install
rm $RPM_BUILD_ROOT/%{_libdir}/libunuran.la
rm $RPM_BUILD_ROOT/%{_includedir}/unuran_tests.h
rm $RPM_BUILD_ROOT/%{_infodir}/unuran_win32*
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
rm -rf __dist_examples __clean_examples
cp -a examples __clean_examples
make -C __clean_examples distclean
rm __clean_examples/Makefile*
mkdir __dist_examples
mv __clean_examples __dist_examples/examples
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check # enable if you want - takes a long time

SEED=2742664 make check
%files -f %{oreon_filedir}/main.list
%files -n unuran-devel -f %{oreon_filedir}/unuran-devel.list

%changelog

%autochangelog
