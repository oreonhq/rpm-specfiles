# default dependencies
%global hawkey_version 0.75.0
%global libcomps_version 0.1.8
%global libmodulemd_version 2.9.3
%global rpm_version 4.14.0

# conflicts
%global conflicts_dnf_plugins_core_version 4.7.0
%global conflicts_dnf_plugins_extras_version 4.0.4
%global conflicts_dnfdaemon_version 0.3.19

%bcond dnf5_obsoletes_dnf %[0%{?fedora} > 40 || 0%{?rhel} > 10]

# override dependencies for fedora 26
%if 0%{?fedora} == 26
    %global rpm_version 4.13.0.1-7
%endif


# YUM compat subpackage configuration
#
# level=full    -> deploy all compat symlinks (conflicts with yum < 4)
# level=minimal -> deploy a subset of compat symlinks only
#                  (no conflict with yum >= 3.4.3-505)*
# *release 505 renamed /usr/bin/yum to /usr/bin/yum-deprecated
%global yum_compat_level full
%global yum_subpackage_name yum
%if 0%{?fedora}
    # Avoid file conflict with yum < 4 in all Fedoras
    # It can be resolved by pretrans scriptlet but they are not recommended in Fedora
    %global yum_compat_level minimal
    %if 0%{?fedora} < 31
        # Avoid name conflict with yum < 4
        %global yum_subpackage_name %{name}-yum
    %endif
%endif

# paths
%global confdir %{_sysconfdir}/%{name}
%global pluginconfpath %{confdir}/plugins

%global py3pluginpath %{python3_sitelib}/%{name}-plugins

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}


%global pkg_summary     Package manager
%global pkg_description Utility that allows users to manage packages on their systems. \
It supports RPMs, modules and comps groups & environments.

Name:           dnf
Version:        4.24.0
Release:        3%{?dist}
Summary:        %{pkg_summary}
# For a breakdown of the licensing, see PACKAGE-LICENSING
License:        GPL-2.0-or-later AND GPL-1.0-only
URL:            https://github.com/rpm-software-management/dnf
Source0:        https://github.com/rpm-software-management/dnf/releases/download/4.24.0/dnf-4.24.0.tar.gz
Source1:        https://github.com/rpm-software-management/dnf/releases/download/4.24.0/dnf-4.24.0.tar.gz.asc
# Key exported from Petr Pisar's keyring
Source2:        gpgkey-E3F42FCE156830A80358E6E94FD1AEC3365AF7BF.gpg
# oreon url source checksums begin
%global source0_sha256 fabdc4436e9a8a152d38060602f491bee4245ad54656f01991f33d511c87bfb1
%global source0_file dnf-4.24.0.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  cmake >= 3.5.0
BuildRequires:  gettext
BuildRequires:  gnupg2
# Documentation
BuildRequires:  systemd
%if 0%{?fedora} > 40 || 0%{?rhel} > 10
BuildRequires:  bash-completion-devel
%else
BuildRequires:  bash-completion
%endif
Requires:       coreutils
BuildRequires:  %{_bindir}/sphinx-build-3
Requires:       python3-%{name} = %{version}-%{release}
%if 0%{?fedora}
Recommends:     (%{_bindir}/sqlite3 if (bash-completion and python3-dnf-plugins-core))
%else
Recommends:     (python3-dbus if NetworkManager)
%endif
Conflicts:      python3-dnf-plugins-core < %{conflicts_dnf_plugins_core_version}
Conflicts:      python3-dnf-plugins-extras-common < %{conflicts_dnf_plugins_extras_version}

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

%if 0%{?fedora} && 0%{?fedora} < 31
Conflicts:      yum < 3.4.3-505
%else
Provides:       %{name}-yum = %{version}-%{release}
Obsoletes:      %{name}-yum < 5
%endif

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
%if 0%{?fedora}
%if 0%{?fedora} < 40
Recommends:     deltarpm
%endif
# required for DNSSEC main.gpgkey_dns_verification https://dnf.readthedocs.io/en/latest/conf_ref.html
Recommends:     python3-unbound
%endif
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/dnf-4.24.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fabdc4436e9a8a152d38060602f491bee4245ad54656f01991f33d511c87bfb1" || { echo "oreon: Source0 SHA256 mismatch for dnf-4.24.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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

# Strict conf distribution
%if 0%{?rhel}
mv -f %{buildroot}%{confdir}/%{name}-strict.conf %{buildroot}%{confdir}/%{name}.conf
%else
rm -vf %{buildroot}%{confdir}/%{name}-strict.conf
%endif

%if %{without dnf5_obsoletes_dnf}
# YUM compat layer
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

%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
%py3_shebang_fix %{buildroot}%{_bindir}/dnf-3
%if %{without dnf5_obsoletes_dnf}
%py3_shebang_fix %{buildroot}%{_bindir}/dnf-automatic
%endif
%py3_shebang_fix %{buildroot}%{python3_sitelib}/%{name}/cli/completion_helper.py
%endif

%check
%if 0%{?rhel} && 0%{?rhel} < 10
pushd %{__cmake_builddir}
ctest -VV
popd
%else
%ctest -VV
%endif


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
%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/yum2dnf.8*
%{_mandir}/man7/dnf.modularity.7*
%{_mandir}/man5/dnf-transaction-json.5*
%{_unitdir}/%{name}-makecache.service
%{_unitdir}/%{name}-makecache.timer
%endif

%files data
%license COPYING PACKAGE-LICENSING
%doc AUTHORS README.rst
%dir %{confdir}
%dir %{confdir}/modules.d
%dir %{confdir}/modules.defaults.d
%dir %{pluginconfpath}
%if %{without dnf5_obsoletes_dnf}
%dir %{confdir}/protected.d
%dir %{confdir}/usr-drift-protected-paths.d
%dir %{confdir}/vars
%endif
%dir %{confdir}/aliases.d
%exclude %{confdir}/aliases.d/zypper.conf
%if %{without dnf5_obsoletes_dnf}
# If DNF5 does not obsolete DNF ownership of dnf.conf should be DNF's
%config(noreplace) %{confdir}/%{name}.conf
%endif
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%ghost %attr(644,-,-) %{_localstatedir}/log/hawkey.log
%ghost %attr(644,-,-) %{_localstatedir}/log/%{name}.log
%ghost %attr(644,-,-) %{_localstatedir}/log/%{name}.librepo.log
%ghost %attr(644,-,-) %{_localstatedir}/log/%{name}.rpm.log
%ghost %attr(644,-,-) %{_localstatedir}/log/%{name}.plugin.log
%ghost %attr(755,-,-) %dir %{_sharedstatedir}/%{name}
%ghost %attr(644,-,-) %{_sharedstatedir}/%{name}/groups.json
%ghost %attr(755,-,-) %dir %{_sharedstatedir}/%{name}/yumdb
%ghost %attr(755,-,-) %dir %{_sharedstatedir}/%{name}/history
%{_mandir}/man5/%{name}4.conf.5*
%if %{without dnf5_obsoletes_dnf}
%{_mandir}/man5/%{name}.conf.5*
%endif
%{_tmpfilesdir}/%{name}.conf

%if %{without dnf5_obsoletes_dnf}
%files -n %{yum_subpackage_name}
%{_bindir}/yum
%{_mandir}/man8/yum.8*
%if "%{yum_compat_level}" == "full"
%{_sysconfdir}/yum
%{_sysconfdir}/yum.conf
%{_mandir}/man5/yum.conf.5.*
%{_mandir}/man8/yum-shell.8*
%{_mandir}/man1/yum-aliases.1*
# If DNF5 does not obsolete DNF, protected.d/yum.conf should be owned by DNF
%config(noreplace) %{confdir}/protected.d/yum.conf
%else
%exclude %{_sysconfdir}/yum.conf
%exclude %{confdir}/protected.d/yum.conf
%exclude %{_mandir}/man5/yum.conf.5.*
%exclude %{_mandir}/man8/yum-shell.8*
%exclude %{_mandir}/man1/yum-aliases.1*
%endif
%else
# No %%{yum_subpackage_name} package
%exclude %{confdir}/protected.d/yum.conf
%exclude %{_mandir}/man5/yum.conf.5.*
%exclude %{_mandir}/man8/yum.8*
%exclude %{_mandir}/man8/yum-shell.8*
%exclude %{_mandir}/man1/yum-aliases.1*
%endif

%files -n python3-%{name}
%{_bindir}/%{name}-3
%{_bindir}/%{name}4
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}-3
%{_datadir}/bash-completion/completions/%{name}4
%{_mandir}/man8/%{name}4.8*
%{_mandir}/man7/dnf4.modularity.7*
%{_mandir}/man5/dnf4-transaction-json.5*
%exclude %{python3_sitelib}/%{name}/automatic
%{python3_sitelib}/%{name}-*.dist-info
%{python3_sitelib}/%{name}/
%dir %{py3pluginpath}
%dir %{py3pluginpath}/__pycache__
%{_var}/cache/%{name}/

%if %{without dnf5_obsoletes_dnf}
%files automatic
%{_bindir}/%{name}-automatic
%config(noreplace) %{confdir}/automatic.conf
%{_mandir}/man8/%{name}-automatic.8*
%{_unitdir}/%{name}-automatic.service
%{_unitdir}/%{name}-automatic.timer
%{_unitdir}/%{name}-automatic-notifyonly.service
%{_unitdir}/%{name}-automatic-notifyonly.timer
%{_unitdir}/%{name}-automatic-download.service
%{_unitdir}/%{name}-automatic-download.timer
%{_unitdir}/%{name}-automatic-install.service
%{_unitdir}/%{name}-automatic-install.timer
%{python3_sitelib}/%{name}/automatic/
%endif

%files bootc
# bootc subpackage does not include any files

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.24.0-3
- Prepare for Oreon 11 (RP1)
