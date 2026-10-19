%global source0_hash 28a3a521782063c8eb2ee5f4c0f38a517e023853edb55856052cdd7ac400381b
Name:           libirecovery
Version:        1.3.1
Release:        1%{?dist}
Summary:        Library and utility to talk to iBoot/iBSS via USB
License:        LGPL-2.1-only
URL:            https://github.com/libimobiledevice/libirecovery
Source0:        https://github.com/libimobiledevice/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libimobiledevice-glue-devel
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  readline-devel
BuildRequires:  systemd-devel
# /oreon:deps
%description
The libirecovery library allows communication with iBoot/iBSS of iOS devices
via USB.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        utils
Summary:        Utilites for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Suggests:       libimobiledevice-utils
%description    utils
This package contains command line utilities for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static --with-udev
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libirecovery-devel -f %{oreon_filedir}/libirecovery-devel.list
%files -n libirecovery-utils -f %{oreon_filedir}/libirecovery-utils.list

%changelog

%autochangelog
