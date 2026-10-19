%global source0_hash e16ce096161265fb6838a64e325015b0f79ffa9b920e79287d8cae488f37dab0
%global build_sample_subpackage 0
%global dbus_send /bin/dbus-send
Name: oddjob
Version: 0.34.7
Release:        18%{?dist}
Source0:        https://deb.debian.org/debian/pool/main/o/oddjob/oddjob_%{version}.orig.tar.gz#/oddjob-%{version}.tar.gz
Patch1: oddjob-override-mask-fix.patch
Patch2: oddjob-libxml2.patch
Summary:        A D-Bus service which runs odd jobs on behalf of client applications
License: BSD-3-Clause
Requires(post):	systemd-units
Requires(preun):	systemd-units
Requires(postun):	systemd-units
Requires(post):	systemd-sysv
Requires: dbus
Requires(post): psmisc
Obsoletes: oddjob-devel < 0.30, oddjob-libs < 0.30, oddjob-python < 0.30
URL: https://pagure.io/oddjob
# oreon:deps
BuildRequires:  cyrus-sasl-devel
BuildRequires:  dbus-devel
BuildRequires:  dbus-x11
BuildRequires:  docbook-dtds
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  libselinux-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-units
BuildRequires:  xmlto
# /oreon:deps
%description
oddjob is a D-Bus service which performs particular tasks for clients which
connect to it and issue requests using the system-wide message bus.

%package mkhomedir
Summary: An oddjob helper which creates and populates home directories
Requires: %{name} = %{version}-%{release}
Requires(post): %{dbus_send}, grep, sed, psmisc
%description mkhomedir
This package contains the oddjob helper which can be used by the
pam_oddjob_mkhomedir module to create a home directory for a user
at login-time.

%package sample
Summary: A sample oddjob service.
Requires: %{name} = %{version}-%{release}
%description sample
This package contains a trivial sample oddjob service.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P1 -p1
%patch -P2 -p1

%build

sample_flag=
%configure \
	--disable-static \
	--enable-pie --enable-now \
	--with-selinux-acls \
	--with-selinux-labels \
	--without-python --enable-xml-docs --enable-compat-dtd \
	--disable-dependency-tracking \
	--enable-systemd --disable-sysvinit \
	$sample_flag
make %{_smp_mflags}
%install
rm -fr "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"
rm -f "$RPM_BUILD_ROOT"/%{_libdir}/security/*.la
rm -f "$RPM_BUILD_ROOT"/%{_libdir}/security/*.a
rm -f "$RPM_BUILD_ROOT"/%{_libdir}/*.la
%if ! %{build_sample_subpackage}
mkdir -p sample-install-root/sample/{%{_sysconfdir}/{dbus-1/system.d,%{name}d.conf.d},%{_libdir}/%{name}}
install -m644 sample/oddjobd-sample.conf	sample-install-root/sample/%{_sysconfdir}/%{name}d.conf.d/
install -m644 sample/oddjob-sample.conf		sample-install-root/sample/%{_sysconfdir}/dbus-1/system.d/
install -m755 sample/oddjob-sample.sh		sample-install-root/sample/%{_libdir}/%{name}/
%endif
chmod -x src/reload src/mkhomedirfor src/mkmyhomedir
touch -r src/oddjobd-mkhomedir.conf.in	$RPM_BUILD_ROOT/%{_sysconfdir}/oddjobd.conf.d/oddjobd-mkhomedir.conf
touch -r src/oddjob-mkhomedir.conf.in	$RPM_BUILD_ROOT/%{_sysconfdir}/dbus-1/system.d/oddjob-mkhomedir.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post oddjobd.service
%postun

%systemd_postun_with_restart oddjobd.service
exit 0
%preun

%systemd_preun oddjobd.service
exit 0
%post mkhomedir

cfg=%{_sysconfdir}/oddjobd.conf.d/oddjobd-mkhomedir.conf
if grep -q %{_libdir}/%{name}/mkhomedir $cfg ; then
	sed -i 's^%{_libdir}/%{name}/mkhomedir^%{_libexecdir}/%{name}/mkhomedir^g' $cfg
fi
systemctl --quiet is-active oddjobd
isactive=$?
if test $isactive -eq 0 ; then
	%{dbus_send} --system --dest=com.redhat.oddjob /com/redhat/oddjob com.redhat.oddjob.reload
fi
exit 0
%files -f %{oreon_filedir}/main.list
%files -n oddjob-mkhomedir -f %{oreon_filedir}/oddjob-mkhomedir.list
%files -n oddjob-sample -f %{oreon_filedir}/oddjob-sample.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.34.7-18
- Prepare for Oreon 11 (RP1)
