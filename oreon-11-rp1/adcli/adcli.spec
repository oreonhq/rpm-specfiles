%global source0_hash daf00b183d9ad842eaafc7f8981f73e6e33ae9e1cb3f0e9a2cb7fbf030c36356

%global with_selinux 1
%global selinuxtype targeted
%global modulename adcli

Name:    adcli
Version: 0.9.3.1
Release: 5%{?dist}
Summary: Active Directory enrollment
License: LGPL-2.1-or-later
URL:     https://gitlab.freedesktop.org/realmd/adcli
Source0:        https://gitlab.freedesktop.org/-/project/1196/uploads/5a1c55410c0965835b81fbd28d820d46/adcli-%{version}.tar.gz

Patch1: 0001-enroll-fix-issues-if-default-keytab-is-used.patch

BuildRequires: gcc
BuildRequires: intltool pkgconfig
BuildRequires: libtool
BuildRequires: gettext-devel
BuildRequires: krb5-devel
BuildRequires: openldap-devel
BuildRequires: libxslt
BuildRequires: xmlto
BuildRequires: make
BuildRequires: libnetapi-devel

# Build dependencies for SELinux policy
%if %{with selinux}
BuildRequires:  libselinux-devel
BuildRequires:  selinux-policy-devel
%endif

Requires: cyrus-sasl-gssapi
Conflicts: adcli-doc < %{version}-%{release}

# adcli no longer has a library of development files
# the adcli tool itself is to be used by callers
Obsoletes: adcli-devel < 0.5

%if %{with selinux}
# This ensures that the *-selinux package and all it’s dependencies are not
# pulled into containers and other systems that do not use SELinux. The
# policy defines types and file contexts for client and server.
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
autoreconf --force --install --verbose
%configure --disable-static --disable-silent-rules \
%if 0%{?rhel}
    --with-vendor-error-message='Please check\n    https://red.ht/support_rhel_ad \nto get help for common issues.' \
%endif
    %{nil}
%make_build

%check
make check

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%if %{with selinux}
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
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

%files
%{_sbindir}/adcli
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_mandir}/*/*

%package doc
Summary: The adcli documentation package
BuildArch: noarch
Conflicts: adcli < %{version}-%{release}

%description doc
adcli is a tool for joining an Active Directory domain using
standard LDAP and Kerberos calls. This package contains its
documentation.

%files doc
%doc %{_datadir}/doc/adcli/*

%if %{with selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp
%ghost %verify(not md5 size mode mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.3.1-5
- Prepare for Oreon 11 (RP1)
