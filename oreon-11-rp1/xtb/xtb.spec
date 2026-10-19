%global source0_hash 52506a689147cdb4695bf1c666158b6d6d6b31726fecaa5bf53af7f4e3f3d20d
%define soname 6
%global blaslib openblas
%global blasvar o
%global __requires_exclude_from ^%{_datadir}/xtb/.*$
Name:           xtb
Version:        6.7.1
Release:        6%{?dist}
Summary:        Semiempirical Extended Tight-Binding Program Package
License:        LGPL-3.0-or-later
URL:            https://github.com/grimme-lab/xtb/
Source0:        https://github.com/grimme-lab/xtb/archive/v%{version}/xtb-%{version}.tar.gz
Patch0:         xtb-6.5.1-fedora.patch
Patch4:         xtb-6.3.2-environment.patch
Patch5:         xtb-6.7.1-formatting.patch
ExcludeArch:    s390x
Requires:       %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  dftd4-devel
BuildRequires:  gcc-gfortran
BuildRequires:  hostname
BuildRequires:  mctc-lib-devel
BuildRequires:  meson
BuildRequires:  multicharge-devel
BuildRequires:  ninja-build
BuildRequires:  openblas-devel
BuildRequires:  rubygem-asciidoctor
BuildRequires:  test-drive-devel
# /oreon:deps
%description
The xtb program package developed by the Grimme group in Bonn.

%package data
Summary:   Data files for xtb
BuildArch: noarch
%description data
This package contains the data files for xtb.

%package libs
Summary:   Shared libraries for xtb
Requires: hostname
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
%meson -Dlapack=custom -Dcustom_libraries=%{blaslib}%{blasvar} -Dtblite=disabled -Dcpcmx=disabled
date=$(date)
cat > %{_vpath_builddir}/xtb_version.fh <<EOF
character(len=*),parameter :: version = "%{version}-%{release}%{dist}"
character(len=*),parameter :: date = "$date"
character(len=*),parameter :: author = "Fedora project"
EOF
ninja -C %{_vpath_builddir} -j %{_smp_build_ncpus} %{?__meson_verbose:--verbose} libxtb.a
%meson_build
%install
%meson_install
rm %{buildroot}%{_libdir}/libxtb.a
rm -rf %{buildroot}%{_datadir}/modules
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/xtb.sh <<EOF
XTBPATH=%{_datadir}/xtb
export XTBPATH
EOF
cat > %{buildroot}%{_sysconfdir}/profile.d/xtb.csh <<EOF
setenv XTBPATH %{_datadir}/xtb
EOF
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export HOSTNAME=$(hostname)
export OMP_NUM_THREADS=1
%meson_test --timeout-multiplier=10
%files -f %{oreon_filedir}/main.list
%files -n xtb-data -f %{oreon_filedir}/xtb-data.list
%files -n xtb-libs -f %{oreon_filedir}/xtb-libs.list
%files -n xtb-devel -f %{oreon_filedir}/xtb-devel.list

%changelog

%autochangelog
