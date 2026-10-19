%global source0_hash cfb326c7ca2639c401c00f0207ef67ee2ea2b6e595f1e1e6d2de3b11126a2830
%{?mingw_package_header}
%global pkgname twaindsm
Name:          mingw-%{pkgname}
Version:       2.5.1
Release:        1%{?dist}
Summary:        TWAIN Data Source Manager
License:       LicenseRef-Callaway-LGPLv2+
URL:           https://github.com/twain/twain-dsm
BuildArch:     noarch
Source0:        https://github.com/twain/twain-dsm/archive/v%{version}/%{pkgname}-%{version}.tar.gz
Patch0:        twaindsm_defs.patch
Patch1:        twaindsm_cmake.patch
Patch2:        twaindsm_build-errors.patch
Patch10:        twaindsm_assert.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
%description
TWAIN Data Source Manager, compliant with the TWAIN specification version 2.2.

###############################################################################

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

###############################################################################

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

###############################################################################

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir twain-dsm-%{version}
%oreon_prep
%build

pushd TWAIN_DSM/src
%mingw_cmake .
%mingw_make_build VERBOSE=1
popd
%install
pushd TWAIN_DSM/src
%mingw_make_install
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-twaindsm -f %{oreon_filedir}/mingw32-twaindsm.list
%files -n mingw64-twaindsm -f %{oreon_filedir}/mingw64-twaindsm.list

%changelog

%autochangelog
