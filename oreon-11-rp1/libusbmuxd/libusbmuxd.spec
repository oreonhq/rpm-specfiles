%global source0_hash 5546f1aba1c3d1812c2b47d976312d00547d1044b84b6a461323c621f396efce
%global forgeurl https://github.com/libimobiledevice/libusbmuxd
Name:           libusbmuxd
Version:        2.1.1
Release:        1%{?dist}
Summary:        Client library USB multiplex daemon for Apple's iOS devices
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            https://www.libimobiledevice.org/
Source0:        %{forgeurl}/releases/download/%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libimobiledevice-glue-devel
BuildRequires:  libplist-devel
BuildRequires:  make
# /oreon:deps
%description
libusbmuxd is the client library used for communicating with Apple's iPod Touch,
iPhone, iPad and Apple TV devices. It allows multiple services on the device 
to be accessed simultaneously.

%package        utils
Summary:        Utilities for communicating with Apple's iOS devices
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    utils
Utilities for Apple's iOS devices

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Files for development with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
%make_build
%install
%make_install
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n libusbmuxd-utils -f %{oreon_filedir}/libusbmuxd-utils.list
%files -n libusbmuxd-devel -f %{oreon_filedir}/libusbmuxd-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.0-1
- Prepare for Oreon 11 (RP1)
