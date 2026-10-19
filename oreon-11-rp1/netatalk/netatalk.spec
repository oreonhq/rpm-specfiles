%global source0_hash f091de10b0c40996ebf7d6502cf947cfd87dfe1a7e62f9d96013225573938524
Name:              netatalk
Epoch:             5
Version:           4.5.1
Release:        1%{?dist}
Summary:        Open Source Apple Filing Protocol(AFP) File Server
License:           GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD AND FSFUL AND LicenseRef-Callaway-MIT
URL:               http://netatalk.sourceforge.net
Source0:        https://download.sourceforge.net/netatalk/netatalk-%{version}.tar.xz
Source1:           netatalk.pam-system-auth
Patch0:            netatalk-AfpErr2name.patch
ExcludeArch: %{ix86}
Requires:     dconf
Requires:     python3-dbus
%{?systemd_requires}
Conflicts: jday
# oreon:deps
BuildRequires:  avahi-devel
BuildRequires:  bison
BuildRequires:  bstring-devel
BuildRequires:  coreutils
BuildRequires:  cracklib-devel
BuildRequires:  cups-devel
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  findutils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  grep
BuildRequires:  iniparser-devel
BuildRequires:  krb5-devel
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libdb-devel
BuildRequires:  libevent-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libretls-devel
BuildRequires:  libtalloc-devel
BuildRequires:  libtdb-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  localsearch
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  meson
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pandoc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  procps
BuildRequires:  procps-ng
BuildRequires:  quota-devel
BuildRequires:  rpm
BuildRequires:  sed
BuildRequires:  systemd
BuildRequires:  systemtap-sdt-devel
BuildRequires:  tinysparql-devel
# /oreon:deps
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
install -Dpm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/netatalk
rm -rf %{buildroot}%{_prefix}%{_sysconfdir}
find %{buildroot} \( -name '*.la' -o -name '*.a' \) -type f -delete -print
rm -rf %{buildroot}%{_pkgdocdir}/COMPILATION.txt
rm -rf %{buildroot}%{_pkgdocdir}/DOCKER.txt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n netatalk-devel -f %{oreon_filedir}/netatalk-devel.list
%files -n netatalk-afptest -f %{oreon_filedir}/netatalk-afptest.list
%files -n netatalk-doc -f %{oreon_filedir}/netatalk-doc.list

%changelog

%autochangelog
