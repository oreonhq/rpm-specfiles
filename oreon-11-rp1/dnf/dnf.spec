%global source0_hash fabdc4436e9a8a152d38060602f491bee4245ad54656f01991f33d511c87bfb1
%global source2_key_fpr E3F42FCE156830A80358E6E94FD1AEC3365AF7BF
%global hawkey_version 0.75.0
%global libcomps_version 0.1.8
%global libmodulemd_version 2.9.3
%global rpm_version 4.14.0
%global conflicts_dnf_plugins_core_version 4.7.0
%global conflicts_dnf_plugins_extras_version 4.0.4
%global conflicts_dnfdaemon_version 0.3.19
%bcond dnf5_obsoletes_dnf %[0%{?fedora} > 40 || 0%{?rhel} > 10]
%global yum_compat_level full
%global yum_subpackage_name yum
%global confdir %{_sysconfdir}/%{name}
%global pluginconfpath %{confdir}/plugins
%global py3pluginpath %{python3_sitelib}/%{name}-plugins
%global _docdir_fmt %{name}
%global pkg_summary     Package manager
%global pkg_description Utility that allows users to manage packages on their systems. \
It supports RPMs, modules and comps groups & environments.
Name:           dnf
Version:        4.24.0
Release:        1%{?dist}
Summary:        Package manager
License:        GPL-2.0-or-later AND GPL-1.0-only
URL:            https://github.com/rpm-software-management/dnf
Source0:        https://github.com/rpm-software-management/dnf/releases/download/4.24.0/dnf-4.24.0.tar.gz
Source1:        dnf-4.24.0.tar.gz.asc
Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg
BuildArch:      noarch
Requires:       coreutils
Requires:       python3-%{name} = %{version}-%{release}
Recommends:     (python3-dbus if NetworkManager)
Conflicts:      python3-dnf-plugins-core < %{conflicts_dnf_plugins_core_version}
Conflicts:      python3-dnf-plugins-extras-common < %{conflicts_dnf_plugins_extras_version}
# oreon:deps
BuildRequires:  /usr/bin/sphinx-build-3
BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  libmodulemd
BuildRequires:  python3-devel
BuildRequires:  python3-hawkey
BuildRequires:  python3-libcomps
BuildRequires:  python3-libdnf
BuildRequires:  python3-rpm
BuildRequires:  systemd
# /oreon:deps
%description
%{pkg_description}

%package data
Summary:        Common data and configuration files for DNF
%if %{with dnf5_obsoletes_dnf}
Requires:       /etc/dnf/dnf.conf
%endif
Obsoletes:      %{name}-conf <= %{version}-%{release}
Provides:       %{name}-conf = %{version}-%{release}
%description data
Common data and configuration files for DNF

%package -n %{yum_subpackage_name}
Requires:       %{name} = %{version}-%{release}
Summary:        %{pkg_summary}
Provides:       %{name}-yum = %{version}-%{release}
Obsoletes:      %{name}-yum < 5
%description -n %{yum_subpackage_name}
%{pkg_description}

%package -n python3-%{name}
Summary:        Python 3 interface to DNF
%{?python_provide:%python_provide python3-%{name}}
BuildRequires:  python3-devel
BuildRequires:  python3-hawkey >= %{hawkey_version}
BuildRequires:  python3-libdnf >= %{hawkey_version}
BuildRequires:  python3-libcomps >= %{libcomps_version}
BuildRequires:  python3-libdnf
BuildRequires:  libmodulemd >= %{libmodulemd_version}
Requires:       libmodulemd >= %{libmodulemd_version}
Requires:       %{name}-data = %{version}-%{release}
Requires:       python3-hawkey >= %{hawkey_version}
Requires:       python3-libdnf >= %{hawkey_version}
Requires:       python3-libcomps >= %{libcomps_version}
Requires:       python3-libdnf
BuildRequires:  python3-rpm >= %{rpm_version}
Requires:       python3-rpm >= %{rpm_version}
Recommends:     (rpm-plugin-systemd-inhibit if systemd)
Provides:       dnf4 = %{version}-%{release}
Provides:       dnf-command(alias)
Provides:       dnf-command(autoremove)
Provides:       dnf-command(check-update)
Provides:       dnf-command(clean)
Provides:       dnf-command(distro-sync)
Provides:       dnf-command(downgrade)
Provides:       dnf-command(group)
Provides:       dnf-command(history)
Provides:       dnf-command(info)
Provides:       dnf-command(install)
Provides:       dnf-command(list)
Provides:       dnf-command(makecache)
Provides:       dnf-command(mark)
Provides:       dnf-command(provides)
Provides:       dnf-command(reinstall)
Provides:       dnf-command(remove)
Provides:       dnf-command(repolist)
Provides:       dnf-command(repoquery)
Provides:       dnf-command(repository-packages)
Provides:       dnf-command(search)
Provides:       dnf-command(updateinfo)
Provides:       dnf-command(upgrade)
Provides:       dnf-command(upgrade-to)
%description -n python3-%{name}
Python 3 interface to DNF.

%package automatic
Summary:        %{pkg_summary} - automated upgrades
BuildRequires:  systemd
Requires:       python3-%{name} = %{version}-%{release}
%{?systemd_requires}
%description automatic
Systemd units that can periodically download package upgrades and apply them.

%package bootc
Summary:        %{pkg_summary} - additional bootc dependencies
Requires:       python3-%{name} = %{version}-%{release}
Requires:       ostree
Requires:       ostree-libs
Requires:       python3-gobject-base
Requires:       util-linux-core
%description bootc
Additional dependencies needed to perform transactions on booted bootc (bootable containers) systems.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%cmake -DPYTHON_DESIRED:FILEPATH=%{__python3} -DDNF_VERSION=%{version}
%cmake_build
%cmake_build -t doc-man
%install
%cmake_install
%find_lang %{name}
mkdir -p %{buildroot}%{confdir}/vars
mkdir -p %{buildroot}%{confdir}/aliases.d
mkdir -p %{buildroot}%{pluginconfpath}/
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/modules.d
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/modules.defaults.d
mkdir -p %{buildroot}%{py3pluginpath}/__pycache__/
mkdir -p %{buildroot}%{_localstatedir}/log/
mkdir -p %{buildroot}%{_var}/cache/dnf/
touch %{buildroot}%{_localstatedir}/log/%{name}.log
%if %{without dnf5_obsoletes_dnf}
ln -sr %{buildroot}%{_bindir}/dnf-3 %{buildroot}%{_bindir}/dnf
ln -sr %{buildroot}%{_datadir}/bash-completion/completions/dnf-3 %{buildroot}%{_datadir}/bash-completion/completions/dnf
for file in %{buildroot}%{_mandir}/man[578]/dnf4[-.]*; do
    dir=$(dirname $file)
    filename=$(basename $file)
    ln -sr $file $dir/${filename/dnf4/dnf}
done
%endif
ln -sr %{buildroot}%{_bindir}/dnf-3 %{buildroot}%{_bindir}/dnf4
ln -sr %{buildroot}%{_datadir}/bash-completion/completions/dnf-3 %{buildroot}%{_datadir}/bash-completion/completions/dnf4
%if %{without dnf5_obsoletes_dnf}
mv %{buildroot}%{_bindir}/dnf-automatic-3 %{buildroot}%{_bindir}/dnf-automatic
%endif
rm -vf %{buildroot}%{_bindir}/dnf-automatic-*
rm -vf %{buildroot}%{confdir}/%{name}-strict.conf
%if %{without dnf5_obsoletes_dnf}
ln -sr  %{buildroot}%{confdir}/%{name}.conf %{buildroot}%{_sysconfdir}/yum.conf
ln -sr  %{buildroot}%{_bindir}/dnf-3 %{buildroot}%{_bindir}/yum
%if "%{yum_compat_level}" == "full"
mkdir -p %{buildroot}%{_sysconfdir}/yum
ln -sr  %{buildroot}%{pluginconfpath} %{buildroot}%{_sysconfdir}/yum/pluginconf.d
ln -sr  %{buildroot}%{confdir}/protected.d %{buildroot}%{_sysconfdir}/yum/protected.d
ln -sr  %{buildroot}%{confdir}/vars %{buildroot}%{_sysconfdir}/yum/vars
%endif
%endif
%if %{with dnf5_obsoletes_dnf}
rm %{buildroot}%{confdir}/automatic.conf
rm %{buildroot}%{confdir}/%{name}.conf
rm %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
rm %{buildroot}%{_mandir}/man8/%{name}-automatic.8*
rm %{buildroot}%{_mandir}/man8/yum2dnf.8*
rm %{buildroot}%{_unitdir}/%{name}-automatic.service
rm %{buildroot}%{_unitdir}/%{name}-automatic.timer
rm %{buildroot}%{_unitdir}/%{name}-automatic-notifyonly.service
rm %{buildroot}%{_unitdir}/%{name}-automatic-notifyonly.timer
rm %{buildroot}%{_unitdir}/%{name}-automatic-download.service
rm %{buildroot}%{_unitdir}/%{name}-automatic-download.timer
rm %{buildroot}%{_unitdir}/%{name}-automatic-install.service
rm %{buildroot}%{_unitdir}/%{name}-automatic-install.timer
rm %{buildroot}%{_unitdir}/%{name}-makecache.service
rm %{buildroot}%{_unitdir}/%{name}-makecache.timer
%endif
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%py3_shebang_fix %{buildroot}%{_bindir}/dnf-3
%if %{without dnf5_obsoletes_dnf}
%py3_shebang_fix %{buildroot}%{_bindir}/dnf-automatic
%endif
%py3_shebang_fix %{buildroot}%{python3_sitelib}/%{name}/cli/completion_helper.py
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%ctest -VV
%if %{without dnf5_obsoletes_dnf}
%post

%systemd_post dnf-makecache.timer
%preun

%systemd_preun dnf-makecache.timer
%postun

%systemd_postun_with_restart dnf-makecache.timer
%post automatic

%systemd_post dnf-automatic.timer dnf-automatic-notifyonly.timer dnf-automatic-download.timer dnf-automatic-install.timer
%preun automatic

if [ ! -e %{_unitdir}/dnf5-automatic.timer ]; then
    %systemd_preun dnf-automatic.timer
fi
%systemd_preun dnf-automatic-notifyonly.timer dnf-automatic-download.timer dnf-automatic-install.timer
%postun automatic

%systemd_postun_with_restart dnf-automatic.timer dnf-automatic-notifyonly.timer dnf-automatic-download.timer dnf-automatic-install.timer
%endif
%if %{without dnf5_obsoletes_dnf}
%files -f %{oreon_filedir}/main.list
%files -n dnf-data -f %{oreon_filedir}/dnf-data.list
%files -n yum -f %{oreon_filedir}/yum.list
%files -n python3-dnf -f %{oreon_filedir}/python3-dnf.list
%files -n dnf-automatic -f %{oreon_filedir}/dnf-automatic.list
%files -n dnf-bootc -f %{oreon_filedir}/dnf-bootc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.24.0-3
- Prepare for Oreon 11 (RP1)
%endif
