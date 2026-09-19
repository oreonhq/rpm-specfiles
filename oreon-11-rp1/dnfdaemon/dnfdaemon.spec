%global source0_hash a276fa5180559fb1c0712f0bb44309eb22580288aaaf3f58b0b3e102ca2d4cc1

%global dnf_org org.baseurl.Dnf
%global dnf_version 4.2.6

Name:           dnfdaemon
Version:        0.3.22
Release:        11%{?dist}
Summary:        DBus daemon for dnf package actions

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/manatools/%{name}
Source0:        %{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  systemd

Requires:       python3-gobject
Requires:       python3-dbus
Requires:       python3-dnf >= %{dnf_version}
Requires:       polkit

%{?systemd_requires}

%description
Dbus daemon for performing package actions with the dnf package manager

%package selinux
Summary:        SELinux integration for the dnf-daemon

Requires:       %{name} = %{version}-%{release}

Requires(post):   policycoreutils-python-utils
Requires(postun): policycoreutils-python-utils

# http://rpm.org/user_doc/boolean_dependencies.html#cautionary-tale-about-if
Supplements:    (dnfdaemon and selinux-policy)

%description selinux
Metapackage customizing the SELinux policy to make the dnf-daemon work with
SELinux enabled in enforcing mode.

%package -n python3-%{name}
Summary:        Python 3 api for communicating with the dnf-daemon DBus service

BuildRequires:  python3-devel
BuildRequires: make

Requires:       %{name} = %{version}-%{release}
Requires:       python3-gobject

%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Python 3 api for communicating with the dnf-daemon DBus service

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# Nothing to build

%install
%make_install DATADIR=%{_datadir} SYSCONFDIR=%{_datadir}

%post
%systemd_post %{name}.service

%postun
%systemd_postun %{name}.service

%preun
%systemd_preun %{name}.service

%post selinux
# apply the right selinux file context
# http://fedoraproject.org/wiki/PackagingDrafts/SELinux#File_contexts
semanage fcontext -a -t rpm_exec_t '%{_datadir}/%{name}/%{name}-system' 2>/dev/null || :
restorecon -R %{_datadir}/%{name}/%{name}-system || :

%postun selinux
if [ $1 -eq 0 ] ; then  # final removal
semanage fcontext -d -t rpm_exec_t '%{_datadir}/%{name}/%{name}-system' 2>/dev/null || :
fi

%files
%license COPYING
%doc README.md ChangeLog
%{_datadir}/dbus-1/system-services/%{dnf_org}*
%{_datadir}/dbus-1/services/%{dnf_org}*
%{_datadir}/%{name}/
%{_unitdir}/%{name}.service
%{_datadir}/polkit-1/actions/%{dnf_org}*
%{_datadir}/dbus-1/system.d/%{dnf_org}*
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/__*
%{python3_sitelib}/%{name}/server

%files selinux
# empty metapackage

%files -n  python3-%{name}
%{python3_sitelib}/%{name}/client

%changelog
%autochangelog
