%global source0_hash 098793854c590b4c2c7e98bc48a45408875f48c5ad47650b5fabbd3e94dd8049

Name:		unuran
Version:	1.11.0
Release:	4%{?dist}
Summary:	Universal Non-Uniform Random number generator

License:	GPL-2.0-or-later
URL:		http://statistik.wu-wien.ac.at/unuran
Source0:	http://statistik.wu-wien.ac.at/unuran/%{name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	gcc-c++

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

%autosetup -p1

%build
%configure --enable-shared --disable-static
%make_build

%install
%make_install
rm $RPM_BUILD_ROOT/%{_libdir}/libunuran.la
rm $RPM_BUILD_ROOT/%{_includedir}/unuran_tests.h
rm $RPM_BUILD_ROOT/%{_infodir}/unuran_win32*
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

# clean examples
rm -rf __dist_examples __clean_examples
cp -a examples __clean_examples
make -C __clean_examples distclean
rm __clean_examples/Makefile*
mkdir __dist_examples
mv __clean_examples __dist_examples/examples

%files
%doc AUTHORS README NEWS KNOWN-PROBLEMS THANKS UPGRADE
%license COPYING
%{_infodir}/unuran*
%{_libdir}/libunuran.so.*

%files devel
%{_includedir}/unuran*.h
%{_libdir}/libunuran.so
%doc doc/unuran.pdf __dist_examples/examples

%check # enable if you want - takes a long time
SEED=2742664 make check

%changelog
%autochangelog
