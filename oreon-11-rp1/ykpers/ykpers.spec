%global source0_hash 0ec84d0ea862f45a7d85a1a3afe5e60b8da42df211bb7d27a50f486e31a79b93

Name:           ykpers
Version:        1.20.0
Release:        18%{?dist}
Summary:        Yubikey personalization program

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://opensource.yubico.com/yubikey-personalization/
Source0:        http://opensource.yubico.com/yubikey-personalization/releases/%{name}-%{version}.tar.gz
Patch0:         ykpers-args-extern.patch

%ifnarch s390 s390x
BuildRequires: libusb1-devel
%else
BuildRequires: libusb-compat-0.1-devel
%endif
BuildRequires: libyubikey-devel
BuildRequires: systemd
BuildRequires: gcc
BuildRequires: make

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
# --disable-rpath doesn't work for the configure script
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%check
export LD_LIBRARY_PATH=$RPM_BUILD_DIR/%{name}-%{version}/.libs
make check

%install
%make_install INSTALL="%{__install} -p"

%files
%license COPYING
%doc AUTHORS README ChangeLog NEWS
%doc doc/Compatibility.asciidoc
%{_bindir}/ykinfo
%{_bindir}/ykpersonalize
%{_bindir}/ykchalresp
%{_libdir}/libykpers-1.so.1
%{_libdir}/libykpers-1.so.%{version}
%{_mandir}/man1/ykpersonalize.1*
%{_mandir}/man1/ykchalresp.1*
%{_mandir}/man1/ykinfo.1*
%{_udevrulesdir}/69-yubikey.rules

%files devel
%doc doc/USB-Hid-Issue.asciidoc
%{_libdir}/pkgconfig/ykpers-1.pc
%{_libdir}/libykpers-1.so
%{_includedir}/ykpers-1/
%exclude %{_libdir}/libykpers-1.la

%changelog
%autochangelog
