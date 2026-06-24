%global source0_hash none

Name:           libyubikey
Version:        1.13
Release:        27%{?dist}
Summary:        C library for decrypting and parsing Yubikey One-time passwords

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://opensource.yubico.com/yubico-c
Source0:        http://opensource.yubico.com/yubico-c/releases/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: make

%description
This package holds a low-level C software development kit for the Yubico
authentication device, the Yubikey.

%package devel
Summary:        Development files for libyubikey
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header file needed to develop applications that use
libyubikey.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-static --disable-silent-rules
# --disable-rpath doesn't work for the configure script
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%check
export LD_LIBRARY_PATH=${RPM_BUILD_DIR}/%{name}-%{version}/.libs
make check

%install
%make_install INSTALL="install -p"

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS ChangeLog README
%license COPYING
%{_bindir}/modhex
%{_bindir}/ykparse
%{_bindir}/ykgenerate
%{_libdir}/libyubikey.so.0
%{_libdir}/libyubikey.so.0.1.7
%{_mandir}/man1/ykgenerate.1*
%{_mandir}/man1/ykparse.1*
%{_mandir}/man1/modhex.1*

%files devel
%{_includedir}/yubikey.h
%{_libdir}/libyubikey.so
%exclude %{_libdir}/libyubikey.la

%changelog
%autochangelog

