# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8177f97513213526df2cf6184d8ff986c675afb514d4e68a404010521b880643
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

%global distro Oreon
%global major 11
%global release_name RP1

Name: oreon-release
Version: %{major}
Release: 1%{?dist}
Summary: %{distro} release files
License: GPL-2.0-or-later
URL: https://oreonhq.com/
BuildArch: noarch
Source0: LICENSE

BuildRequires: oreon-rpm-macros

Provides: system-release = %{version}-%{release}
Provides: system-release(releasever) = %{major}
Provides: system-release(releasever_major) = %{major}
Provides: base-module(platform:or%{major})
Requires: oreon-release-common = %{version}-%{release}
Conflicts: system-release

%description
Release files for %{distro} %{major}: os-release, the system-release
files, and the dist tag macros used by rpmbuild.

%package common
Summary: %{distro} release files shared by every edition
Provides: system-release-common = %{version}-%{release}

%description common
os-release, system-release-cpe, issue files, and the rpm dist macros for
%{distro} %{major}.

%prep
%oreon_sha256
%setup -c -T
cp -p %{SOURCE0} .

%build

%install
install -d -m 0755 %{buildroot}%{_sysconfdir} %{buildroot}%{_prefix}/lib %{buildroot}%{_rpmmacrodir} %{buildroot}%{_sysconfdir}/issue.d
echo "%{distro} release %{major} (%{release_name})" > %{buildroot}%{_sysconfdir}/oreon-release
ln -s oreon-release %{buildroot}%{_sysconfdir}/system-release
echo "cpe:/o:oreon:oreon:%{major}" > %{buildroot}%{_sysconfdir}/system-release-cpe

cat > %{buildroot}%{_prefix}/lib/os-release <<EOT
NAME="%{distro}"
VERSION="%{major} (%{release_name})"
ID=oreon
VERSION_ID=%{major}
VERSION_CODENAME=""
PLATFORM_ID="platform:or%{major}"
PRETTY_NAME="%{distro} %{major} (%{release_name})"
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:oreon:oreon:%{major}"
HOME_URL="https://oreonhq.com/"
DOCUMENTATION_URL="https://oreonhq.com/help"
BUG_REPORT_URL="https://github.com/oreonhq/rpm-specfiles/issues"
VENDOR_NAME="Oreon"
VENDOR_URL="https://oreonhq.com/"
EOT
ln -s ../usr/lib/os-release %{buildroot}%{_sysconfdir}/os-release

printf '\\S\nKernel \\r on an \\m\n\n' > %{buildroot}%{_sysconfdir}/issue
printf '\\S\nKernel \\r on an \\m\n' > %{buildroot}%{_sysconfdir}/issue.net

cat > %{buildroot}%{_rpmmacrodir}/macros.dist <<EOT
%%__bootstrap ~bootstrap
%%oreon %{major}
%%oreon_ver %{major}
%%distcore .or%{major}
%%dist %%{!?distprefix0:%%{?distprefix}}%%{expand:%%{lua:for i=0,9999 do print("%%{?distprefix" .. i .."}") end}}%%{distcore}%%{?distsuffix}%%{?with_bootstrap:%%{__bootstrap}}
%%dist_vendor Oreon
%%dist_name %{distro}
%%dist_home_url https://oreonhq.com/
%%dist_bug_report_url https://github.com/oreonhq/rpm-specfiles/issues
EOT

%files
%{_sysconfdir}/oreon-release
%{_sysconfdir}/system-release

%files common
%license LICENSE
%{_prefix}/lib/os-release
%{_sysconfdir}/os-release
%{_sysconfdir}/system-release-cpe
%config(noreplace) %{_sysconfdir}/issue
%config(noreplace) %{_sysconfdir}/issue.net
%dir %{_sysconfdir}/issue.d
%{_rpmmacrodir}/macros.dist
