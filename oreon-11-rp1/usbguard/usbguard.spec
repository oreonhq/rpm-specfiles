%global source0_hash 707dad2938923202697f636c2b4e0be80f192242039a2af3fc7ac35d03f78551
%global source1_hash bd70162b31f65497b2f5254cd287dbc1290c2c036ba0c2c8fa92fa8caca9dc71

%global selinuxtype targeted
%global moduletype contrib
%define semodule_version 0.0.5

Name:           usbguard
Version:        1.1.3
Release:        7%{?dist}
Summary:        A tool for implementing USB device usage policy
License:        GPL-2.0-or-later
## Not installed
# src/ThirdParty/Catch: Boost Software License - Version 1.0
URL:            https://usbguard.github.io/
Source0:        https://github.com/USBGuard/usbguard/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/USBGuard/usbguard-selinux/archive/refs/tags/v%{semodule_version}.tar.gz#/%{name}-selinux-%{semodule_version}.tar.gz
Source2:        usbguard-daemon.conf

Requires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Requires: (%{name}-selinux if selinux-policy-%{selinuxtype})
Obsoletes: %{name}-applet-qt < 0.7.6

BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libqb-devel
BuildRequires: libgcrypt-devel
BuildRequires: libstdc++-devel
BuildRequires: protobuf-devel protobuf-compiler
BuildRequires: PEGTL-static
BuildRequires: autoconf automake libtool
BuildRequires: bash-completion
BuildRequires: asciidoc
BuildRequires: audit-libs-devel
# For `pkg-config systemd` only
BuildRequires: systemd

Patch0: tmpfiles-v1.patch
Patch1: tmpfiles-v2.patch
Patch2: uninstall-ignore-error.patch
Patch3: ipc-privileges.patch
Patch4: protobuf-3.0.patch
Patch5: catch2-support.patch
Patch6: disable-catch.patch
Patch7: selinux-bin-sbin.patch

%description
The USBGuard software framework helps to protect your computer against rogue USB
devices by implementing basic whitelisting/blacklisting capabilities based on
USB device attributes.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       libstdc++-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        USBGuard Tools
Requires:       %{name} = %{version}-%{release}

%description    tools
The %{name}-tools package contains optional tools from the USBGuard
software framework.

# dbus
%package        dbus
Summary:        USBGuard D-Bus Service
Requires:       %{name} = %{version}-%{release}
BuildRequires:	dbus-devel
BuildRequires:	glib2-devel
BuildRequires:	polkit-devel
BuildRequires:	libxslt
BuildRequires:	libxml2
Requires:       dbus
Requires:       polkit

%description    dbus
The %{name}-dbus package contains an optional component that provides
a D-Bus interface to the USBGuard daemon component.

%package        selinux
Summary:        USBGuard selinux
Group:          Applications/System
Requires:       %{name} = %{version}-%{release}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
BuildArch: noarch
%{?selinux_requires}

%description    selinux
The %{name}-selinux package contains selinux policy for the USBGuard
daemon.

# usbguard
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q

# selinux
%setup -q -D -T -a 1

%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1

pushd %{name}-selinux-%{semodule_version}
%patch -P 7 -p1
popd

# Remove bundled library sources before build
rm -rf src/ThirdParty/{Catch,PEGTL}

%build
mkdir -p ./m4
autoreconf -i -v --no-recursive ./
%configure \
    --disable-silent-rules \
    --without-bundled-catch \
    --without-bundled-pegtl \
    --enable-systemd \
    --with-dbus \
    --with-polkit \
    --with-crypto-library=gcrypt \
    --disable-catch

make %{?_smp_mflags}

# selinux
pushd %{name}-selinux-%{semodule_version}
make
popd

# selinux
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%install
make install INSTALL='install -p' DESTDIR=%{buildroot}

# Overwrite configuration with distribution defaults
mkdir -p %{buildroot}%{_sysconfdir}/usbguard
mkdir -p %{buildroot}%{_sysconfdir}/usbguard/rules.d
mkdir -p %{buildroot}%{_sysconfdir}/usbguard/IPCAccessControl.d
install -p -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/usbguard/usbguard-daemon.conf

# selinux
install -d %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -m 0644 %{name}-selinux-%{semodule_version}/%{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -d -p %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}
install -p -m 644 %{name}-selinux-%{semodule_version}/%{name}.if %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}/ipp-%{name}.if

# Cleanup
find %{buildroot} \( -name '*.la' -o -name '*.a' \) -exec rm -f {} ';'

%preun
%systemd_preun usbguard.service

%post
%{?ldconfig}
%systemd_post usbguard.service

%postun
%{?ldconfig}
%systemd_postun usbguard.service

%files
%doc README.adoc CHANGELOG.md
%license LICENSE
%{_libdir}/*.so.*
%{_sbindir}/usbguard-daemon
%{_bindir}/usbguard
%dir %{_localstatedir}/log/usbguard
%dir %{_sysconfdir}/usbguard
%dir %{_sysconfdir}/usbguard/rules.d/
%dir %{_sysconfdir}/usbguard/IPCAccessControl.d
%config(noreplace) %attr(0600,-,-) %{_sysconfdir}/usbguard/usbguard-daemon.conf
%config(noreplace) %attr(0600,-,-) %{_sysconfdir}/usbguard/rules.conf
%{_unitdir}/usbguard.service
%{_datadir}/man/man8/usbguard-daemon.8.gz
%{_datadir}/man/man5/usbguard-daemon.conf.5.gz
%{_datadir}/man/man5/usbguard-rules.conf.5.gz
%{_datadir}/man/man1/usbguard.1.gz
%{_datadir}/bash-completion/completions/usbguard
%attr(640,root,root) %{_tmpfilesdir}/usbguard.conf

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files tools
%{_bindir}/usbguard-rule-parser

# dbus
%files dbus
%{_sbindir}/usbguard-dbus
%{_datadir}/dbus-1/system-services/org.usbguard1.service
%{_datadir}/dbus-1/system.d/org.usbguard1.conf
%{_datadir}/polkit-1/actions/org.usbguard1.policy
%{_unitdir}/usbguard-dbus.service
%{_mandir}/man8/usbguard-dbus.8.gz

%preun dbus
%systemd_preun usbguard-dbus.service

%post dbus
%systemd_post usbguard-dbus.service

%postun dbus
%systemd_postun_with_restart usbguard-dbus.service

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}
%{_datadir}/selinux/devel/include/%{moduletype}/ipp-%{name}.if

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-7
- Prepare for Oreon 11 (RP1)
