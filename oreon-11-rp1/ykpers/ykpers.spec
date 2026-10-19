%global source0_hash 0ec84d0ea862f45a7d85a1a3afe5e60b8da42df211bb7d27a50f486e31a79b93
Name:           ykpers
Version:        1.20.0
Release:        1%{?dist}
Summary:        Yubikey personalization program
License:        LicenseRef-Callaway-BSD
URL:            http://opensource.yubico.com/yubikey-personalization/
Source0:        http://opensource.yubico.com/yubikey-personalization/releases/%{name}-%{version}.tar.gz
Patch0:         ykpers-args-extern.patch
%ifnarch s390 s390x
%else
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libusb1-devel
BuildRequires:  libyubikey-devel
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
Yubico's YubiKey can be re-programmed with a new AES key. This is a library
that makes this an easy task.

%package devel
Summary:        Development files for ykpers
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the header file needed to develop applications that
use ykpers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0

%build

%configure --enable-static=no --disable-rpath \
    --with-udevrulesdir=/usr/lib/udev/rules.d \
%ifnarch s390 s390x
    --with-backend=libusb-1.0
%else
    --with-backend=libusb
%endif
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%check

export LD_LIBRARY_PATH=$RPM_BUILD_DIR/%{name}-%{version}/.libs
make check
%install
%make_install INSTALL="%{__install} -p"
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ykpers-devel -f %{oreon_filedir}/ykpers-devel.list

%changelog

%autochangelog
