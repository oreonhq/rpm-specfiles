%global source0_hash c615df68e6e521a8d5035c2ed9d9315b3f7b4f6437fa0922799f565ea25518c7
%undefine __cmake_in_source_build
%bcond_without tests
Name:           gammu
Version:        1.45.0
Release:        1%{?dist}
Summary:        Command Line utility to work with mobile phones
License:        GPL-2.0-or-later
URL:            http://wammu.eu/gammu/
Source0:        https://github.com/gammu/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         gammu-1.3.7-udev.patch
Patch1:         a37e5d8054f863fa71e38e244dd4da13eee6e251.patch
%ifnarch s390 s390x
%endif
%{?systemd_requires}
Requires:       bluez
Requires:       dialog
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  bash-completion
BuildRequires:  bluez-libs-devel
BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgudev1-devel
BuildRequires:  libpq-devel
BuildRequires:  libusb1-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  unixODBC-devel
# /oreon:deps
%package    libs
Summary:    Libraries files for %{name}
%package    devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}
Requires:   pkgconfig
%description
Gammu is command line utility and library to work with mobile phones
from many vendors. Support for different models differs, but basic
functions should work with majority of them. Program can work with
contacts, messages (SMS, EMS and MMS), calendar, todos, filesystem,
integrated radio, camera, etc. It also supports daemon mode to send and
receive SMSes.

Currently supported phones include:

* Many Nokia models.
* Alcatel BE5 (501/701), BF5 (715), BH4 (535/735).
* AT capable phones (Siemens, Nokia, Alcatel, IPAQ).
* OBEX and IrMC capable phones (Sony-Ericsson, Motorola).
* Symbian phones through gnapplet.

This package contains Gammu binary as well as some examples.

%description    libs
The %{name}-libs package contains libraries files that used by %{name}

%description    devel
The %{name}-devel  package contains Header and libraries files for
developing applications that use %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .udev
%patch -P1 -p1

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake3                  \
    -DENABLE_BACKUP=ON      \
    -DWITH_NOKIA_SUPPORT=ON     \
    -DWITH_Bluez=ON         \
    -DWITH_IrDA=ON          \
    -DINSTALL_UDEV_RULES=ON \
    -DINSTALL_GNAPPLET=ON       \
    -DINSTALL_MEDIA=ON       \
    -DINSTALL_PHP_EXAMPLES=ON       \
    -DINSTALL_BASH_COMPLETION=ON       \
    -DINSTALL_DOC=ON       \
    -DINSTALL_LOC=ON       \
    -DBUILD_SHARED_LIBS=ON \
    -DINSTALL_UDEV_RULES=ON \
    -DSYSTEMD_FOUND=ON \
    -DWITH_SYSTEMD=ON \
    -DSYSTEMD_SERVICES_INSTALL_DIR=%{_unitdir} \
    ../
%cmake_build
%install
%cmake_install
install -d %{buildroot}%{_sysconfdir}
install -pm 0644 docs/config/smsdrc %{buildroot}%{_sysconfdir}/gammu-smsdrc
%find_lang %{name}
%find_lang lib%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if %{with tests}
%global _smp_mflags %{nil}
%ctest3
%endif
%post

%systemd_post gammu-smsd.service
%preun

%systemd_preun gammu-smsd.service
%postun

%systemd_postun_with_restart gammu-smsd.service
%ldconfig_scriptlets -n %{name}-libs
%files -f %{oreon_filedir}/main.list
%files -n gammu-libs -f %{oreon_filedir}/gammu-libs.list
%files -n gammu-devel -f %{oreon_filedir}/gammu-devel.list

%changelog

%autochangelog
