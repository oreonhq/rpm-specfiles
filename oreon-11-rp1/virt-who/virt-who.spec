%global source0_hash 547b3e426674ec68b84ee47194f3a5c84c9c64ea632780bfa3b05d2ca6080f13

%define use_systemd (0%{?fedora} && 0%{?fedora} >= 18) || (0%{?rhel} && 0%{?rhel} >= 7)

%define use_python3 0%{?fedora} || (0%{?rhel} && 0%{?rhel} > 7)
%if %{use_python3}
%global python_ver python3
%global python_exec %{__python3}
%global python_sitelib %{python3_sitelib}
%else
%if !%{use_systemd}
%global __python2 %{__python}
%global python2_sitelib %{python_sitelib}
%endif
%global python_ver python
%global python_exec %{__python2}
%global python_sitelib %{python2_sitelib}
%endif
%global release_number 1

%global git_tag %{name}-%{version}-%{release_number}

Name:           virt-who
Version:        1.31.26
Release:        %{release_number}%{?dist}.11

Summary:        Agent for reporting virtual guest IDs to subscription-manager

Group:          System Environment/Base
# GPL for virt-who proper and LGPL for incorporated suds
License:        GPL-2.0-or-later AND LGPL-3.0-or-later
URL:            https://github.com/candlepin/virt-who
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{python_ver}-devel
BuildRequires:  %{python_ver}-setuptools
BuildRequires:  %{python_ver}-pyyaml

# libvirt python required for libvirt support
%if (0%{?rhel} && 0%{?rhel} > 7 || 0%{?fedora})
Requires:       %{python_ver}-libvirt
%else
Requires:       libvirt-python
%endif
# python-rhsm 1.20 has the M2Crypto wrappers needed to replace M2Crypto
# with the python standard libraries where plausible
%if %{use_python3}
Requires:       python3-subscription-manager-rhsm > 1.25.6
%else
Requires:       subscription-manager-rhsm > 1.25.6
%endif
# m2crypto OR python3-cryptography is required for Hyper-V support
%if %{use_python3}
Requires:       python3-cryptography
%else
Requires:       m2crypto
%endif
Requires:       %{python_ver}-requests
# python-argparse is required for Python 2.6 on EL6
%{?el6:Requires: python-argparse}
Requires:       openssl
Requires:       %{python_ver}-pyyaml

%if %{use_systemd}
%if %{use_python3}
Requires: python3-systemd
%else
Requires: systemd-python
%endif
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%else
Requires(post): chkconfig
Requires(preun): chkconfig
# This is for /sbin/service
Requires(preun): initscripts
%endif
Provides: bundled(python-suds) = 0.8.4

%description
Agent that collects information about virtual guests present in the system and
report them to the subscription manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%{python_exec} setup.py build --rpm-version=%{version}-%{release_number}

%install
rm -rf $RPM_BUILD_ROOT
%{python_exec} setup.py install --root %{buildroot}
%{python_exec} setup.py install_config --root %{buildroot}
%{python_exec} setup.py install_man_pages --root %{buildroot}
%if %{use_systemd}
%{python_exec} setup.py install_systemd --root %{buildroot}
%else
%{python_exec} setup.py install_upstart --root %{buildroot}
%endif

mkdir -p %{buildroot}/%{_sharedstatedir}/%{name}/
touch %{buildroot}/%{_sharedstatedir}/%{name}/key

mkdir -p %{buildroot}/%{_datadir}/zsh/site-functions
install -m 644 virt-who-zsh %{buildroot}/%{_datadir}/zsh/site-functions/_virt-who

# Don't run test suite in check section, because it need the system to be
# registered to subscription-manager server

%post
%if %{use_systemd}
%systemd_post virt-who.service
%else
# This adds the proper /etc/rc*.d links for the script
/sbin/chkconfig --add virt-who
%endif
# This moves parameters from old config to remaining general config file
%if (0%{?fedora} > 33 || 0%{?rhel} > 8)
%{python_exec} %{python_sitelib}/virtwho/migrate/migrateconfiguration.py
%endif

%preun
%if %{use_systemd}
%systemd_preun virt-who.service
%else
if [ $1 -eq 0 ] ; then
    /sbin/service virt-who stop >/dev/null 2>&1
    /sbin/chkconfig --del virt-who
fi
%endif

%postun
%if %{use_systemd}
%systemd_postun_with_restart virt-who.service
%else
if [ "$1" -ge "1" ] ; then
    /sbin/service virt-who condrestart >/dev/null 2>&1 || :
fi
%endif

%files
%doc README.md LICENSE README.hyperv
%{_bindir}/virt-who
%{_bindir}/virt-who-password
%{python_sitelib}/*
%if %{use_systemd}
%{_unitdir}/virt-who.service
%else
%{_sysconfdir}/rc.d/init.d/virt-who
%endif
%attr(700, root, root) %dir %{_sysconfdir}/virt-who.d
%{_mandir}/man8/virt-who.8.gz
%{_mandir}/man8/virt-who-password.8.gz
%{_mandir}/man5/virt-who-config.5.gz
%attr(700, root, root) %{_sharedstatedir}/%{name}
%ghost %{_sharedstatedir}/%{name}/key
%{_datadir}/zsh/site-functions/_virt-who
%{_sysconfdir}/virt-who.d/template.conf
%attr(600, root, root) %config(noreplace) %{_sysconfdir}/virt-who.conf

%changelog
%autochangelog
