%global source0_hash daf00b183d9ad842eaafc7f8981f73e6e33ae9e1cb3f0e9a2cb7fbf030c36356
%global with_selinux 1
%global selinuxtype targeted
%global modulename adcli
Name:    adcli
Version: 0.9.3.1
Release:        1%{?dist}
Summary:        Active Directory enrollment
License: LGPL-2.1-or-later
URL:     https://gitlab.freedesktop.org/realmd/adcli
Source0:        https://gitlab.freedesktop.org/-/project/1196/uploads/5a1c55410c0965835b81fbd28d820d46/adcli-%{version}.tar.gz
Patch1: 0001-enroll-fix-issues-if-default-keytab-is-used.patch
%if %{with selinux}
%endif
Requires: cyrus-sasl-gssapi
Conflicts: adcli-doc < %{version}-%{release}
Obsoletes: adcli-devel < 0.5
%if %{with selinux}
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  krb5-devel
BuildRequires:  libnetapi-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  xmlto
# /oreon:deps
%description
adcli is a tool for joining an Active Directory domain using
standard LDAP and Kerberos calls.

%if %{with selinux}
# SELinux subpackage
%package selinux
Summary:             The adcli SELinux policy
BuildArch:           noarch
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
%{?selinux_requires_min}
%description selinux
Custom SELinux policy module for adcli to make sure generated Kerberos keytab
files have the right SELinux context.
%endif

%define _hardened_build 1

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf --force --install --verbose
%configure --disable-static --disable-silent-rules \
    %{nil}
%make_build
%check

make check
%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles adcli-selinux usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles adcli-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with selinux}
%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi
%posttrans selinux

%selinux_relabel_post -s %{selinuxtype}
%endif
%package doc
Summary: The adcli documentation package
BuildArch: noarch
Conflicts: adcli < %{version}-%{release}
%description doc
adcli is a tool for joining an Active Directory domain using
standard LDAP and Kerberos calls. This package contains its
documentation.

%files -f %{oreon_filedir}/main.list
%files -n adcli-selinux -f %{oreon_filedir}/adcli-selinux.list
%files -n adcli-doc -f %{oreon_filedir}/adcli-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.3.1-5
- Prepare for Oreon 11 (RP1)
