%global source0_hash cfb326c7ca2639c401c00f0207ef67ee2ea2b6e595f1e1e6d2de3b11126a2830

%{?mingw_package_header}

%global pkgname twaindsm

Name:          mingw-%{pkgname}
Version:       2.5.1
Release:       11%{?dist}
Summary:       TWAIN Data Source Manager

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           https://github.com/twain/twain-dsm
BuildArch:     noarch
Source0:       https://github.com/twain/twain-dsm/archive/v%{version}/%{pkgname}-%{version}.tar.gz

### Upstreamable patches: https://github.com/twain/twain-dsm/pull/4
# Use TWNDSM_OS to detect platform instead of TWNDSM_CMP
# - sed -i 's/TWNDSM_CMP == TWNDSM_CMP_VISUALCPP/TWNDSM_OS == TWNDSM_OS_WINDOWS/g' src/{*.cpp,*.h}
# - sed -i 's/(TWNDSM_CMP == TWNDSM_CMP_GNUGPP)/(TWNDSM_OS == TWNDSM_OS_LINUX) || (TWNDSM_OS == TWNDSM_OS_MACOSX)/g' src/{*.cpp,*.h}
Patch0:        twaindsm_defs.patch
# Add MINGW support to the cmake file
# Increase minimum cmake version to 3.5
Patch1:        twaindsm_cmake.patch
# Fix build failure due to invalid conversion
Patch2:        twaindsm_build-errors.patch

### Downstream patch (could be discussed upstream I suppose)
# Don't raise an assertion just because an error occured, leave it to the consumer to deal with the error...
Patch10:        twaindsm_assert.patch

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++

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

%autosetup -p1 -n twain-dsm-%{version}

%build
pushd TWAIN_DSM/src
%mingw_cmake .
%mingw_make_build VERBOSE=1
popd

%install
pushd TWAIN_DSM/src
%mingw_make_install
popd

%files -n mingw32-%{pkgname}
%doc TWAIN_DSM/README.txt TWAIN_DSM/ChangeLog.txt
%license TWAIN_DSM/license.txt
%{mingw32_bindir}/twaindsm.dll
%{mingw32_libdir}/libtwaindsm.dll.a
%{mingw32_includedir}/twain.h

%files -n mingw64-%{pkgname}
%doc TWAIN_DSM/README.txt TWAIN_DSM/ChangeLog.txt
%license TWAIN_DSM/license.txt
%{mingw64_bindir}/twaindsm.dll
%{mingw64_libdir}/libtwaindsm.dll.a
%{mingw64_includedir}/twain.h

%changelog
%autochangelog
