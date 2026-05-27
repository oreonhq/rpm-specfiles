%global source0_hash e16ce096161265fb6838a64e325015b0f79ffa9b920e79287d8cae488f37dab0

%global build_sample_subpackage 0

%if 0%{?fedora} > 21 || 0%{?rhel} > 7
%global dbus_send /usr/bin/dbus-send
%else
%global dbus_send /bin/dbus-send
%endif

Name: oddjob
Version: 0.34.7
Release: 18%{?dist}
Source0: https://releases.pagure.org/oddjob/oddjob-%{version}.tar.gz
Source1: https://releases.pagure.org/oddjob/oddjob-%{version}.tar.gz.asc
Patch1: oddjob-override-mask-fix.patch
# Fix build with libxml2-2.12.0
# https://pagure.io/oddjob/pull-request/24
Patch2: oddjob-libxml2.patch
Summary: A D-Bus service which runs odd jobs on behalf of client applications
License: BSD-3-Clause
BuildRequires: make
BuildRequires:  gcc
BuildRequires: dbus-devel >= 0.22, dbus-x11, libselinux-devel, libxml2-devel
BuildRequires: pam-devel, pkgconfig
BuildRequires: cyrus-sasl-devel, krb5-devel, openldap-devel
BuildRequires: docbook-dtds, xmlto
BuildRequires:	systemd-units
Requires(post):	systemd-units
Requires(preun):	systemd-units
Requires(postun):	systemd-units
Requires(post):	systemd-sysv
Requires: dbus
# for "killall"
Requires(post): psmisc
Obsoletes: oddjob-devel < 0.30, oddjob-libs < 0.30, oddjob-python < 0.30
URL: https://pagure.io/oddjob

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P1 -p1
%patch -P2 -p1

%build
sample_flag=
%if %{build_sample_subpackage}
sample_flag=--enable-sample
%endif
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
# Recommended, though I disagree.
rm -f "$RPM_BUILD_ROOT"/%{_libdir}/*.la

%if ! %{build_sample_subpackage}
# Go ahead and build the sample layout.
mkdir -p sample-install-root/sample/{%{_sysconfdir}/{dbus-1/system.d,%{name}d.conf.d},%{_libdir}/%{name}}
install -m644 sample/oddjobd-sample.conf	sample-install-root/sample/%{_sysconfdir}/%{name}d.conf.d/
install -m644 sample/oddjob-sample.conf		sample-install-root/sample/%{_sysconfdir}/dbus-1/system.d/
install -m755 sample/oddjob-sample.sh		sample-install-root/sample/%{_libdir}/%{name}/
%endif

# Make sure we don't needlessly make these docs executable.
chmod -x src/reload src/mkhomedirfor src/mkmyhomedir

# Make sure the datestamps match in multilib pairs.
touch -r src/oddjobd-mkhomedir.conf.in	$RPM_BUILD_ROOT/%{_sysconfdir}/oddjobd.conf.d/oddjobd-mkhomedir.conf
touch -r src/oddjob-mkhomedir.conf.in	$RPM_BUILD_ROOT/%{_sysconfdir}/dbus-1/system.d/oddjob-mkhomedir.conf

%files
%doc *.dtd NEWS QUICKSTART doc/oddjob.html src/reload
%license COPYING
%if ! %{build_sample_subpackage}
%doc sample-install-root/sample
%endif
%{_unitdir}/oddjobd.service
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/dbus-*/system.d/oddjob.conf
%config(noreplace) %{_sysconfdir}/oddjobd.conf
%dir %{_sysconfdir}/oddjobd.conf.d
%config(noreplace) %{_sysconfdir}/oddjobd.conf.d/oddjobd-introspection.conf
%dir %{_sysconfdir}/%{name}
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/sanity.sh
%{_mandir}/*/oddjob.*
%{_mandir}/*/oddjob_request.*
%{_mandir}/*/oddjobd.*
%{_mandir}/*/oddjobd-introspection.*

%files mkhomedir
%doc src/mkhomedirfor src/mkmyhomedir
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mkhomedir
%{_libdir}/security/pam_oddjob_mkhomedir.so
%{_mandir}/*/pam_oddjob_mkhomedir.*
%{_mandir}/*/oddjob-mkhomedir.*
%{_mandir}/*/oddjobd-mkhomedir.*
%config(noreplace) %{_sysconfdir}/dbus-*/system.d/oddjob-mkhomedir.conf
%config(noreplace) %{_sysconfdir}/oddjobd.conf.d/oddjobd-mkhomedir.conf

%if %{build_sample_subpackage}
%files sample
%{_libdir}/%{name}/oddjob-sample.sh
%config %{_sysconfdir}/dbus-*/system.d/oddjob-sample.conf
%config %{_sysconfdir}/oddjobd.conf.d/oddjobd-sample.conf
%endif

%post
%systemd_post oddjobd.service

%postun
%systemd_postun_with_restart oddjobd.service
exit 0

%preun
%systemd_preun oddjobd.service
exit 0

%post mkhomedir
# Adjust older configuration files that may have been modified so that they
# point to the current location of the helper.
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

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.34.7-18
- Prepare for Oreon 11 (RP1)
