%global source0_hash 52506a689147cdb4695bf1c666158b6d6d6b31726fecaa5bf53af7f4e3f3d20d

%define soname 6

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar o
%endif

# avoid bash/tcsh dependencies from config_env scripts
%global __requires_exclude_from ^%{_datadir}/xtb/.*$

Name:           xtb
Version:        6.7.1
Release:        6%{?dist}
Summary:        Semiempirical Extended Tight-Binding Program Package
License:        LGPL-3.0-or-later
URL:            https://github.com/grimme-lab/xtb/
Source0:        https://github.com/grimme-lab/xtb/archive/v%{version}/xtb-%{version}.tar.gz

# Fedora versioning
Patch0:         xtb-6.5.1-fedora.patch
# Add sanity checks to environment variables, https://github.com/grimme-lab/xtb/pull/317
Patch4:         xtb-6.3.2-environment.patch
# Fix fortran formatting, issue was fixed upstream in #1278
Patch5:         xtb-6.7.1-formatting.patch

BuildRequires:  gcc-gfortran
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  %{blaslib}-devel
# To generate man pages
BuildRequires:  rubygem-asciidoctor
# The program queries $HOSTNAME at runtime and so fails to run in mock without this
BuildRequires:  hostname
BuildRequires:  mctc-lib-devel
BuildRequires:  test-drive-devel
BuildRequires:  multicharge-devel
BuildRequires:  dftd4-devel

# Tests fail on s390x for some reason
ExcludeArch:    s390x

# Need data files to run
Requires:       %{name}-data = %{version}-%{release}

%description
The xtb program package developed by the Grimme group in Bonn.

%package data
Summary:   Data files for xtb
BuildArch: noarch

%description data
This package contains the data files for xtb.

%package libs
Summary:   Shared libraries for xtb
# The program queries $HOSTNAME at runtime and so fails to run in mock without this
Requires: hostname
# Need data files to run
Requires:       %{name}-data = %{version}-%{release}

%description libs
This package contains the shared libraries for xtb.

%package devel
Summary:   Development headers for xtb
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains development headers for xtb.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1 -b .fedoraver
%patch 4 -p1 -b .env
%patch 5 -p1 -b .formatting

%build
export FFLAGS="$FFLAGS -fPIC"
export FCFLAGS="$FCFLAGS -fPIC"
# TODO: tblite and cpcm-x support should ideally be turned on, but the packages are not yet in Fedora
%meson -Dlapack=custom -Dcustom_libraries=%{blaslib}%{blasvar} -Dtblite=disabled -Dcpcmx=disabled
date=$(date)
# Create customized Fedora versioning
cat > %{_vpath_builddir}/xtb_version.fh <<EOF
character(len=*),parameter :: version = "%{version}-%{release}%{dist}"
character(len=*),parameter :: date = "$date"
character(len=*),parameter :: author = "Fedora project"
EOF
# Meson dependency workaround from BZ #2390464
ninja -C %{_vpath_builddir} -j %{_smp_build_ncpus} %{?__meson_verbose:--verbose} libxtb.a
%meson_build

%install
%meson_install
# Remove static library
rm %{buildroot}%{_libdir}/libxtb.a
# Remove environment module files
rm -rf %{buildroot}%{_datadir}/modules

# Create profile files
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/xtb.sh <<EOF
XTBPATH=%{_datadir}/xtb
export XTBPATH
EOF
cat > %{buildroot}%{_sysconfdir}/profile.d/xtb.csh <<EOF
setenv XTBPATH %{_datadir}/xtb
EOF

%check
# Set missing environment variable
export HOSTNAME=$(hostname)
# Turn off use of OpenMP parallelism since tests are already run in parallel
export OMP_NUM_THREADS=1
# Tests time out
%meson_test --timeout-multiplier=10

%files
# LGPLv3+ license is stated at bottom of README.md
%doc README.md CONTRIBUTING.md
%license COPYING COPYING.LESSER README.md
%{_mandir}/man1/xtb.1*
%{_mandir}/man7/xcontrol.7*
%{_bindir}/xtb

%files data
%{_sysconfdir}/profile.d/xtb.sh
%{_sysconfdir}/profile.d/xtb.csh
%{_datadir}/xtb/

%files libs
%license COPYING COPYING.LESSER README.md
%{_libdir}/libxtb.so.%{soname}*

%files devel
%{_includedir}/xtb.h
%{_libdir}/libxtb.so
%{_libdir}/pkgconfig/xtb.pc

%changelog
%autochangelog
