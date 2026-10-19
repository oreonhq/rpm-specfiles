%global source0_hash 26aa624525a636de272c0b329e2dfd01a0d5b7827f1c1c76f393d71e37dead70
Name:           DSDP
Version:        5.8
Release:        41%{?dist}
Summary:        Software for semidefinite programming
License:        DSDP AND OFL-1.1-RFN AND Knuth-CTAN
URL:            https://www.mcs.anl.gov/hs/software/DSDP/
Source0:        https://www.mcs.anl.gov/hs/software/DSDP/%{name}%{version}.tar.gz
Source1:        DSDP-man.tar.xz
Source2:        DSDP.Makefile
Patch:          %{name}-overflow.patch
Patch:          %{name}-int-in-bool-context.patch
Patch:          %{name}-type-mismatch.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  doxygen-latex
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)
# /oreon:deps
%description
DSDP is a free open source implementation of an interior-point method for
semidefinite programming.  It provides primal and dual solutions, exploits
low-rank structure and sparsity in the data, and has relatively low memory
requirements for an interior-point method.  It allows feasible and infeasible
starting points and provides approximate certificates of infeasibility when no
feasible solution exists.  The dual-scaling algorithm implemented in this
package has a convergence proof and worst-case polynomial complexity under
mild assumptions on the data.  The software can be used as a set of
subroutines, through Matlab, or by reading and writing to data files.
Furthermore, the solver offers scalable parallel performance for large
problems and a well documented interface.  Some of the most popular
applications of semidefinite programming and linear matrix inequalities (LMI)
are model control, truss topology design, and semidefinite relaxations of
combinatorial and global optimization problems.

%package devel
License:        DSDP AND OFL-1.1-RFN AND Knuth-CTAN
Summary:        Headers and libraries for developing with DSDP
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       bundled(js-jquery)
%description devel
Headers and libraries for developing with DSDP.

%package examples
License:        DSDP
Summary:        Example programs that use DSDP
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description examples
Examples programs that use the DSDP library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}%{version} -a 1

%conf
sed -e 's|@RPM_OPT_FLAGS@|%{build_cflags}|' \
    -e 's|@RPM_LD_FLAGS@|%{build_ldflags}|' \
    -e 's|@libdir@|%{_libdir}|' \
    -e 's|@version@|%{version}|' \
    %{SOURCE2} > Makefile

%build

%make_build
cd docs
unzip DSDP5-api-html.zip
cd dox
rm -fr html images
doxygen
%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
install -p -m 0755 src/libdsdp.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -s libdsdp.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libdsdp.so.5
ln -s libdsdp.so.5 $RPM_BUILD_ROOT%{_libdir}/libdsdp.so
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -a include $RPM_BUILD_ROOT%{_includedir}/DSDP
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for f in maxcut theta stable color; do
  install -p -m 0755 examples/$f $RPM_BUILD_ROOT%{_bindir}/dsdp-$f
done
install -p -m 0755 examples/dsdp5 $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cd man
for f in *.1; do
  sed "s/@VERSION@/%{version}/" $f > $RPM_BUILD_ROOT%{_mandir}/man1/$f
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n DSDP-devel -f %{oreon_filedir}/DSDP-devel.list
%files -n DSDP-examples -f %{oreon_filedir}/DSDP-examples.list

%changelog

%autochangelog
