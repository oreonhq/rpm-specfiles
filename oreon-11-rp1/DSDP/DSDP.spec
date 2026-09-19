%global source0_hash 26aa624525a636de272c0b329e2dfd01a0d5b7827f1c1c76f393d71e37dead70

Name:           DSDP
Version:        5.8
Release:        41%{?dist}
Summary:        Software for semidefinite programming

# The content is DSDP.  The remaining licenses cover the various fonts embedded
# in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
License:        DSDP AND OFL-1.1-RFN AND Knuth-CTAN
URL:            https://www.mcs.anl.gov/hs/software/DSDP/
Source0:        https://www.mcs.anl.gov/hs/software/DSDP/%{name}%{version}.tar.gz
# Man pages written by Jerry James using text from the sources.
# Therefore, the man pages have the same copyright and license as the source.
Source1:        DSDP-man.tar.xz
# A substitute makefile to fix the brokenness of the distributed Makefiles
Source2:        DSDP.Makefile
# Fix a buffer overflow in one of the examples.
Patch:          %{name}-overflow.patch
# Fix -Wint-in-bool-context warnings.
Patch:          %{name}-int-in-bool-context.patch
# Fix big endian problems (patch courtesy of Debian)
Patch:          %{name}-type-mismatch.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  doxygen-latex
BuildRequires:  gcc
BuildRequires:  ghostscript
BuildRequires:  make
BuildRequires:  pkgconfig(flexiblas)

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
# The content is DSDP.  The remaining licenses cover the various fonts embedded
# in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
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
# Install the library
mkdir -p $RPM_BUILD_ROOT%{_libdir}
install -p -m 0755 src/libdsdp.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -s libdsdp.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libdsdp.so.5
ln -s libdsdp.so.5 $RPM_BUILD_ROOT%{_libdir}/libdsdp.so

# Install the header files
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -a include $RPM_BUILD_ROOT%{_includedir}/DSDP

# Install the example programs with a dsdp- prefix, except for dsdp5
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for f in maxcut theta stable color; do
  install -p -m 0755 examples/$f $RPM_BUILD_ROOT%{_bindir}/dsdp-$f
done
install -p -m 0755 examples/dsdp5 $RPM_BUILD_ROOT%{_bindir}

# Install the man pages
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cd man
for f in *.1; do
  sed "s/@VERSION@/%{version}/" $f > $RPM_BUILD_ROOT%{_mandir}/man1/$f
done

%files
%doc docs/DSDP5-Exe-UserGuide.pdf docs/DSDP5-P1289-0905.pdf
%license dsdp-license
%{_libdir}/libdsdp.so.5{,.*}

%files devel
%doc docs/DSDP5-API-UserGuide.pdf docs/dox
%{_libdir}/libdsdp.so
%{_includedir}/DSDP

%files examples
%doc examples/Contents
%{_bindir}/dsdp*
%{_mandir}/man1/dsdp*

%changelog
%autochangelog
