%global source0_hash none

%global mingw_build_ucrt64 1
# The mingw-w64-headers provide the headers pthread_time.h
# and pthread_unistd.h by default and are dummy headers.
# The real implementation for these headers is in a separate
# library called winpthreads. As long as winpthreads isn't
# build, the flag below needs to be set to 1. When winpthreads
# is available then this flag needs to be set to 0 to avoid
# a file conflict with the winpthreads headers.
%global bundle_dummy_pthread_headers 0

Name:           mingw-headers
Version:        13.0.0
Release:        3%{?dist}
Summary:        Win32/Win64 header files

License:        BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later AND ZPL-2.1 AND MIT-Khronos-old AND LicenseRef-Fedora-Public-Domain
URL:            http://mingw-w64.sourceforge.net/
Source0:        https://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}%{?pre:-%{pre}}.tar.bz2

# Our RPM macros automatically set the environment variable WIDL
# This confuses the mingw-headers configure scripts and causes various
# headers to be regenerated from their .idl source. Prevent this from
# happening as the .idl files shouldn't be used by default
Patch0:         mingw-headers-no-widl.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires: mingw32-filesystem >= 133
BuildRequires: mingw64-filesystem >= 133
BuildRequires: ucrt64-filesystem >= 133


%description
MinGW Windows cross-compiler Win32 and Win64 header files.


%package -n mingw32-headers
Summary:        MinGW Windows cross-compiler Win32 header files
Requires:       mingw32-filesystem >= 95
%if 0%{bundle_dummy_pthread_headers} == 0
Requires:       mingw32-winpthreads
%endif

%description -n mingw32-headers
MinGW Windows cross-compiler Win32 header files.

%package -n mingw64-headers
Summary:        MinGW Windows cross-compiler Win64 header files
Requires:       mingw64-filesystem >= 95
%if 0%{bundle_dummy_pthread_headers} == 0
Requires:       mingw64-winpthreads
%endif

%description -n mingw64-headers
MinGW Windows cross-compiler Win64 header files.

%package -n ucrt64-headers
Summary:        MinGW Windows cross-compiler Win64 header files
Requires:       ucrt64-filesystem >= 133
%if 0%{bundle_dummy_pthread_headers} == 0
Requires:       ucrt64-winpthreads
%endif

%description -n ucrt64-headers
MinGW Windows cross-compiler Win64 header files.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n mingw-w64-v%{version}%{?pre:-%{pre}}


%build
export MINGW32_CONFIGURE_ARGS="--with-default-msvcrt=msvcrt"
export MINGW64_CONFIGURE_ARGS="--with-default-msvcrt=msvcrt"
export UCRT64_CONFIGURE_ARGS="--with-default-msvcrt=ucrt"

pushd mingw-w64-headers
    %mingw_configure --enable-sdk=all --enable-idl
popd


%install
pushd mingw-w64-headers
    %mingw_make_install
popd

# Drop the dummy pthread headers if necessary
%if 0%{?bundle_dummy_pthread_headers} == 0
rm -f %{buildroot}%{mingw32_includedir}/pthread_signal.h
rm -f %{buildroot}%{mingw32_includedir}/pthread_time.h
rm -f %{buildroot}%{mingw32_includedir}/pthread_unistd.h
rm -f %{buildroot}%{mingw64_includedir}/pthread_signal.h
rm -f %{buildroot}%{mingw64_includedir}/pthread_time.h
rm -f %{buildroot}%{mingw64_includedir}/pthread_unistd.h
rm -f %{buildroot}%{ucrt64_includedir}/pthread_signal.h
rm -f %{buildroot}%{ucrt64_includedir}/pthread_time.h
rm -f %{buildroot}%{ucrt64_includedir}/pthread_unistd.h
%endif


%files -n mingw32-headers
%license COPYING DISCLAIMER DISCLAIMER.PD
%{mingw32_includedir}/*

%files -n mingw64-headers
%license COPYING DISCLAIMER DISCLAIMER.PD
%{mingw64_includedir}/*

%files -n ucrt64-headers
%license COPYING DISCLAIMER DISCLAIMER.PD
%{ucrt64_includedir}/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.0.0-3
- Prepare for Oreon 11 (RP1)
