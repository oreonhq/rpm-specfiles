%global source0_hash 8f3a53a438b957c7fd3a587ae2d3134287b4c700fafe617069c10aa62224343a

%undefine __cmake_in_source_build
%bcond_without tests

Name:           gammu
Version:        1.42.0
Release:        21%{?dist}
Summary:        Command Line utility to work with mobile phones

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://wammu.eu/gammu/
Source0:        https://github.com/gammu/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         gammu-1.3.7-udev.patch
Patch1:         a37e5d8054f863fa71e38e244dd4da13eee6e251.patch

BuildRequires:  gcc
BuildRequires:  cmake3
BuildRequires:  autoconf
BuildRequires:  pkgconfig
BuildRequires:  gettext-devel
BuildRequires:  doxygen
%ifnarch s390 s390x
BuildRequires:  libusb1-devel
%endif
# Enabling bluetooth function
BuildRequires:  bluez-libs-devel
# Enabling Database sms function
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires:  postgresql-devel
BuildRequires:  mysql-devel
%else
BuildRequires:  libpq-devel
BuildRequires:  mariadb-connector-c-devel
%endif

%if 0%{?fedora}
BuildRequires:  libdbi-devel
%endif
BuildRequires:  unixODBC-devel
#for tests
%if 0%{?fedora}
BuildRequires:  libdbi-dbd-sqlite
%endif
BuildRequires:  libcurl-devel
BuildRequires:  glib2-devel
BuildREquires:  libgudev1-devel
%if 0%{?fedora} >= 41
BuildRequires:  bash-completion-devel
%else
BuildRequires:  bash-completion
%endif

%{?systemd_requires}
BuildRequires: systemd-rpm-macros

Requires:       bluez
Requires:       dialog
# drive sqlite is in use by default
%if 0%{?fedora}
Requires:       libdbi-dbd-sqlite
%endif
# we should force the exact EVR for an ISA - not only the same ABI
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

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
# TODO: Please submit an issue to upstream (rhbz#2380612)
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

# Install config file
install -d %{buildroot}%{_sysconfdir}
install -pm 0644 docs/config/smsdrc %{buildroot}%{_sysconfdir}/gammu-smsdrc

%find_lang %{name}
%find_lang lib%{name}

%check
%if %{with tests}
# add %%{?_smp_mflags} breaks the tests
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

%files -f %{name}.lang
%docdir %{_docdir}/%{name}
%{_docdir}/%{name}/README.rst
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/examples
%license %{_docdir}/%{name}/COPYING
%config(noreplace) %{_sysconfdir}/gammu-smsdrc
%{_bindir}/%{name}*
%{_bindir}/jadmaker
%{_mandir}/man1/*.gz
%{_mandir}/man5/*.gz
%{_mandir}/man7/*.gz
#{_mandir}/cs/man1/*.gz
#{_mandir}/cs/man5/*.gz
#{_mandir}/cs/man7/*.gz
%{bash_completions_dir}/%{name}
%{_unitdir}/gammu-smsd.service
%{_datadir}/%{name}
%{_udevrulesdir}/69-gammu-acl.rules
#{_udevrulesdir}/45-nokiadku2.rules

%files libs -f lib%{name}.lang
%{_libdir}/*.so.*

%files devel
%doc %{_docdir}/%{name}/manual
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}

%changelog
%autochangelog
