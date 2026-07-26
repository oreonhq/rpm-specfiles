%global source0_hash 8fcab0bf3b39cd8a94fe3ee7a8264c6000515a3af377da3416696609ab13316d

Name:              netatalk
Epoch:             5
Version:           4.4.1
Release:           1%{?dist}
Summary:           Open Source Apple Filing Protocol(AFP) File Server
# Automatically converted from old format: GPL+ and GPLv2 and GPLv2+ and LGPLv2+ and BSD and FSFUL and MIT - review is highly recommended.
License:           GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD AND FSFUL AND LicenseRef-Callaway-MIT
# Project is also mirrored at https://github.com/Netatalk/Netatalk
URL:               http://netatalk.sourceforge.net
Source0:           https://download.sourceforge.net/netatalk/netatalk-%{version}.tar.xz
Source1:           netatalk.pam-system-auth

Patch0:            netatalk-AfpErr2name.patch

# Per i686 leaf package policy 
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:     avahi-devel
BuildRequires:     bison
BuildRequires:     bstring-devel
BuildRequires:     coreutils
BuildRequires:     cracklib-devel
BuildRequires:     dbus-devel
BuildRequires:     dbus-glib-devel
BuildRequires:     findutils
BuildRequires:     flex
BuildRequires:     gcc
BuildRequires:     grep
BuildRequires:     iniparser-devel
BuildRequires:     krb5-devel
BuildRequires:     libacl-devel
BuildRequires:     libattr-devel
BuildRequires:     libdb-devel
BuildRequires:     libevent-devel
BuildRequires:     libgcrypt-devel
BuildRequires:     libretls-devel
BuildRequires:     libtalloc-devel
BuildRequires:     libtdb-devel
BuildRequires:     libxcrypt-devel
BuildRequires:     mariadb-connector-c-devel
BuildRequires:     meson
BuildRequires:     openldap-devel
BuildRequires:     openssl-devel
BuildRequires:     pam-devel
BuildRequires:     pandoc
BuildRequires:     perl-generators
BuildRequires:     perl-interpreter
BuildRequires:     procps
BuildRequires:     procps-ng
BuildRequires:     quota-devel
BuildRequires:     rpm
BuildRequires:     sed
BuildRequires:     systemd
BuildRequires:     systemtap-sdt-devel
BuildRequires:     localsearch
BuildRequires:     tinysparql-devel
BuildRequires:     cups-devel

Requires:     dconf
Requires:     python3-dbus
%{?systemd_requires}

# Netatalk /usr/bin/dbd binary conflicts with binary of the same name in jday package
Conflicts: jday

%description
Netatalk is a freely-available Open Source AFP file server. A *NIX/*BSD
system running Netatalk is capable of serving many Macintosh clients
simultaneously as an AppleShare file server (AFP).

In addition to the AFP file server daemon, the following utility programs
are also included:
 * ad          - AppleDouble file utility suite
 * afpldaptest - validate Netatalk LDAP parameters
 * afppasswd   - RandNum UAM password management
 * afpstats    - inquire AFP server usage stats
 * asip-status - inquire AFP server capabilities
 * dbd         - CNID database maintenance
 * macusers    - list connected AFP server users

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%package        afptest
Summary:        Afp test suite for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    afptest
Apple Filing Protocol service test tools.

This package contains the following AFP functional test runners,
benchmarks, and supporting tools:
 * afp_lantest   - AFP benchmark akin to HELIOS LanTest
 * afp_logintest - test authentication over DSI
 * afp_spectest  - AFP specification functional test suite
 * afp_speedtest - AFP read/write/copy benchmark
 * afparg        - AFP CLI client
 * fce_listen    - listener for Netatalk's Filesystem Change Event protocol

%if 0%{?fedora}
# The following subpackage needs the appletalk module, which is part of kernel-modules-extra
# Unfortunately, the appletalk module is only available in Fedora
%package        appletalk
Summary:        Appletalk support for classic macintoshes
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       kernel-modules-extra

%description    appletalk
This package contains Netatalk's services and tools for networking
with very old Macs and Apple IIs.

This package contains the daemon and utility programs
for the Netatalk AppleTalk network suite, which can be used
with the Netatalk AFP file server, and other services.

In addition to the atalkd network management daemon,
the following utility programs are installed:
 * aecho      - send AppleTalk Echo Protocol pings
 * getzones   - list available AppleTalk zones
 * nbplkup    - list registered AppleTalk entities
 * nbprgstr   - register an AppleTalk entity
 * nbpunrgstr - release a registered AppleTalk entity
 * a2boot     - allows you to boot an Apple II over the network
                from an AFP volume
 * macipgw    - MacIP gateway which enables pre-TCP/IP Macs to browse the web
                and use other TCP/IP resources
 * papd       - allows Mac OS and Apple II clients to print to modern
                AirPrint / CUPS enabled printers
 * pap        - print from the host to a LocalTalk printer
 * papstatus  - inquire the status of a LocalTalk printer
 * timelord   - time server for Mac OS and Apple II
%endif

%package doc
Summary:        HTML Documentation for %{name}
BuildArch:      noarch

%description doc
Netatalk is a freely-available Open Source AFP file server. A *NIX/*BSD
system running Netatalk is capable of serving many Macintosh clients
simultaneously as an AppleShare file server (AFP).

This package contains the HTML documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

# Remove bundled bstring
rm -rf subprojects/bstring-*

# Don't build the japanese docs
sed -i 's\install: true\install: false\' doc/translated/ja/meson.build

# Set RuntimeDirectory in the relevant service files rather than use a tmpfiles.d config
for servicename in atalkd netatalk papd; do
  sed -E -i 's|^(PIDFile=.*)|RuntimeDirectory=lock/netatalk\nRuntimeDirectoryPreserve=yes\n\1|' distrib/initscripts/systemd.${servicename}.service.in
done

%build
%meson \
        --localstatedir=%{_localstatedir}/lib                                  \
        -Ddefault_library=shared                                               \
        -Dwith-rpath=false                                                     \
        -Dwith-overwrite=true                                                  \
        -Dwith-lockfile-path=%{_rundir}/lock/netatalk                          \
        -Dwith-tcp-wrappers=false                                              \
        -Dwith-dbus-sysconf-path=%{_sysconfdir}/dbus-1/system.d                \
        -Dwith-pkgconfdir-path=%{_sysconfdir}/netatalk                         \
        -Dwith-init-style=systemd                                              \
        -Dwith-init-hooks=false                                                \
        -Dwith-uams-path=%{_libdir}/netatalk                                   \
        -Dwith-cups=true                                                       \
        -Dwith-tests=true                                                      \
        -Dwith-testsuite=true                                                  \
        %{?fedora:-Dwith-appletalk=true}

%meson_build

%install
%meson_install

# Use specific pam conf.
install -Dpm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/netatalk

# Bundled pam config gets installed into non-standard folder. 
# Remove the bundled pam config and it parent folders as we supply our own pam config
rm -rf %{buildroot}%{_prefix}%{_sysconfdir}

# make sure all static libraries are deleted
find %{buildroot} \( -name '*.la' -o -name '*.a' \) -type f -delete -print

# Remove documentation files not relevant to rpm packaging
rm -rf %{buildroot}%{_pkgdocdir}/COMPILATION.txt
rm -rf %{buildroot}%{_pkgdocdir}/DOCKER.txt

%check
%meson_test

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%if 0%{?fedora}
%post appletalk
%systemd_post a2boot.service atalkd.service macipgw.service papd.service timelord.service

%preun appletalk
%systemd_preun a2boot.service atalkd.service macipgw.service papd.service timelord.service

%postun appletalk
%systemd_postun_with_restart a2boot.service atalkd.service macipgw.service papd.service timelord.service
%endif

%files
%license COPYING COPYRIGHT
%doc CONTRIBUTORS.txt NEWS.txt INSTALL.txt README.txt SECURITY.txt CODE_OF_CONDUCT.txt

%dir %{_sysconfdir}/netatalk
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/netatalk-dbus.conf
%config(noreplace) %{_sysconfdir}/netatalk/afp.conf
%config(noreplace) %{_sysconfdir}/netatalk/dbus-session.conf
%config(noreplace) %{_sysconfdir}/netatalk/extmap.conf
%config(noreplace) %{_sysconfdir}/pam.d/netatalk

%{_sbindir}/afpd
%{_sbindir}/cnid_dbd
%{_sbindir}/cnid_metad
%{_sbindir}/netatalk

%{_bindir}/nad
%{_bindir}/afpldaptest
%{_bindir}/afppasswd
%{_bindir}/afpstats
%{_bindir}/addump
%{_bindir}/asip-status
%{_bindir}/dbd
%{_bindir}/macusers

%dir %{_libdir}/netatalk
%{_libdir}/netatalk/uams_*.so
%{_libdir}/libatalk.so.19{,.*}

%{_mandir}/man1/nad.1*
%{_mandir}/man1/afpldaptest.1*
%{_mandir}/man1/afppasswd.1*
%{_mandir}/man1/afpstats.1*
%{_mandir}/man1/addump.1*
%{_mandir}/man1/asip-status.1*
%{_mandir}/man1/dbd.1*
%{_mandir}/man1/macusers.1*

%{_mandir}/man5/afp.conf.5*
%{_mandir}/man5/afp_signature.conf.5*
%{_mandir}/man5/afp_voluuid.conf.5*
%{_mandir}/man5/extmap.conf.5*

%{_mandir}/man8/afpd.8*
%{_mandir}/man8/cnid_dbd.8*
%{_mandir}/man8/cnid_metad.8*
%{_mandir}/man8/netatalk.8*

%{_unitdir}/netatalk.service

%{_localstatedir}/lib/netatalk

%files devel
%doc %{_pkgdocdir}/CONTRIBUTING.txt
%dir %{_includedir}/atalk
%{_includedir}/atalk/*.h
%{_libdir}/libatalk.so

%if 0%{?fedora}
%dir %{_includedir}/netatalk
%{_includedir}/netatalk/*.h
%endif

%{_mandir}/man3/atalk_aton.3*
%{_mandir}/man3/nbp_name.3*

%{_mandir}/man4/atalk.4*

%files afptest
%license test/testsuite/COPYING
%{_bindir}/afp_lantest
%{_bindir}/afp_logintest
%{_bindir}/afp_spectest
%{_bindir}/afp_speedtest
%{_bindir}/afparg
%{_bindir}/fce_listen

%dir %{_datarootdir}/netatalk
%{_datarootdir}/netatalk/test-data/test431_data

%{_mandir}/man1/afp_lantest.1*
%{_mandir}/man1/afp_logintest.1*
%{_mandir}/man1/afp_spectest.1*
%{_mandir}/man1/afp_speedtest.1*
%{_mandir}/man1/afptest.1*
%{_mandir}/man1/afparg.1*
%{_mandir}/man1/fce_listen.1*

%if 0%{?fedora}
%files appletalk
%config(noreplace) %{_sysconfdir}/netatalk/atalkd.conf
%config(noreplace) %{_sysconfdir}/netatalk/macipgw.conf
%config(noreplace) %{_sysconfdir}/netatalk/papd.conf

%{_sbindir}/a2boot
%{_sbindir}/atalkd
%{_sbindir}/macipgw
%{_sbindir}/papd
%{_sbindir}/timelord

%{_bindir}/aecho
%{_bindir}/getzones
%{_bindir}/nbplkup
%{_bindir}/nbprgstr
%{_bindir}/nbpunrgstr
%{_bindir}/pap
%{_bindir}/papstatus
%{_bindir}/rtmpqry

%{_mandir}/man1/aecho.1*
%{_mandir}/man1/getzones.1*
%{_mandir}/man1/nbplkup.1*
%{_mandir}/man1/nbp.1*
%{_mandir}/man1/nbprgstr.1*
%{_mandir}/man1/nbpunrgstr.1*
%{_mandir}/man1/pap.1*
%{_mandir}/man1/rtmpqry.1*

%{_mandir}/man5/atalkd.conf.5*
%{_mandir}/man5/macipgw.conf.5*
%{_mandir}/man5/papd.conf.5*

%{_mandir}/man8/a2boot.8*
%{_mandir}/man8/atalkd.8*
%{_mandir}/man8/macipgw.8*
%{_mandir}/man8/papd.8*
%{_mandir}/man8/papstatus.8*
%{_mandir}/man8/timelord.8*

%{_unitdir}/a2boot.service
%{_unitdir}/atalkd.service
%{_unitdir}/macipgw.service
%{_unitdir}/papd.service
%{_unitdir}/timelord.service
%endif

%files doc
%license COPYING COPYRIGHT
%doc %{_pkgdocdir}/manual

%changelog
%autochangelog
