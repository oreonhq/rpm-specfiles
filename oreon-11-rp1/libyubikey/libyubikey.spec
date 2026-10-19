%global source0_hash 04edd0eb09cb665a05d808c58e1985f25bb7c5254d2849f36a0658ffc51c3401
Name:           libyubikey
Version:        1.13
Release:        27%{?dist}
Summary:        C library for decrypting and parsing Yubikey One-time passwords
License:        LicenseRef-Callaway-BSD
URL:            http://opensource.yubico.com/yubico-c
Source0:        http://opensource.yubico.com/yubico-c/releases/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%check

export LD_LIBRARY_PATH=${RPM_BUILD_DIR}/%{name}-%{version}/.libs
make check
%install
%make_install INSTALL="install -p"
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libyubikey-devel -f %{oreon_filedir}/libyubikey-devel.list

%changelog

%autochangelog

