%global source0_hash d74cda35bcaec3efac7f032944adb6cfac8a496f8f93c93315ad1ab586e1f74b
%global source41_hash 9aa8ec276e253ab8fffe04b786e322a1c1fe988e5e2af06fb617a43a4413d139
%global source42_hash cec83bf402dc6ac0e5a2030500ef7296ad4d5c77e756475252b99e89a4d5ebfa
%global source100_hash 8ddc952a290821bde82a158dae0591aff2a0218e26f35d0b8decb9c672609a0f
%global source101_hash 3543108bb93f27ef00cd1c4381ac9a5b160ab8a1481a8a1df6359d0799fc18c5

Name: pcs
Version: 0.12.2
Release: 1%{?dist}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
# GPL-2.0-only: pcs
# MIT: dacite
License: GPL-2.0-only AND MIT
URL: https://github.com/ClusterLabs/pcs
Group: System Environment/Base
Summary: Pacemaker/Corosync Configuration System
BuildArch: noarch

# Remove a tilde used by RPM to get the correct upstream version
%global clean_version %(echo %{version} | sed 's/~//')

# To build an official pcs release, comment out branch_or_commit
# Use long commit hash or branch name to build an unreleased version
# %%global branch_or_commit 1353dfbb3af82d77f4de17a3fa4cbde185bb2b2d
%global version_or_commit %{clean_version}
%if 0%{?branch_or_commit:1}
  %global version_or_commit %{branch_or_commit}
  %global tarball_version %{clean_version}+%(echo %{branch_or_commit} | head -c 8)
%endif
%global pcs_source_name %{name}-%{version_or_commit}

# To build an official pcs-web-ui release, comment out ui_branch_or_commit
# Last tagged version, also used as fallback version for untagged tarballs
%global ui_version 0.1.24.2
%global ui_modules_version 0.1.24.2
# Use long commit hash or branch name to build an unreleased version
# %%global ui_branch_or_commit 34372d1268f065ed186546f55216aaa2d7e76b54
%global ui_version_or_commit %{ui_version}
%if 0%{?ui_branch_or_commit:1}
  %global ui_version_or_commit %{ui_branch_or_commit}
  %global ui_tarball_version %{ui_version}-%(echo %{ui_branch_or_commit} | head -c 8)
%endif
%global ui_src_name pcs-web-ui-%{ui_version_or_commit}


%global pyagentx_version  0.4.pcs.2
%global dacite_version 1.9.2

%global required_pacemaker_version 3.0.0

%global pcs_bundled_dir pcs_bundled
%global pcsd_webui_dir %{_prefix}/lib/pcsd/public/ui

%global cockpit_dir %{_datadir}/cockpit/
%global metainfo_dir %{_datadir}/metainfo
%global ui_metainfo_name org.clusterlabs.cockpit_pcs_web_ui.metainfo.xml
%global ui_metainfo %{metainfo_dir}/%{ui_metainfo_name}

%global pkg_pcs_snmp  pcs-snmp
%global pkg_pcs_web_ui pcs-web-ui
%global pkg_cockpit_ha_cluster cockpit-ha-cluster

# prepend v for folder in GitHub link when using tagged tarball
%if "%{clean_version}" == "%{version_or_commit}"
  %global v_prefix v
%endif

# part after the last slash is recognized as filename in look-aside cache
Source0:        https://github.com/ClusterLabs/pcs/archive/refs/tags/v0.12.2.tar.gz#/pcs-0.12.2.tar.gz

Source41:        https://github.com/ondrejmular/pyagentx/archive/refs/tags/v0.4.pcs.2.tar.gz#/pyagentx-0.4.pcs.2.tar.gz
Source42:        https://github.com/konradhalas/dacite/archive/refs/tags/v1.9.2.tar.gz#/dacite-1.9.2.tar.gz

Source100:        https://github.com/ClusterLabs/pcs-web-ui/archive/refs/tags/0.1.24.2.tar.gz#/pcs-web-ui-0.1.24.2.tar.gz
Source101:        https://github.com/ClusterLabs/pcs-web-ui/releases/download/0.1.24.2/pcs-web-ui-node-modules-0.1.24.2.tar.xz


# pcs patches: <= 200
# Patch1: name.patch
Patch1: show-info-page-instead-of-webui.patch
Patch2: drop-dependency-on-rubygem-cgi.patch
Patch3: typing-fixes-for-python-3.15.patch

# ui patches: >200
# Patch201: name-web-ui.patch


# Split pcs to pcs and pcs-web-ui, all packages that replace pcs must obsolete
# the old monolithic package
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_one_to_many_replacement
Obsoletes: pcs < 0.12.0
# Web UI is an add-on that doesn't need to be installed for pcs to function.
# Upgrades from before 0.12 will install it thanks to Obsoletes. But it will
# be possible to uninstall web UI to disable it and then it will not be
# installed during upgrades because it is a weak dependency.
Recommends: %{pkg_pcs_web_ui} == %{version}-%{release}


# git for patches
BuildRequires: git-core
# for building pcs tarballs
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
# printf from coreutils is used in makefile, head is used in spec
BuildRequires: coreutils
# find is used in Makefile and also somewhere else
BuildRequires: findutils
# python for pcs
BuildRequires: python3-dateutil >= 2.7.0
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pycurl
BuildRequires: python3-pip
BuildRequires: python3-pyparsing
BuildRequires: python3-tornado
BuildRequires: python3-cryptography
BuildRequires: python3-lxml
# for building bundled python packages
# setuptools 71+ builds wheels by itself
BuildRequires: (python3-wheel if python3-setuptools < 71)
# ruby and gems for pcsd
BuildRequires: ruby >= 2.5.0
BuildRequires: ruby-devel
BuildRequires: rubygem(backports)
BuildRequires: rubygem(childprocess)
BuildRequires: rubygem(ethon)
BuildRequires: rubygem(ffi)
BuildRequires: rubygem(json)
BuildRequires: rubygem(logger)
BuildRequires: rubygem(mustermann)
BuildRequires: rubygem(puma)
BuildRequires: (rubygem(rack) < 3 or (rubygem(rack) >= 3 and rubygem(rackup)))
BuildRequires: rubygem(rack-protection)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(sinatra)
BuildRequires: rubygem(tilt)
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: rubygem(rexml)
%endif
# ruby libraries for tests
BuildRequires: rubygem(test-unit)
# for touching patch files (sanitization function)
BuildRequires: diffstat
# for systemd scriptlet macros
BuildRequires: systemd-rpm-macros
# pam is used for authentication inside daemon (python ctypes)
# needed for tier0 tests during build
BuildRequires: pam
# for working with qdevice certificates (certutil) - used in configure.ac
BuildRequires: nss-tools
# pcs now provides a pc file
BuildRequires: pkgconfig


# cluster stack packages for pkg-config
# corosync has different package names on distributions but all provide
# corosync-devel
# corosync and pacemaker need versions and it's not working in virtual provides
BuildRequires: corosync-devel >= 3.0
BuildRequires: pacemaker-libs-devel >= %{required_pacemaker_version}
BuildRequires: pkgconfig(booth)
BuildRequires: pkgconfig(corosync-qdevice)
BuildRequires: pkgconfig(sbd)

# for validating cockpit-ha-cluster metainfo
BuildRequires: libappstream-glib


# python and libraries for pcs, setuptools for pcs entrypoint
Requires: python3-cryptography
Requires: python3-dateutil >= 2.7.0
Requires: python3-lxml
Requires: python3-pycurl
Requires: python3-pyparsing
Requires: python3-tornado
# ruby and gems for pcsd
Requires: ruby >= 3.3.0
Requires: rubygem(backports)
Requires: rubygem(childprocess)
Requires: rubygem(ethon)
Requires: rubygem(ffi)
Requires: rubygem(json)
Requires: rubygem(logger)
Requires: rubygem(mustermann)
Requires: rubygem(puma)
Requires: (rubygem(rack) < 3 or (rubygem(rack) >= 3 and rubygem(rackup)))
Requires: rubygem(rack-protection)
Requires: rubygem(sinatra)
Requires: rubygem(tilt)
%if 0%{?fedora} || 0%{?rhel} >= 9
Requires: rubygem(rexml)
%endif
# for killall
Requires: psmisc
# cluster stack and related packages
Requires: pcmk-cluster-manager >= %{required_pacemaker_version}
Suggests: pacemaker
Requires: (corosync >= 3.0 if pacemaker)
# pcs enables corosync encryption by default so we require libknet1-plugins-all
Requires: (libknet1-plugins-all if corosync)
Requires: pacemaker-cli >= %{required_pacemaker_version}
# pam is used for authentication inside daemon (python ctypes)
# more details: https://bugzilla.redhat.com/show_bug.cgi?id=1717113
Requires: pam
# needs logrotate for /etc/logrotate.d/pcsd
Requires: logrotate
# for working with qdevice certificates (certutil)
Requires: nss-tools


Provides: bundled(dacite) = %{dacite_version}

# pcs-snmp subpackage definition
%package -n %{pkg_pcs_snmp}
Group: System Environment/Base
Summary: Pacemaker cluster SNMP agent
# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
# GPL-2.0-only: pcs
# BSD-2-Clause: pyagentx
License: GPL-2.0-only AND BSD-2-Clause
URL: https://github.com/ClusterLabs/pcs
BuildArch: noarch

# tar for unpacking pyagentx source tarball
BuildRequires: tar

Requires: pcs = %{version}-%{release}
Requires: pacemaker
Requires: net-snmp

Provides: bundled(pyagentx) = %{pyagentx_version}

# pcs-web-ui subpackage definition
%package -n %{pkg_pcs_web_ui}
Summary: Standalone web UI for Pacemaker/Corosync Configuration System
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
# GPL-2.0-only: pcs
License: GPL-2.0-only
URL: https://github.com/ClusterLabs/pcs-web-ui

# Split pcs to pcs and pcs-web-ui, all packages that replace pcs must obsolete
# the old monolithic package
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_one_to_many_replacement
Obsoletes: pcs < 0.12.0

Requires: pcs = %{version}-%{release}

Provides: bundled(pcs-web-ui) = %{!?ui_tarball_version:%{ui_version}}%{?ui_tarball_version}

# cockpit-ha-cluster subpackage definition
%package -n %{pkg_cockpit_ha_cluster}
Group: System Environment/Base
Summary: Cockpit application for managing Pacemaker based clusters
License: GPL-2.0-only AND CC0-1.0
URL: https://github.com/ClusterLabs/pcs-web-ui

BuildRequires: make
BuildRequires: nodejs-npm, /usr/bin/npm

Requires: pcs = %{version}-%{release}
Requires: cockpit-bridge

Provides: bundled(pcs-web-ui) = %{!?ui_tarball_version:%{ui_version}}%{?ui_tarball_version}



%description
pcs is a configuration tool for Corosync and Pacemaker. It permits users to
easily view, modify and create high availability clusters based on Pacemaker.
This package contains the pcs command-line utility and its server pcsd.

%description -n %{pkg_pcs_web_ui}
Provides standalone web UI for Pacemaker/Corosync Configuration System (pcs).

%description -n %{pkg_pcs_snmp}
SNMP agent that provides information about Pacemaker cluster to the main agent
(snmpd).

%description -n %{pkg_cockpit_ha_cluster}
Cockpit application for managing Pacemaker based clusters. Uses
Pacemaker/Corosync Configuration System (pcs) in the background.



%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source41_hash}" = "none" || { f="%{SOURCE41}"; test -f "$f" || { echo "oreon: missing Source41 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source41_hash}" || { echo "oreon: Source41 hash mismatch" >&2; exit 1; }; }
test "%{source42_hash}" = "none" || { f="%{SOURCE42}"; test -f "$f" || { echo "oreon: missing Source42 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source42_hash}" || { echo "oreon: Source42 hash mismatch" >&2; exit 1; }; }
test "%{source100_hash}" = "none" || { f="%{SOURCE100}"; test -f "$f" || { echo "oreon: missing Source100 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source100_hash}" || { echo "oreon: Source100 hash mismatch" >&2; exit 1; }; }
test "%{source101_hash}" = "none" || { f="%{SOURCE101}"; test -f "$f" || { echo "oreon: missing Source101 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source101_hash}" || { echo "oreon: Source101 hash mismatch" >&2; exit 1; }; }# -- following is inspired by python-simplejon.el5 --
# Update timestamps on the files touched by a patch, to avoid non-equal
# .pyc/.pyo files across the multilib peers within a build

update_times(){
  # update_times <reference_file> <file_to_touch> ...
  # set the access and modification times of each file_to_touch to the times
  # of reference_file

  # put all args to file_list
  file_list=("$@")
  # first argument is reference_file: so take it and remove from file_list
  reference_file=${file_list[0]}
  unset file_list[0]

  for fname in ${file_list[@]}; do
    # some files could be deleted by a patch therefore we test file for
    # existance before touch to avoid exit with error: No such file or
    # directory
    # diffstat cannot create list of files without deleted files
    test -e $fname && touch -r $reference_file $fname
  done
}

update_times_patch(){
  # update_times_patch <patch_file_name>
  # set the access and modification times of each file in patch to the times
  # of patch_file_name

  patch_file_name=$1

  # diffstat
  # -l lists only the filenames. No histogram is generated.
  # -p override the logic that strips common pathnames,
  #    simulating the patch "-p" option. (Strip the smallest prefix containing
  #    num leading slashes from each file name found in the patch file)
  update_times ${patch_file_name} `diffstat -p1 -l ${patch_file_name}`
}

# documentation for setup/autosetup/autopatch:
#   * http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html
#   * https://rpm-software-management.github.io/rpm/manual/autosetup.html
# patch web-ui sources
# -n <name> — Set Name of Build Directory
# -T — Do Not Perform Default Archive Unpacking
# -b <n> — Unpack The nth Sources Before Changing Directory
# -a <n> — Unpack The nth Sources After Changing Directory
# -N — disables automatic patch application, use autopatch to apply patches
#
# 1. unpack sources (-b 0)
# 2. then cd into sources tree (the setup macro itself)
# 3. then unpack node_modules into sources tree (-a 1).
%autosetup -T -b 100 -a 101 -N -n %{ui_src_name}
%autopatch -p1 -m 201
# update_times_patch %%{PATCH201}

# patch pcs sources
%autosetup -S git -n %{pcs_source_name} -N
%autopatch -p1 -M 200
# update_times_patch %%{PATCH1}
update_times_patch %{PATCH1}
update_times_patch %{PATCH2}
update_times_patch %{PATCH3}

# generate .tarball-version if building from an untagged commit, not a released version
# autogen uses git-version-gen which uses .tarball-version for generating version number
%if 0%{?tarball_version:1}
  echo %{tarball_version} > %{_builddir}/%{pcs_source_name}/.tarball-version
%endif

%if 0%{?ui_tarball_version:1}
  echo %{ui_tarball_version} > %{_builddir}/%{ui_src_name}/.tarball-version
%endif

# prepare dirs/files necessary for building python bundles
mkdir -p %{pcs_bundled_dir}/src
cp -f %SOURCE41 rpm/
cp -f %SOURCE42 rpm/



%build
%define debug_package %{nil}

# We left off by setting up pcs, so we are in its directory now
./autogen.sh
%{configure} --enable-local-build --enable-use-local-cache-only \
  --enable-individual-bundling --enable-webui \
  --with-pcsd-default-cipherlist='PROFILE=SYSTEM' \
  --with-pcs-lib-dir="%{_prefix}/lib" PYTHON=%{__python3}
make all

# Web UI installation
# Switch to web ui folder first
cd ../%{ui_src_name}
./autogen.sh
%{configure} \
  --with-pcsd-webui-dir=%{pcsd_webui_dir} \
  --with-cockpit-dir=%{cockpit_dir} \
  --with-metainfo-dir=%{metainfo_dir}
make all



%install
rm -rf %{buildroot}
pwd

# Install cockpit pcs-web-ui
cd ../%{ui_src_name}
%make_install

# prepare pcs-web-ui files (not needed for pcs as pcs installs them in Makefile)
mkdir -p %{buildroot}/%{_defaultlicensedir}/%{pkg_cockpit_ha_cluster}
mkdir -p %{buildroot}/%{_defaultlicensedir}/%{pkg_pcs_web_ui}

cp COPYING %{buildroot}/%{_defaultlicensedir}/%{pkg_cockpit_ha_cluster}/COPYING_WUI.md
mv COPYING %{buildroot}/%{_defaultlicensedir}/%{pkg_pcs_web_ui}/COPYING_WUI.md

mkdir -p %{buildroot}/%{_docdir}/%{pkg_cockpit_ha_cluster}
mkdir -p %{buildroot}/%{_docdir}/%{pkg_pcs_web_ui}

cp CHANGELOG.md %{buildroot}/%{_docdir}/%{pkg_cockpit_ha_cluster}/CHANGELOG_WUI.md
mv CHANGELOG.md %{buildroot}/%{_docdir}/%{pkg_pcs_web_ui}/CHANGELOG_WUI.md

cp README.md %{buildroot}/%{_docdir}/%{pkg_cockpit_ha_cluster}/README_WUI.md
mv README.md %{buildroot}/%{_docdir}/%{pkg_pcs_web_ui}/README_WUI.md

# Install pcs
cd ../%{pcs_source_name}
%make_install

# prepare license files
cp %{pcs_bundled_dir}/src/pyagentx-*/LICENSE.txt pyagentx_LICENSE.txt
cp %{pcs_bundled_dir}/src/pyagentx-*/CONTRIBUTORS.txt pyagentx_CONTRIBUTORS.txt
cp %{pcs_bundled_dir}/src/pyagentx-*/README.md pyagentx_README.md

cp %{pcs_bundled_dir}/src/dacite-*/LICENSE dacite_LICENSE
cp %{pcs_bundled_dir}/src/dacite-*/README.md dacite_README.md



%check
# Run validation of cockpit metainfo
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{ui_metainfo_name}

# In the building environment LC_CTYPE is set to C which causes tests to fail
# due to python prints a warning about it to stderr. The following environment
# variable disables the warning.
# On the live system either UTF8 locale is set or the warning is emmited
# which breaks pcs. That is the correct behavior since with wrong locales it
# would be probably broken anyway.
# The main concern here is to make the tests pass.
# See https://fedoraproject.org/wiki/Changes/python3_c.utf-8_locale for details.
export PYTHONCOERCECLOCALE=0

run_all_tests(){
  #run pcs tests

  # disabled tests:
  #
  %{__python3} pcs_test/suite --tier0 -v --vanilla --all-but \
  pcs_test.tier0.daemon.app.test_app_remote.SyncConfigMutualExclusive.test_get_not_locked \
  pcs_test.tier0.daemon.app.test_app_remote.SyncConfigMutualExclusive.test_post_not_locked \

  test_result_python=$?

  #run pcsd tests and remove them
  ruby \
    -I%{buildroot}%{_prefix}/lib/pcsd \
    -Ipcsd/test \
    pcsd/test/test_all_suite.rb
  test_result_ruby=$?

  if [ $test_result_python -ne 0 ]; then
    return $test_result_python
  fi
  return $test_result_ruby
}

run_all_tests



# Scriptlets documentation:
#  * https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/
#  * https://github.com/systemd/systemd/blob/main/src/rpm/macros.systemd.in
#  * https://github.com/systemd/systemd/blob/main/src/rpm/systemd-update-helper.in
#  * https://fedoraproject.org/wiki/Changes/Restart_services_at_end_of_rpm_transaction

%post
# Set systemd preset for pcsd{,-ruby}.service after install
%systemd_post pcsd.service pcsd-ruby.service

%post -n %{pkg_pcs_snmp}
# Set systemd preset for pcs_snmp_agent.service after install
%systemd_post pcs_snmp_agent.service


%preun
# Stop pcsd{,-ruby}.service before pcs uninstall
%systemd_preun pcsd.service pcsd-ruby.service

%preun -n %{pkg_pcs_snmp}
# Stop pcs_snmp_agent.service before pcs-snmp uninstall
%systemd_preun pcs_snmp_agent.service


%posttrans
# Mark pcsd.service for restart after pcs upgrade
%systemd_posttrans_with_restart pcsd.service

%posttrans -n %{pkg_pcs_snmp}
# Mark pcs_snmp_agent.service for restart after pcs-snmp upgrade
%systemd_posttrans_with_restart pcs_snmp_agent.service

%posttrans -n %{pkg_pcs_web_ui}
# NOTE: Systemd macros cannot be used for pcsd restart from pcs-web-ui because
# pcs-web-ui does not change unit files and therefore trigger for restart would
# not happen. Direct call `systemctl try-restart` is used instead.

# Restart pcsd if it is running to reload the Tornado app so it detects
# presence or absence of the webui backend handler on install/update
# of pcs-web-ui that contains it
if [ $1 -ge 1 ] && [ -d /run/systemd/system ]; then
  systemctl try-restart pcsd.service || :
fi


%postun -n %{pkg_pcs_web_ui}
# Restart pcsd.service if running on pcs-web-ui uninstall
if [ $1 -eq 0 ] && [ -d /run/systemd/system ]; then
  systemctl try-restart pcsd.service || :
fi



%files
%doc CHANGELOG.md
%doc README.md
%doc dacite_README.md
%license dacite_LICENSE
%license COPYING
%{python3_sitelib}/*
%{_bindir}/pcs
%{_bindir}/pcsd
%{_prefix}/lib/pcs/*
%{_prefix}/lib/pkgconfig/pcs.pc
%{_prefix}/lib/pcsd/*
%{_unitdir}/pcsd.service
%{_unitdir}/pcsd-ruby.service
%{_datadir}/bash-completion/completions/pcs
%{_sharedstatedir}/pcsd
%config(noreplace) %{_sysconfdir}/pam.d/pcsd
%dir %{_var}/log/pcsd
%config(noreplace) %{_sysconfdir}/logrotate.d/pcsd
%config(noreplace) %{_sysconfdir}/sysconfig/pcsd
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/cfgsync_ctl
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/known-hosts
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/pcsd.cookiesecret
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/pcsd.crt
%ghost %config(noreplace) %attr(0600,root,root) %{_sharedstatedir}/pcsd/pcsd.key
%ghost %config(noreplace) %attr(0644,root,root) %{_sharedstatedir}/pcsd/pcs_settings.conf
%ghost %config(noreplace) %attr(0644,root,root) %{_sharedstatedir}/pcsd/pcs_users.conf
%{_mandir}/man8/pcs.*
%{_mandir}/man8/pcsd.*
%exclude %{_prefix}/lib/pcs/pcs_snmp_agent
%exclude %{_prefix}/lib/pcs/%{pcs_bundled_dir}/packages/pyagentx*
%exclude %{cockpit_dir}
%exclude %{ui_metainfo}
%exclude %{python3_sitelib}/pcs/daemon/app/webui
%exclude %{pcsd_webui_dir}

%files -n %{pkg_pcs_web_ui}
%doc CHANGELOG.md
%doc %{_docdir}/%{pkg_pcs_web_ui}/CHANGELOG_WUI.md
%doc %{_docdir}/%{pkg_pcs_web_ui}/README_WUI.md
%license COPYING
%license %{_defaultlicensedir}/%{pkg_pcs_web_ui}/COPYING_WUI.md
%{python3_sitelib}/pcs/daemon/app/webui
%{pcsd_webui_dir}

%files -n %{pkg_pcs_snmp}
%{_prefix}/lib/pcs/pcs_snmp_agent
%{_prefix}/lib/pcs/%{pcs_bundled_dir}/packages/pyagentx*
%{_unitdir}/pcs_snmp_agent.service
%{_datadir}/snmp/mibs/PCMK-PCS*-MIB.txt
%{_mandir}/man8/pcs_snmp_agent.*
%config(noreplace) %{_sysconfdir}/sysconfig/pcs_snmp_agent
%doc CHANGELOG.md
%doc pyagentx_CONTRIBUTORS.txt
%doc pyagentx_README.md
%license COPYING
%license pyagentx_LICENSE.txt

%files -n %{pkg_cockpit_ha_cluster}
%doc %{_docdir}/%{pkg_cockpit_ha_cluster}/CHANGELOG_WUI.md
%doc %{_docdir}/%{pkg_cockpit_ha_cluster}/README_WUI.md
%license %{_defaultlicensedir}/%{pkg_cockpit_ha_cluster}/COPYING_WUI.md
%{cockpit_dir}
%{ui_metainfo}



%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12.2-1
- Prepare for Oreon 11 (RP1)
