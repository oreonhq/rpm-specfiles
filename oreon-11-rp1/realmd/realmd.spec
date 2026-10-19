%global source0_hash 2eb12cc6e023c3dd1e2691b893f9841f0a679ba3feb3c8d0bc71891424ebec5f
Name:    realmd
Version: 0.17.1
Release:        19%{?dist}
Summary:        Kerberos realm enrollment service
License: LGPL-2.1-or-later
URL:     https://gitlab.freedesktop.org/realmd/realmd
Source0:        https://gitlab.freedesktop.org/realmd/realmd/uploads/204d05bd487908ece2ce2705a01d2b26/realmd-%{version}.tar.gz
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
Requires: authselect
Requires: polkit
Conflicts: realmd-devel-docs < %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  krb5-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  pkgconfig
BuildRequires:  polkit-devel
BuildRequires:  python3
BuildRequires:  samba-common-tools
BuildRequires:  systemd-devel
BuildRequires:  xmlto
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fi
%configure --disable-silent-rules \
    %{nil}
%make_build
%check

make check
%install
%make_install
%find_lang realmd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post realmd.service
%preun

%systemd_preun realmd.service
%postun

%systemd_postun_with_restart realmd.service
%files -f %{oreon_filedir}/main.list
%files -n realmd-devel-docs -f %{oreon_filedir}/realmd-devel-docs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.17.1-19
- Prepare for Oreon 11 (RP1)
