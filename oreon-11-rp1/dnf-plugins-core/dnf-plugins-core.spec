%{?!dnf_lowest_compatible: %global dnf_lowest_compatible 4.19.0}
%global dnf_plugins_extra 2.0.0
%global hawkey_version 0.73.0
%global yum_utils_subpackage_name dnf-utils
%if 0%{?rhel} > 7
%global yum_utils_subpackage_name yum-utils
%endif

%define __cmake_in_source_build 1

%bcond dnf5_obsoletes_dnf %[0%{?fedora} > 40 || 0%{?rhel} > 10]

%if (0%{?fedora} && 0%{?fedora} >= 41) || (0%{?rhel} && 0%{?rhel} >= 10)
%bcond_with debug_plugin
%else
%bcond_without debug_plugin
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

%if 0%{?rhel} > 7 || 0%{?fedora} > 29
%bcond_with python2
%else
%bcond_without python2
%endif

%if 0%{?rhel} > 7 || 0%{?fedora} > 30
%bcond_without yumcompatibility
%else
%bcond_with yumcompatibility
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with yumutils
%else
%bcond_without yumutils
%endif

Name:           dnf-plugins-core
Version:        4.10.1
Release:        9%{?dist}
Summary:        Core Plugins for DNF
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/dnf-plugins-core
Source0:        https://github.com/rpm-software-management/dnf-plugins-core/archive/4.10.1/dnf-plugins-core-4.10.1.tar.gz
Patch1:         0001-Fix-building-with-CMake-4.patch
Patch2:         0002-spec-Use-cmake-macros-for-invoking-a-build-script.patch
# oreon url source checksums begin
%global source0_sha256 0f6966a6cb62912cd3520ef2a09ddfcdb48aa3091009f9834526b04f6de9a70a
%global source0_file dnf-plugins-core-4.10.1.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  cmake >= 3.18.0
BuildRequires:  gettext
# Documentation
%if %{with python3}
BuildRequires:  %{_bindir}/sphinx-build-3
Requires:       python3-%{name} = %{version}-%{release}
%else
BuildRequires:  %{_bindir}/sphinx-build
Requires:       python2-%{name} = %{version}-%{release}
%endif
Provides:       dnf-command(builddep)
Provides:       dnf-command(changelog)
Provides:       dnf-command(config-manager)
Provides:       dnf-command(copr)
%if %{with debug_plugin}
Provides:       dnf-command(debug-dump)
Provides:       dnf-command(debug-restore)
%endif
Provides:       dnf-command(debuginfo-install)
Provides:       dnf-command(download)
Provides:       dnf-command(groups-manager)
Provides:       dnf-command(repoclosure)
Provides:       dnf-command(repograph)
Provides:       dnf-command(repomanage)
Provides:       dnf-command(reposync)
Provides:       dnf-command(repodiff)
Provides:       dnf-command(system-upgrade)
Provides:       dnf-command(offline-upgrade)
Provides:       dnf-command(offline-distrosync)
%if %{with debug_plugin}
Provides:       dnf-plugins-extras-debug = %{version}-%{release}
%endif
Provides:       dnf-plugins-extras-repoclosure = %{version}-%{release}
Provides:       dnf-plugins-extras-repograph = %{version}-%{release}
Provides:       dnf-plugins-extras-repomanage = %{version}-%{release}
Provides:       dnf-plugin-builddep = %{version}-%{release}
Provides:       dnf-plugin-config-manager = %{version}-%{release}
Provides:       dnf-plugin-debuginfo-install = %{version}-%{release}
Provides:       dnf-plugin-download = %{version}-%{release}
Provides:       dnf-plugin-generate_completion_cache = %{version}-%{release}
Provides:       dnf-plugin-needs_restarting = %{version}-%{release}
Provides:       dnf-plugin-groups-manager = %{version}-%{release}
Provides:       dnf-plugin-repoclosure = %{version}-%{release}
Provides:       dnf-plugin-repodiff = %{version}-%{release}
Provides:       dnf-plugin-repograph = %{version}-%{release}
Provides:       dnf-plugin-repomanage = %{version}-%{release}
Provides:       dnf-plugin-reposync = %{version}-%{release}
Provides:       dnf-plugin-system-upgrade = %{version}-%{release}
%if %{with yumcompatibility}
Provides:       yum-plugin-copr = %{version}-%{release}
Provides:       yum-plugin-changelog = %{version}-%{release}
Provides:       yum-plugin-auto-update-debug-info = %{version}-%{release}
%endif
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}

%description
Core Plugins for DNF. This package enhances DNF with builddep, config-manager,
copr, %{?with_debug_plugin:debug, }debuginfo-install, download, needs-restarting, groups-manager, repoclosure,
repograph, repomanage, reposync, changelog and repodiff commands. Additionally
provides generate_completion_cache passive plugin.

%if %{with python2}
%package -n python2-%{name}
Summary:        Core Plugins for DNF
%{?python_provide:%python_provide python2-%{name}}
BuildRequires:  python2-dnf >= %{dnf_lowest_compatible}
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  dbus-python
%else
BuildRequires:  python2-dbus
%endif
BuildRequires:  python2-devel
%if 0%{?fedora}
Requires:       python2-distro
%endif
Requires:       python2-dnf >= %{dnf_lowest_compatible}
Requires:       python2-hawkey >= %{hawkey_version}
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       dbus-python
Requires:       python-dateutil
%else
Requires:       python2-dbus
Requires:       python2-dateutil
%endif
%if %{with debug_plugin}
Provides:       python2-dnf-plugins-extras-debug = %{version}-%{release}
%endif
Provides:       python2-dnf-plugins-extras-repoclosure = %{version}-%{release}
Provides:       python2-dnf-plugins-extras-repograph = %{version}-%{release}
Provides:       python2-dnf-plugins-extras-repomanage = %{version}-%{release}
%if %{with debug_plugin}
Obsoletes:      python2-dnf-plugins-extras-debug < %{dnf_plugins_extra}
%endif
Obsoletes:      python2-dnf-plugins-extras-repoclosure < %{dnf_plugins_extra}
Obsoletes:      python2-dnf-plugins-extras-repograph < %{dnf_plugins_extra}
Obsoletes:      python2-dnf-plugins-extras-repomanage < %{dnf_plugins_extra}

Conflicts:      %{name} <= 0.1.5
# let the both python plugin versions be updated simultaneously
Conflicts:      python3-%{name} < %{version}-%{release}
Conflicts:      python-%{name} < %{version}-%{release}

%description -n python2-%{name}
Core Plugins for DNF, Python 2 interface. This package enhances DNF with builddep,
config-manager, copr, %{?with_debug_plugin:debug, }debuginfo-install, download, needs-restarting,
groups-manager, repoclosure, repograph, repomanage, reposync, changelog,
repodiff, system-upgrade, offline-upgrade and offline-distrosync commands.
Additionally provides generate_completion_cache passive plugin.
%endif

%if %{with python3}
%package -n python3-%{name}
Summary:    Core Plugins for DNF
%{?python_provide:%python_provide python3-%{name}}
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  python3-dnf >= %{dnf_lowest_compatible}
BuildRequires:  python3-systemd
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd
%{?systemd_ordering}
%if 0%{?fedora}
Requires:       python3-distro
%endif
Requires:       python3-dbus
Requires:       python3-dnf >= %{dnf_lowest_compatible}
Requires:       python3-hawkey >= %{hawkey_version}
Requires:       python3-dateutil
Requires:       python3-systemd
%if %{with debug_plugin}
Provides:       python3-dnf-plugins-extras-debug = %{version}-%{release}
%endif
Provides:       python3-dnf-plugins-extras-repoclosure = %{version}-%{release}
Provides:       python3-dnf-plugins-extras-repograph = %{version}-%{release}
Provides:       python3-dnf-plugins-extras-repomanage = %{version}-%{release}
Provides:       python3-dnf-plugin-system-upgrade = %{version}-%{release}
%if %{with debug_plugin}
Obsoletes:      python3-dnf-plugins-extras-debug < %{dnf_plugins_extra}
%endif
Obsoletes:      python3-dnf-plugins-extras-repoclosure < %{dnf_plugins_extra}
Obsoletes:      python3-dnf-plugins-extras-repograph < %{dnf_plugins_extra}
Obsoletes:      python3-dnf-plugins-extras-repomanage < %{dnf_plugins_extra}
Obsoletes:      python3-dnf-plugin-system-upgrade < %{version}-%{release}

Conflicts:      %{name} <= 0.1.5
# let the both python plugin versions be updated simultaneously
Conflicts:      python2-%{name} < %{version}-%{release}
Conflicts:      python-%{name} < %{version}-%{release}

%description -n python3-%{name}
Core Plugins for DNF, Python 3 interface. This package enhances DNF with builddep,
config-manager, copr, %{?with_debug_plugin:debug, }debuginfo-install, download, needs-restarting,
groups-manager, repoclosure, repograph, repomanage, reposync, changelog,
repodiff, system-upgrade, offline-upgrade and offline-distrosync commands.
Additionally provides generate_completion_cache passive plugin.
%endif

%if %{with yumutils}
%package -n %{yum_utils_subpackage_name}
%if "%{yum_utils_subpackage_name}" == "dnf-utils"
Conflicts:      yum-utils < 1.1.31-520
%if 0%{?rhel} != 7
Provides:       yum-utils = %{version}-%{release}
%endif
%else
Provides:       dnf-utils = %{version}-%{release}
Obsoletes:      dnf-utils < %{version}-%{release}
%endif
Requires:       %{name} = %{version}-%{release}
%if %{with python3}
Requires:       python3-dnf >= %{dnf_lowest_compatible}
%else
Requires:       python2-dnf >= %{dnf_lowest_compatible}
%endif
Summary:        Yum-utils CLI compatibility layer

%description -n %{yum_utils_subpackage_name}
As a Yum-utils CLI compatibility layer, supplies in CLI shims for
debuginfo-install, repograph, package-cleanup, repoclosure, repomanage,
repoquery, reposync, repotrack, repodiff, builddep, config-manager,%{?with_debug_plugin: debug,}
download and yum-groups-manager that use new implementations using DNF.
%endif

%if %{with python2}
%package -n python2-dnf-plugin-leaves
Summary:        Leaves Plugin for DNF
Requires:       python2-%{name} = %{version}-%{release}
Provides:       python2-dnf-plugins-extras-leaves = %{version}-%{release}
%if !%{with python3}
Provides:       dnf-command(leaves)
Provides:       dnf-plugin-leaves = %{version}-%{release}
Provides:       dnf-plugins-extras-leaves = %{version}-%{release}
%endif
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python3-dnf-plugin-leaves < %{version}-%{release}
Obsoletes:      python2-dnf-plugins-extras-leaves < %{dnf_plugins_extra}

%description -n python2-dnf-plugin-leaves
Leaves Plugin for DNF, Python 2 version. List all installed packages
not required by any other installed package.
%endif

%if %{with python3}
%package -n python3-dnf-plugin-leaves
Summary:        Leaves Plugin for DNF
Requires:       python3-%{name} = %{version}-%{release}
Provides:       python3-dnf-plugins-extras-leaves = %{version}-%{release}
Provides:       dnf-command(leaves)
Provides:       dnf-plugin-leaves = %{version}-%{release}
Provides:       dnf-plugins-extras-leaves = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python2-dnf-plugin-leaves < %{version}-%{release}
Obsoletes:      python3-dnf-plugins-extras-leaves < %{dnf_plugins_extra}

%description -n python3-dnf-plugin-leaves
Leaves Plugin for DNF, Python 3 version. List all installed packages
not required by any other installed package.
%endif

%if 0%{?rhel} == 0 && %{with python2}
%package -n python2-dnf-plugin-local
Summary:        Local Plugin for DNF
Requires:       %{_bindir}/createrepo_c
Requires:       python2-%{name} = %{version}-%{release}
%if !%{with python3}
Provides:       dnf-plugin-local =  %{version}-%{release}
Provides:       dnf-plugins-extras-local = %{version}-%{release}
%endif
Provides:       python2-dnf-plugins-extras-local = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python3-dnf-plugin-local < %{version}-%{release}
Obsoletes:      python2-dnf-plugins-extras-local < %{dnf_plugins_extra}

%description -n python2-dnf-plugin-local
Local Plugin for DNF, Python 2 version. Automatically copy all downloaded packages to a
repository on the local filesystem and generating repo metadata.
%endif

%if %{with python3} && 0%{?rhel} == 0
%package -n python3-dnf-plugin-local
Summary:        Local Plugin for DNF
Requires:       %{_bindir}/createrepo_c
Requires:       python3-%{name} = %{version}-%{release}
Provides:       dnf-plugin-local =  %{version}-%{release}
Provides:       python3-dnf-plugins-extras-local = %{version}-%{release}
Provides:       dnf-plugins-extras-local = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python2-dnf-plugin-local < %{version}-%{release}
Obsoletes:      python3-dnf-plugins-extras-local < %{dnf_plugins_extra}

%description -n python3-dnf-plugin-local
Local Plugin for DNF, Python 3 version. Automatically copy all downloaded
packages to a repository on the local filesystem and generating repo metadata.
%endif

%if %{with python2}
%package -n python2-dnf-plugin-migrate
Summary:        Migrate Plugin for DNF
Requires:       python2-%{name} = %{version}-%{release}
Requires:       yum
Provides:       dnf-plugin-migrate = %{version}-%{release}
Provides:       python2-dnf-plugins-extras-migrate = %{version}-%{release}
Provides:       dnf-command(migrate)
Provides:       dnf-plugins-extras-migrate = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Obsoletes:      python2-dnf-plugins-extras-migrate < %{dnf_plugins_extra}
Obsoletes:      python-dnf-plugins-extras-migrate < %{dnf_plugins_extra}

%description -n python2-dnf-plugin-migrate
Migrate Plugin for DNF, Python 2 version. Migrates history, group and yumdb data from yum to dnf.
%endif

%if %{with python2}
%package -n python2-dnf-plugin-post-transaction-actions
Summary:        Post transaction actions Plugin for DNF
Requires:       python2-%{name} = %{version}-%{release}
%if !%{with python3}
Provides:       dnf-plugin-post-transaction-actions =  %{version}-%{release}
%endif
Conflicts:      python3-dnf-plugin-post-transaction-actions < %{version}-%{release}

%description -n python2-dnf-plugin-post-transaction-actions
Post transaction actions Plugin for DNF, Python 2 version. Plugin runs actions
(shell commands) after transaction is completed. Actions are defined in action
files.
%endif

%if %{with python3}
%package -n python3-dnf-plugin-post-transaction-actions
Summary:        Post transaction actions Plugin for DNF
Requires:       python3-%{name} = %{version}-%{release}
Provides:       dnf-plugin-post-transaction-actions =  %{version}-%{release}
Conflicts:      python2-dnf-plugin-post-transaction-actions < %{version}-%{release}

%description -n python3-dnf-plugin-post-transaction-actions
Post transaction actions Plugin for DNF, Python 3 version. Plugin runs actions
(shell commands) after transaction is completed. Actions are defined in action
files.
%endif

%if %{with python2}
%package -n python2-dnf-plugin-pre-transaction-actions
Summary:        Pre transaction actions Plugin for DNF
Requires:       python2-%{name} = %{version}-%{release}
%if !%{with python3}
Provides:       dnf-plugin-pre-transaction-actions =  %{version}-%{release}
%endif
Conflicts:      python3-dnf-plugin-pre-transaction-actions < %{version}-%{release}

%description -n python2-dnf-plugin-pre-transaction-actions
Pre transaction actions Plugin for DNF, Python 2 version. Plugin runs actions
(shell commands) before transaction is completed. Actions are defined in action
files.
%endif

%if %{with python3}
%package -n python3-dnf-plugin-pre-transaction-actions
Summary:        Pre transaction actions Plugin for DNF
Requires:       python3-%{name} = %{version}-%{release}
Provides:       dnf-plugin-pre-transaction-actions =  %{version}-%{release}
Conflicts:      python2-dnf-plugin-pre-transaction-actions < %{version}-%{release}

%description -n python3-dnf-plugin-pre-transaction-actions
Pre transaction actions Plugin for DNF, Python 3 version. Plugin runs actions
(shell commands) before transaction is completed. Actions are defined in action
files.
%endif

%if %{with python2}
%package -n python2-dnf-plugin-show-leaves
Summary:        Leaves Plugin for DNF
Requires:       python2-%{name} = %{version}-%{release}
Requires:       python2-dnf-plugin-leaves = %{version}-%{release}
%if !%{with python3}
Provides:       dnf-plugin-show-leaves =  %{version}-%{release}
Provides:       dnf-command(show-leaves)
Provides:       dnf-plugins-extras-show-leaves = %{version}-%{release}
%endif
Provides:       python2-dnf-plugins-extras-show-leaves = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python3-dnf-plugin-show-leaves < %{version}-%{release}
Obsoletes:      python2-dnf-plugins-extras-show-leaves < %{dnf_plugins_extra}

%description -n python2-dnf-plugin-show-leaves
Show-leaves Plugin for DNF, Python 2 version. List all installed
packages that are no longer required by any other installed package
after a transaction.
%endif

%if %{with python3}
%package -n python3-dnf-plugin-show-leaves
Summary:        Show-leaves Plugin for DNF
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3-dnf-plugin-leaves = %{version}-%{release}
Provides:       dnf-plugin-show-leaves =  %{version}-%{release}
Provides:       python3-dnf-plugins-extras-show-leaves = %{version}-%{release}
Provides:       dnf-command(show-leaves)
Provides:       dnf-plugins-extras-show-leaves = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python2-dnf-plugin-show-leaves < %{version}-%{release}
Obsoletes:      python3-dnf-plugins-extras-show-leaves < %{dnf_plugins_extra}

%description -n python3-dnf-plugin-show-leaves
Show-leaves Plugin for DNF, Python 3 version. List all installed
packages that are no longer required by any other installed package
after a transaction.
%endif

%if %{with python2}
%package -n python2-dnf-plugin-versionlock
Summary:        Version Lock Plugin for DNF
Requires:       python2-%{name} = %{version}-%{release}
%if !%{with python3}
Provides:       dnf-plugin-versionlock =  %{version}-%{release}
Provides:       dnf-command(versionlock)
Provides:       dnf-plugins-extras-versionlock = %{version}-%{release}
%if %{with yumcompatibility}
Provides:       yum-plugin-versionlock = %{version}-%{release}
%endif
%endif
Provides:       python2-dnf-plugins-extras-versionlock = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python3-dnf-plugin-versionlock < %{version}-%{release}
Obsoletes:      python2-dnf-plugins-extras-versionlock < %{dnf_plugins_extra}

%description -n python2-dnf-plugin-versionlock
Version lock plugin takes a set of name/versions for packages and excludes all other
versions of those packages. This allows you to e.g. protect packages from being
updated by newer versions.
%endif

%if %{with python3}
%package -n python3-dnf-plugin-versionlock
Summary:        Version Lock Plugin for DNF
Requires:       python3-%{name} = %{version}-%{release}
Provides:       dnf-plugin-versionlock =  %{version}-%{release}
Provides:       python3-dnf-plugins-extras-versionlock = %{version}-%{release}
Provides:       dnf-command(versionlock)
%if %{with yumcompatibility}
Provides:       yum-plugin-versionlock = %{version}-%{release}
%endif
Provides:       dnf-plugins-extras-versionlock = %{version}-%{release}
Conflicts:      dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:      python2-dnf-plugin-versionlock < %{version}-%{release}
Obsoletes:      python3-dnf-plugins-extras-versionlock < %{dnf_plugins_extra}

%description -n python3-dnf-plugin-versionlock
Version lock plugin takes a set of name/versions for packages and excludes all other
versions of those packages. This allows you to e.g. protect packages from being
updated by newer versions.
%endif

%if %{with python3}
%package -n python3-dnf-plugin-modulesync
Summary:        Download module metadata and packages and create repository
Requires:       python3-%{name} = %{version}-%{release}
Requires:       createrepo_c >= 0.17.4
Provides:       dnf-plugin-modulesync =  %{version}-%{release}
Provides:       dnf-command(modulesync)

%description -n python3-dnf-plugin-modulesync
Download module metadata from all enabled repositories, module artifacts and profiles of matching modules and create
repository.
%endif

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/dnf-plugins-core-4.10.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0f6966a6cb62912cd3520ef2a09ddfcdb48aa3091009f9834526b04f6de9a70a" || { echo "oreon: Source0 SHA256 mismatch for dnf-plugins-core-4.10.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1
%if %{with python2}
mkdir build-py2
%endif
%if %{with python3}
mkdir build-py3
%endif

%build
%if %{with python2}
pushd build-py2
  %cmake ../ -DPYTHON_DESIRED:FILEPATH=%{__python2} \
    -DWITHOUT_DEBUG:str=0%{!?with_debug_plugin:1} \
    -DWITHOUT_LOCAL:str=0%{?rhel}
  %cmake_build
  %cmake_build --target doc-man
popd
%endif
%if %{with python3}
pushd build-py3
  %cmake ../ -DPYTHON_DESIRED:FILEPATH=%{__python3} \
    -DWITHOUT_DEBUG:str=0%{!?with_debug_plugin:1} \
    -DWITHOUT_LOCAL:str=0%{?rhel}
  %cmake_build
  %cmake_build --target doc-man
popd
%endif

%install
%if %{with python2}
pushd build-py2
  %cmake_install
popd
%endif
%if %{with python3}
pushd build-py3
  %cmake_install
popd
%endif

%if %{with python3}
mkdir -p %{buildroot}%{_unitdir}/system-update.target.wants/
pushd %{buildroot}%{_unitdir}/system-update.target.wants/
  ln -sr ../dnf-system-upgrade.service
popd

ln -sf dnf4-system-upgrade.8.gz %{buildroot}%{_mandir}/man8/dnf4-offline-upgrade.8.gz
ln -sf dnf4-system-upgrade.8.gz %{buildroot}%{_mandir}/man8/dnf4-offline-distrosync.8.gz
%endif

%if %{without dnf5_obsoletes_dnf}
for file in %{buildroot}%{_mandir}/man8/dnf4[-.]*; do
    dir=$(dirname $file)
    filename=$(basename $file)
    ln -sf $filename $dir/${filename/dnf4/dnf}
done
%endif

%find_lang %{name}
%if %{with yumutils}
  %if %{with python3}
  mv %{buildroot}%{_libexecdir}/dnf-utils-3 %{buildroot}%{_libexecdir}/dnf-utils
  %else
  mv %{buildroot}%{_libexecdir}/dnf-utils-2 %{buildroot}%{_libexecdir}/dnf-utils
  %endif
%endif
rm -vf %{buildroot}%{_libexecdir}/dnf-utils-*

%if %{with yumutils}
mkdir -p %{buildroot}%{_bindir}
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/debuginfo-install
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/needs-restarting
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/find-repos-of-install
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repo-graph
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/package-cleanup
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repoclosure
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repodiff
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repomanage
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repoquery
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/reposync
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repotrack
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-builddep
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-config-manager
%if %{with debug_plugin}
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-debug-dump
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-debug-restore
%endif
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-groups-manager
ln -srf %{buildroot}%{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yumdownloader
# These commands don't have a dedicated man page, so let's just point them
# to the utils page which contains their descriptions.
ln -sf %{yum_utils_subpackage_name}.1.gz %{buildroot}%{_mandir}/man1/find-repos-of-install.1.gz
ln -sf %{yum_utils_subpackage_name}.1.gz %{buildroot}%{_mandir}/man1/repoquery.1.gz
ln -sf %{yum_utils_subpackage_name}.1.gz %{buildroot}%{_mandir}/man1/repotrack.1.gz
%endif

%check
%if %{with python2}
    pushd build-py2
    ctest -VV
    popd
%endif
%if %{with python3}
    pushd build-py3
    ctest -VV
    popd
%endif

%files
%{_mandir}/man8/dnf*-builddep.*
%{_mandir}/man8/dnf*-changelog.*
%{_mandir}/man8/dnf*-config-manager.*
%{_mandir}/man8/dnf*-copr.*
%if %{with debug_plugin}
%{_mandir}/man8/dnf*-debug.*
%endif
%{_mandir}/man8/dnf*-debuginfo-install.*
%{_mandir}/man8/dnf*-download.*
%{_mandir}/man8/dnf*-expired-pgp-keys.*
%{_mandir}/man8/dnf*-generate_completion_cache.*
%{_mandir}/man8/dnf*-groups-manager.*
%{_mandir}/man8/dnf*-needs-restarting.*
%{_mandir}/man8/dnf*-repoclosure.*
%{_mandir}/man8/dnf*-repodiff.*
%{_mandir}/man8/dnf*-repograph.*
%{_mandir}/man8/dnf*-repomanage.*
%{_mandir}/man8/dnf*-reposync.*
%{_mandir}/man8/dnf*-system-upgrade.*
%{_mandir}/man8/dnf*-offline-upgrade.*
%{_mandir}/man8/dnf*-offline-distrosync.*
%if %{with yumcompatibility}
%{_mandir}/man1/yum-changelog.*
%{_mandir}/man8/yum-copr.*
%else
%exclude %{_mandir}/man1/yum-changelog.*
%exclude %{_mandir}/man8/yum-copr.*
%endif

%if %{with python2}
%files -n python2-%{name} -f %{name}.lang
%license COPYING
%doc AUTHORS README.rst
%ghost %attr(644,-,-) %{_var}/cache/dnf/packages.db
%config(noreplace) %{_sysconfdir}/dnf/plugins/copr.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/copr.d
%config(noreplace) %{_sysconfdir}/dnf/plugins/debuginfo-install.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/expired-pgp-keys.conf
%{python2_sitelib}/dnf-plugins/builddep.*
%{python2_sitelib}/dnf-plugins/changelog.*
%{python2_sitelib}/dnf-plugins/config_manager.*
%{python2_sitelib}/dnf-plugins/copr.*
%{python2_sitelib}/dnf-plugins/debug.*
%{python2_sitelib}/dnf-plugins/debuginfo-install.*
%{python2_sitelib}/dnf-plugins/download.*
%{python2_sitelib}/dnf-plugins/generate_completion_cache.*
%{python2_sitelib}/dnf-plugins/groups_manager.*
%{python2_sitelib}/dnf-plugins/needs_restarting.*
%{python2_sitelib}/dnf-plugins/repoclosure.*
%{python2_sitelib}/dnf-plugins/repodiff.*
%{python2_sitelib}/dnf-plugins/repograph.*
%{python2_sitelib}/dnf-plugins/repomanage.*
%{python2_sitelib}/dnf-plugins/reposync.*
%{python2_sitelib}/dnfpluginscore/
%endif

%if %{with python3}
%files -n python3-%{name} -f %{name}.lang
%license COPYING
%doc AUTHORS README.rst
%ghost %attr(644,-,-) %{_var}/cache/dnf/packages.db
%config(noreplace) %{_sysconfdir}/dnf/plugins/copr.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/copr.d
%config(noreplace) %{_sysconfdir}/dnf/plugins/debuginfo-install.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/expired-pgp-keys.conf
%{python3_sitelib}/dnf-plugins/builddep.py
%{python3_sitelib}/dnf-plugins/changelog.py
%{python3_sitelib}/dnf-plugins/config_manager.py
%{python3_sitelib}/dnf-plugins/copr.py
%if %{with debug_plugin}
%{python3_sitelib}/dnf-plugins/debug.py
%endif
%{python3_sitelib}/dnf-plugins/debuginfo-install.py
%{python3_sitelib}/dnf-plugins/download.py
%{python3_sitelib}/dnf-plugins/expired-pgp-keys.py
%{python3_sitelib}/dnf-plugins/generate_completion_cache.py
%{python3_sitelib}/dnf-plugins/groups_manager.py
%{python3_sitelib}/dnf-plugins/needs_restarting.py
%{python3_sitelib}/dnf-plugins/repoclosure.py
%{python3_sitelib}/dnf-plugins/repodiff.py
%{python3_sitelib}/dnf-plugins/repograph.py
%{python3_sitelib}/dnf-plugins/repomanage.py
%{python3_sitelib}/dnf-plugins/reposync.py
%{python3_sitelib}/dnf-plugins/system_upgrade.py
%{python3_sitelib}/dnf-plugins/__pycache__/builddep.*
%{python3_sitelib}/dnf-plugins/__pycache__/changelog.*
%{python3_sitelib}/dnf-plugins/__pycache__/config_manager.*
%{python3_sitelib}/dnf-plugins/__pycache__/copr.*
%if %{with debug_plugin}
%{python3_sitelib}/dnf-plugins/__pycache__/debug.*
%endif
%{python3_sitelib}/dnf-plugins/__pycache__/debuginfo-install.*
%{python3_sitelib}/dnf-plugins/__pycache__/download.*
%{python3_sitelib}/dnf-plugins/__pycache__/expired-pgp-keys.*
%{python3_sitelib}/dnf-plugins/__pycache__/generate_completion_cache.*
%{python3_sitelib}/dnf-plugins/__pycache__/groups_manager.*
%{python3_sitelib}/dnf-plugins/__pycache__/needs_restarting.*
%{python3_sitelib}/dnf-plugins/__pycache__/repoclosure.*
%{python3_sitelib}/dnf-plugins/__pycache__/repodiff.*
%{python3_sitelib}/dnf-plugins/__pycache__/repograph.*
%{python3_sitelib}/dnf-plugins/__pycache__/repomanage.*
%{python3_sitelib}/dnf-plugins/__pycache__/reposync.*
%{python3_sitelib}/dnf-plugins/__pycache__/system_upgrade.*
%{python3_sitelib}/dnfpluginscore/
%{_unitdir}/dnf-system-upgrade.service
%{_unitdir}/dnf-system-upgrade-cleanup.service
%{_unitdir}/system-update.target.wants/dnf-system-upgrade.service
%endif

%if %{with yumutils}
%files -n %{yum_utils_subpackage_name}
%{_libexecdir}/dnf-utils
%{_bindir}/debuginfo-install
%{_bindir}/needs-restarting
%{_bindir}/find-repos-of-install
%{_bindir}/package-cleanup
%{_bindir}/repo-graph
%{_bindir}/repoclosure
%{_bindir}/repodiff
%{_bindir}/repomanage
%{_bindir}/repoquery
%{_bindir}/reposync
%{_bindir}/repotrack
%{_bindir}/yum-builddep
%{_bindir}/yum-config-manager
%if %{with debug_plugin}
%{_bindir}/yum-debug-dump
%{_bindir}/yum-debug-restore
%endif
%{_bindir}/yum-groups-manager
%{_bindir}/yumdownloader
%{_mandir}/man1/debuginfo-install.*
%{_mandir}/man1/needs-restarting.*
%{_mandir}/man1/repo-graph.*
%{_mandir}/man1/repoclosure.*
%{_mandir}/man1/repodiff.*
%{_mandir}/man1/repomanage.*
%{_mandir}/man1/reposync.*
%{_mandir}/man1/yum-builddep.*
%{_mandir}/man1/yum-config-manager.*
%if %{with debug_plugin}
%{_mandir}/man1/yum-debug-dump.*
%{_mandir}/man1/yum-debug-restore.*
%endif
%{_mandir}/man1/yum-groups-manager.*
%{_mandir}/man1/yumdownloader.*
%{_mandir}/man1/package-cleanup.*
%{_mandir}/man1/dnf-utils.*
%{_mandir}/man1/yum-utils.*
# These are only built with yumutils bcond.
%{_mandir}/man1/find-repos-of-install.*
%{_mandir}/man1/repoquery.*
%{_mandir}/man1/repotrack.*
%else
# These are built regardless of yumutils bcond so we need to exclude them.
%exclude %{_mandir}/man1/debuginfo-install.*
%exclude %{_mandir}/man1/needs-restarting.*
%exclude %{_mandir}/man1/repo-graph.*
%exclude %{_mandir}/man1/repoclosure.*
%exclude %{_mandir}/man1/repodiff.*
%exclude %{_mandir}/man1/repomanage.*
%exclude %{_mandir}/man1/reposync.*
%exclude %{_mandir}/man1/yum-builddep.*
%exclude %{_mandir}/man1/yum-config-manager.*
%exclude %{_mandir}/man1/yum-debug-dump.*
%exclude %{_mandir}/man1/yum-debug-restore.*
%exclude %{_mandir}/man1/yum-groups-manager.*
%exclude %{_mandir}/man1/yumdownloader.*
%exclude %{_mandir}/man1/package-cleanup.*
%exclude %{_mandir}/man1/dnf-utils.*
%exclude %{_mandir}/man1/yum-utils.*
%endif

%if %{with python2}
%files -n python2-dnf-plugin-leaves
%{python2_sitelib}/dnf-plugins/leaves.*
%{_mandir}/man8/dnf*-leaves.*
%endif

%if %{with python3}
%files -n python3-dnf-plugin-leaves
%{python3_sitelib}/dnf-plugins/leaves.*
%{python3_sitelib}/dnf-plugins/__pycache__/leaves.*
%{_mandir}/man8/dnf*-leaves.*
%endif

%if 0%{?rhel} == 0 && %{with python2}
%files -n python2-dnf-plugin-local
%config(noreplace) %{_sysconfdir}/dnf/plugins/local.conf
%{python2_sitelib}/dnf-plugins/local.*
%{_mandir}/man8/dnf*-local.*
%endif

%if %{with python3} && 0%{?rhel} == 0
%files -n python3-dnf-plugin-local
%config(noreplace) %{_sysconfdir}/dnf/plugins/local.conf
%{python3_sitelib}/dnf-plugins/local.*
%{python3_sitelib}/dnf-plugins/__pycache__/local.*
%{_mandir}/man8/dnf*-local.*
%endif

%if %{with python2}
%files -n python2-dnf-plugin-migrate
%{python2_sitelib}/dnf-plugins/migrate.*
%{_mandir}/man8/dnf-migrate.*
%else
%exclude %{_mandir}/man8/dnf-migrate.*
%endif

%if %{with python2}
%files -n python2-dnf-plugin-post-transaction-actions
%config(noreplace) %{_sysconfdir}/dnf/plugins/post-transaction-actions.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/post-transaction-actions.d
%{python2_sitelib}/dnf-plugins/post-transaction-actions.*
%{_mandir}/man8/dnf*-post-transaction-actions.*
%endif

%if %{with python3}
%files -n python3-dnf-plugin-post-transaction-actions
%config(noreplace) %{_sysconfdir}/dnf/plugins/post-transaction-actions.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/post-transaction-actions.d
%{python3_sitelib}/dnf-plugins/post-transaction-actions.*
%{python3_sitelib}/dnf-plugins/__pycache__/post-transaction-actions.*
%{_mandir}/man8/dnf*-post-transaction-actions.*
%endif

%if %{with python2}
%files -n python2-dnf-plugin-pre-transaction-actions
%config(noreplace) %{_sysconfdir}/dnf/plugins/pre-transaction-actions.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/pre-transaction-actions.d
%{python2_sitelib}/dnf-plugins/pre-transaction-actions.*
%{_mandir}/man8/dnf*-pre-transaction-actions.*
%endif

%if %{with python3}
%files -n python3-dnf-plugin-pre-transaction-actions
%config(noreplace) %{_sysconfdir}/dnf/plugins/pre-transaction-actions.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/pre-transaction-actions.d
%{python3_sitelib}/dnf-plugins/pre-transaction-actions.*
%{python3_sitelib}/dnf-plugins/__pycache__/pre-transaction-actions.*
%{_mandir}/man8/dnf*-pre-transaction-actions.*
%endif

%if %{with python2}
%files -n python2-dnf-plugin-show-leaves
%{python2_sitelib}/dnf-plugins/show_leaves.*
%{_mandir}/man8/dnf*-show-leaves.*
%endif

%if %{with python3}
%files -n python3-dnf-plugin-show-leaves
%{python3_sitelib}/dnf-plugins/show_leaves.*
%{python3_sitelib}/dnf-plugins/__pycache__/show_leaves.*
%{_mandir}/man8/dnf*-show-leaves.*
%endif

%if %{with python2}
%files -n python2-dnf-plugin-versionlock
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.list
%{python2_sitelib}/dnf-plugins/versionlock.*
%{_mandir}/man8/dnf*-versionlock.*
%if %{with yumcompatibility}
%{_mandir}/man8/yum-versionlock.*
%{_mandir}/man5/yum-versionlock.*
%else
%exclude %{_mandir}/man8/yum-versionlock.*
%exclude %{_mandir}/man5/yum-versionlock.*
%endif
%endif

%if %{with python3}
%files -n python3-dnf-plugin-versionlock
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.list
%{python3_sitelib}/dnf-plugins/versionlock.*
%{python3_sitelib}/dnf-plugins/__pycache__/versionlock.*
%{_mandir}/man8/dnf*-versionlock.*
%if %{with yumcompatibility}
%{_mandir}/man8/yum-versionlock.*
%{_mandir}/man5/yum-versionlock.*
%else
%exclude %{_mandir}/man8/yum-versionlock.*
%exclude %{_mandir}/man5/yum-versionlock.*
%endif
%endif

%if %{with python3}
%files -n python3-dnf-plugin-modulesync
%{python3_sitelib}/dnf-plugins/modulesync.*
%{python3_sitelib}/dnf-plugins/__pycache__/modulesync.*
%{_mandir}/man8/dnf*-modulesync.*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.10.1-9
- Prepare for Oreon 11 (RP1)
