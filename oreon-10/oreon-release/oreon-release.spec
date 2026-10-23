%global distro  Oreon
%define release_name    10 Core 'Foxy'
%global major   10
%global minor   0
%global dist .el10

Name:           oreon-release
Version:        %{major}.%{minor}
Release:        11%{?dist}.0
Summary:        %{distro} release files
License:        GPL-2.0-or-later
URL:            https://oreonproject.org/oreon-10

Provides:       centos-release = %{version}-%{release}
Provides:       centos-stream-release = %{version}-%{release}
Provides:       oreon-release = %{version}-%{release}

# When running a compose for ELN, we want to make sure that we pull in the
# correct templates when lorax is installed. This Suggests: will clue
# libdnf to use this set of templates instead of lorax-templates-generic.
Suggests: lorax-templates-almalinux

# Required for a lorax run (to generate install media)
Requires:       oreon-repos = %{version}-%{release}
Provides:       centos-release-eula
Provides:       redhat-release-eula

# required by epel-release
Provides:       redhat-release = %{version}-%{release}

# required by dnf
# https://github.com/rpm-software-management/dnf/blob/4.2.23/dnf/const.py.in#L26
Provides:       system-release = %{version}-%{release}
Provides:       system-release(releasever) = %{major}
Conflicts:      system-release

# required by libdnf
# https://github.com/rpm-software-management/libdnf/blob/0.48.0/libdnf/module/ModulePackage.cpp#L472
Provides:       base-module(platform:el%{major})

Source200:      EULA
Source201:      LICENSE

Source300:      85-display-manager.preset
Source301:      90-default.preset
Source302:      90-default-user.preset
Source303:      99-default-disable.preset
Source304:      50-redhat.conf

Source400:      alsecureboot001.cer

Source500:      oreon-appstream.repo
Source501:      oreon-baseos.repo
Source502:      oreon-crb.repo
Source503:      oreon-extras-common.repo
Source504:      oreon-highavailability.repo
Source505:      oreon-resilientstorage.repo
Source506:      oreon-sap.repo
Source507:      oreon-saphana.repo
# Only for x86_64
Source510:      oreon-nfv.repo
Source511:      oreon-rt.repo


Source600:      RPM-GPG-KEY-Oreon-10


%package -n oreon-sb-certs
Summary: %{distro} public secureboot certificates
Group: System Environment/Base
Provides: system-sb-certs = %{version}-%{release}
Provides: redhat-sb-certs = %{version}-%{release}
Provides: centos-sb-certs = %{version}-%{release}
Provides: oreon-sb-certs = %{version}-%{release}

%package -n oreon-repos
Summary:        %{distro} package repositories
Requires:       oreon-release = %{version}-%{release}
Requires:       oreon-gpg-keys = %{version}-%{release}
# Required by CentOS SIGs release packages
Provides:       centos-stream-repos = %{version}-%{release}

%package -n oreon-gpg-keys
Summary:        %{distro} RPM keys
# Required by CentOS SIGs release packages
Provides:       centos-gpg-keys = %{version}-%{release}

%description
%{distro} release files.

%description -n oreon-sb-certs
%{distro} secureboot certificates

%description -n oreon-repos
This package provides the package repository files for %{distro}.

%description -n oreon-gpg-keys
This package provides the RPM signature keys for %{distro}.

%install
# copy license and contributors doc here for %%license and %%doc macros
mkdir -p ./docs
cp %{SOURCE201} ./docs

# create /etc/system-release and /etc/redhat-release
install -d -m 0755 %{buildroot}%{_sysconfdir}
echo "%{distro} release %{major} (%{release_name})" > %{buildroot}%{_sysconfdir}/oreon-release
ln -s oreon-release %{buildroot}%{_sysconfdir}/system-release
ln -s oreon-release %{buildroot}%{_sysconfdir}/redhat-release

# -------------------------------------------------------------------------
# Definitions for /etc/os-release and for macros in macros.dist.  These
# macros are useful for spec files where distribution-specific identifiers
# are used to customize packages.

# Name of vendor / name of distribution. Typically used to identify where
# the binary comes from in --help or --version messages of programs.
# Examples: gdb.spec, clang.spec
%global dist_vendor Oreon HQ
%global dist_name   %{distro}

# URL of the homepage of the distribution
# Example: gstreamer1-plugins-base.spec
%global dist_home_url https://oreonhq.com/

# Bugzilla / bug reporting URLs shown to users.
# Examples: gcc.spec
%global dist_bug_report_url https://oreonhq.com/help

# debuginfod server, as used in elfutils.spec.
# %global dist_debuginfod_url https://debuginfod.centos.org/
# -------------------------------------------------------------------------


# Create the os-release file
install -d -m 0755 %{buildroot}%{_prefix}/lib
cat > %{buildroot}%{_prefix}/lib/os-release << EOF
NAME="Oreon"
VERSION="10"
ID="oreon"
ID_LIKE="rhel centos fedora"
VERSION_ID="10"
PLATFORM_ID="platform:el10"
PRETTY_NAME="Oreon 10"
ANSI_COLOR="0;34"
LOGO="fedora-logo-icon"
CPE_NAME="cpe:/o:oreon:oreon:%{major}::baseos"
HOME_URL="%{dist_home_url}"
DOCUMENTATION_URL="https://oreonhq.com/help"
VENDOR_NAME="Oreon"
VENDOR_URL="https://oreonhq.com"
BUG_REPORT_URL="%{dist_bug_report_url}"

OREON_MANTISBT_PROJECT="Oreon-%{major}"
OREON_MANTISBT_PROJECT_VERSION="%{major}"
REDHAT_SUPPORT_PRODUCT="Oreon"
REDHAT_SUPPORT_PRODUCT_VERSION="%{major}"
EOF

# Should be added to os-release in the future
# SUPPORT_END=%{eol_date}

# Create the symlink for /etc/os-release
ln -s ../usr/lib/os-release %{buildroot}%{_sysconfdir}/os-release

# write cpe to /etc/system/release-cpe
echo "cpe:/o:oreon:oreon:%{major}::baseos" > %{buildroot}%{_sysconfdir}/system-release-cpe

# create /etc/issue, /etc/issue.net and /etc/issue.d
echo '\S' > %{buildroot}%{_sysconfdir}/issue
echo 'Kernel \r on an \m' >> %{buildroot}%{_sysconfdir}/issue
cp %{buildroot}%{_sysconfdir}/issue{,.net}
echo >> %{buildroot}%{_sysconfdir}/issue
mkdir -p %{buildroot}%{_sysconfdir}/issue.d

# set up the dist tag macros
mkdir -p %{buildroot}%{_rpmmacrodir}
cat > %{buildroot}%{_rpmmacrodir}/macros.dist << EOF
# dist macros.

%%__bootstrap ~bootstrap
%%oreon_ver %{major}
%%oreon %{major}
%%centos_ver %{major}
%%centos %{major}
%%rhel %{major}
%%el%{major} 1
%%distcore            .el%{major}
%%dist %%{!?distprefix0:%%{?distprefix}}%%{expand:%%{lua:for i=0,9999 do print("%%{?distprefix" .. i .."}") end}}%%{distcore}%%{?distsuffix}%%{?with_bootstrap:%{__bootstrap}}
%%dist_vendor         %{dist_vendor}
%%dist_name           %{dist_name}
%%dist_home_url       %{dist_home_url}
%%dist_bug_report_url %{dist_bug_report_url}
EOF

# use unbranded datadir
install -d -m 0755 %{buildroot}%{_datadir}/oreon-release
ln -s oreon-release %{buildroot}%{_datadir}/redhat-release
install -p -m 0644 %{SOURCE200} %{buildroot}%{_datadir}/oreon-release/

# copy systemd presets
install -d -m 0755 %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -d -m 0755 %{buildroot}%{_prefix}/lib/systemd/user-preset
install -p -m 0644 %{SOURCE300} %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -p -m 0644 %{SOURCE301} %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -p -m 0644 %{SOURCE302} %{buildroot}%{_prefix}/lib/systemd/user-preset/

# installing the same file for both system and user presets to set the same behavior for both
install -p -m 0644 %{SOURCE303} %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -p -m 0644 %{SOURCE303} %{buildroot}%{_prefix}/lib/systemd/user-preset/

# copy sysctl presets
mkdir -p %{buildroot}/%{_prefix}/lib/sysctl.d/
install -m 0644 %{SOURCE304} %{buildroot}/%{_prefix}/lib/sysctl.d/

# Create stub yum repos
mkdir %{buildroot}%{_sysconfdir}/yum.repos.d
touch %{buildroot}%{_sysconfdir}/yum.repos.d/redhat.repo

# Copy secureboot certificates
install -d -m 0755 %{buildroot}%{_sysconfdir}/pki/sb-certs/
install -d -m 0755 %{buildroot}%{_datadir}/pki/sb-certs/

# Install aarch64 certs
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-aarch64.cer
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-aarch64.cer
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-aarch64.cer
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-fwupd-aarch64.cer
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-aarch64.cer


# Install x86_64 certs
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-x86_64.cer
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-x86_64.cer
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-x86_64.cer
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-fwupd-x86_64.cer
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-x86_64.cer

# Install ppc64le certs
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-ppc64le.cer
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-ppc64le.cer
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-ppc64le.cer
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-ppc64le.cer

# Install s390x certs
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-s390x.cer
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-s390x.cer
install -m 644 %{SOURCE400} %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-s390x.cer

# Link x86_64 certs
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-x86_64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-ca-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-x86_64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-kernel-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-x86_64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-grub2-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-fwupd-x86_64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-fwupd-x86_64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-x86_64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-uki-virt-x86_64.cer

# Link aarch64 certs
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-aarch64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-ca-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-aarch64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-kernel-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-aarch64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-grub2-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-fwupd-aarch64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-fwupd-aarch64.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-aarch64.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-uki-virt-aarch64.cer

# Link ppc64le certs
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-ppc64le.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-ca-ppc64le.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-ppc64le.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-kernel-ppc64le.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-grub2-ppc64le.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-grub2-ppc64le.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-ppc64le.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-uki-virt-ppc64le.cer

# Link s390x certs
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-ca-s390x.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-ca-s390x.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-kernel-s390x.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-kernel-s390x.cer
ln -sr %{buildroot}%{_datadir}/pki/sb-certs/secureboot-uki-virt-s390x.cer %{buildroot}%{_sysconfdir}/pki/sb-certs/secureboot-uki-virt-s390x.cer

# copy yum repos
install -d -m 0755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -m 0644 %{SOURCE500} %{buildroot}%{_sysconfdir}/yum.repos.d/
install -p -m 0644 %{SOURCE501} %{buildroot}%{_sysconfdir}/yum.repos.d/
install -p -m 0644 %{SOURCE502} %{buildroot}%{_sysconfdir}/yum.repos.d/
install -p -m 0644 %{SOURCE503} %{buildroot}%{_sysconfdir}/yum.repos.d/
install -p -m 0644 %{SOURCE504} %{buildroot}%{_sysconfdir}/yum.repos.d/
install -p -m 0644 %{SOURCE505} %{buildroot}%{_sysconfdir}/yum.repos.d/
install -p -m 0644 %{SOURCE506} %{buildroot}%{_sysconfdir}/yum.repos.d/
install -p -m 0644 %{SOURCE507} %{buildroot}%{_sysconfdir}/yum.repos.d/
# RT and NFV are only for x86_64
%ifarch x86_64
install -p -m 0644 %{SOURCE510} %{buildroot}%{_sysconfdir}/yum.repos.d/
install -p -m 0644 %{SOURCE511} %{buildroot}%{_sysconfdir}/yum.repos.d/
%endif

%if %{with beta}
install -p -m 0644 %{SOURCE512} %{buildroot}%{_sysconfdir}/yum.repos.d/
%endif

# Replace basearch to x86_64_v2
%ifarch x86_64_v2
sed -i "s/\$basearch/x86_64_v2/g" %{buildroot}%{_sysconfdir}/yum.repos.d/*.repo
sed -i '/^mirrorlist=/ s|$|?arch=x86_64_v2|g' %{buildroot}%{_sysconfdir}/yum.repos.d/*.repo
%endif

# dnf variables
install -d -m 0755 %{buildroot}%{_sysconfdir}/dnf/vars
echo "%{major}-stream" > %{buildroot}%{_sysconfdir}/dnf/vars/stream

# copy GPG keys
install -d -m 0755 %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -p -m 0644 %{SOURCE600} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/

# These variables should be set in the build environment to change rpm names
mkdir -p %{buildroot}%{_sysconfdir}/rpm
%ifarch x86_64_v2
echo '%%_target_platform x86_64-%%{_vendor}-%%{_target_os}%%{?_gnu}' >> %{buildroot}%{_sysconfdir}/rpm/macros.x86_64_v2
echo '%%x86_64_v2 1' >> %{buildroot}%{_sysconfdir}/rpm/macros.x86_64_v2
%endif


%files
%license docs/LICENSE
%{_sysconfdir}/redhat-release
%{_sysconfdir}/system-release
%{_sysconfdir}/oreon-release
%config(noreplace) %{_sysconfdir}/os-release
%config %{_sysconfdir}/system-release-cpe
%config(noreplace) %{_sysconfdir}/issue
%config(noreplace) %{_sysconfdir}/issue.net
%dir %{_sysconfdir}/issue.d
%dir %{_sysconfdir}/yum.repos.d
%ghost %{_sysconfdir}/yum.repos.d/redhat.repo
%{_rpmmacrodir}/macros.dist
%{_datadir}/redhat-release
%{_datadir}/oreon-release
%{_prefix}/lib/os-release
%{_prefix}/lib/systemd/system-preset/*
%{_prefix}/lib/systemd/user-preset/*
%{_prefix}/lib/sysctl.d/50-redhat.conf
%ifarch x86_64_v2
%config(noreplace) %{_sysconfdir}/rpm/macros.x86_64_v2
%endif

%files -n oreon-sb-certs
# Note to future packagers:
# resetting the symlinks in /etc/pki/sb-certs on upgrade is the intended behavior here
%dir %{_sysconfdir}/pki/sb-certs
%dir %{_datadir}/pki/sb-certs/
%{_sysconfdir}/pki/sb-certs/*.cer
%{_datadir}/pki/sb-certs/*.cer

%files -n oreon-repos
%config(noreplace) %{_sysconfdir}/yum.repos.d/oreon-appstream.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/oreon-baseos.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/oreon-crb.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/oreon-extras-common.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/oreon-highavailability.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/oreon-resilientstorage.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/oreon-sap.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/oreon-saphana.repo
%ifarch x86_64
%config(noreplace) %{_sysconfdir}/yum.repos.d/oreon-nfv.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/oreon-rt.repo
%endif
%if %{with beta}
%config(noreplace) %{_sysconfdir}/yum.repos.d/oreon-beta.repo
%endif
%config(noreplace) %{_sysconfdir}/dnf/vars/stream


%files -n oreon-gpg-keys
%{_sysconfdir}/pki/rpm-gpg

%changelog
%autochangelog
