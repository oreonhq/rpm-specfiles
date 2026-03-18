Name:    realmd
Version: 0.17.1
Release: 19%{?dist}
Summary: Kerberos realm enrollment service
License: LGPL-2.1-or-later
URL:     https://gitlab.freedesktop.org/realmd/realmd
Source0: https://gitlab.freedesktop.org/realmd/realmd/uploads/204d05bd487908ece2ce2705a01d2b26/realmd-%{version}.tar.gz

Patch0001: 0001-service-allow-multiple-names-and-_srv_-ad_server-opt.patch
Patch0002: 0002-service-fix-error-message-when-removing-host-from-AD.patch
Patch0003: 0003-doc-fix-reference-in-realmd.conf-man-page.patch
Patch0004: 0001-sssd-package-fix.patch
Patch0005: 0001-tools-fix-ccache-handling-for-leave-operation.patch
Patch0006: 0001-ipa-Propagate-hostname-error.patch
Patch0007: 0001-configure.ac-Install-dbus-policy-in-usr-share-not-et.patch
Patch0008: 0001-Systemd-security-settings.patch
Patch0009: 0002-Disable-NoNewPrivileges-in-Systemd-service.patch
Patch0010: 0003-service-use-dnshostname-with-net-ads-join.patch
Patch0011: 0004-systemd-set-CacheDirectory.patch
Patch0012: 0005-Various-fixes-for-issues-found-by-static-code-scanne.patch
Patch0013: 0006-krb5-add-realm_krb5_get_error_message.patch
Patch0014: 0001-Initial-implementation-of-a-renew-request.patch
Patch0015: 0002-renew-implement-support-for-adcli.patch
Patch0016: 0003-service-use-proper-macro-for-os-name-and-os-version.patch
Patch0017: 0004-renew-fix-issues-found-by-Coverity.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: intltool pkgconfig
BuildRequires: gettext-devel
BuildRequires: glib2-devel >= 2.32.0
BuildRequires: openldap-devel
BuildRequires: polkit-devel
BuildRequires: krb5-devel
BuildRequires: systemd-devel
BuildRequires: libxslt
BuildRequires: xmlto
BuildRequires: python3
BuildRequires: samba-common-tools

Requires: authselect
Requires: polkit
Conflicts: realmd-devel-docs < %{version}-%{release}

%description
realmd is a DBus system service which manages discovery and enrollment in realms
and domains like Active Directory or IPA. The control center uses realmd as the
back end to 'join' a domain simply and automatically configure things correctly.

%package devel-docs
Summary: Developer documentation files for %{name}
Conflicts: realmd < %{version}-%{release}

%description devel-docs
The %{name}-devel package contains developer documentation for developing
applications that use %{name}.

%define _hardened_build 1

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-silent-rules \
%if 0%{?rhel}
    --with-vendor-error-message='Please check\n    https://red.ht/support_rhel_ad \nto get help for common issues.' \
%endif
    %{nil}

%make_build

%check
make check

%install
%make_install

%find_lang realmd

%post
%systemd_post realmd.service

%preun
%systemd_preun realmd.service

%postun
%systemd_postun_with_restart realmd.service

%files -f realmd.lang
%doc AUTHORS COPYING NEWS README
%{_datadir}/dbus-1/system.d/org.freedesktop.realmd.conf
%{_sbindir}/realm
%dir %{_prefix}/lib/realmd
%{_libexecdir}/realmd
%{_prefix}/lib/realmd/realmd-defaults.conf
%{_prefix}/lib/realmd/realmd-distro.conf
%{_unitdir}/realmd.service
%{_datadir}/dbus-1/system-services/org.freedesktop.realmd.service
%{_datadir}/polkit-1/actions/org.freedesktop.realmd.policy
%{_mandir}/man8/realm.8.gz
%{_mandir}/man5/realmd.conf.5.gz
%{_localstatedir}/cache/realmd/

%files devel-docs
%doc %{_datadir}/doc/realmd/
%doc ChangeLog

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.17.1-19
- Prepare for Oreon 11 (RP1)
