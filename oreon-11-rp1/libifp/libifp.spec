%global source0_hash 3b8fa50b9425b660285484eb42bad3f736f0aecc6a790c5160da276558ebfcee
%global build_type_safety_c 2
Name:           libifp
Version:        1.0.0.2
Release:        1%{?dist}
Summary:        General-purpose library-driver for iRiver's iFP portable audio players
License:        GPL-2.0-only
URL:            http://ifp-driver.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/ifp-driver/%{name}/%{version}-stable/%{name}-%{version}.tar.gz
Patch:          libifp-1.0.0.2-fix-broken-configure.in.diff
Patch:          libifp-1.0.0.2-fix-broken-configure-again.diff
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
libifp is a general-purpose library-driver for iRiver's iFP (flash-based)
portable audio players. The source code is pure C and is fairly portable.

Also included is a console app that uses the library.

%package        devel
Summary:        Headers and libraries for developing with libifp
Requires:       %{name} = %{version}-%{release}
%description    devel
This package contains headers and libraries for developing apps that use
libifp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fiv
%configure --with-libusb --disable-static
%make_build
%install
%make_install
install -Dpm 0755 %{SOURCE1} %{buildroot}/sbin/libifp-hotplug
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_udevrulesdir}/10-libifp.rules
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libifp-devel -f %{oreon_filedir}/libifp-devel.list

%changelog

%autochangelog
