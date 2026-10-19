%global source0_hash 4f3231eaa68302054808109b5676e8cfea7b819030a24a2c9d969593e739753a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%{?dlrn: %global tarsources ansible-collections-openstack.cloud}
%{!?dlrn: %global tarsources ansible-collections-openstack}
Name:           ansible-collections-openstack
Version:        2.6.0
Release:        1%{?dist}
Summary:        Openstack Ansible collections
License:        GPL-3.0-or-later
URL:            https://opendev.org/openstack/ansible-collections-openstack
Source0:        https://github.com/openstack/%{name}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch
%if %{lua:print(rpm.vercmp(rpm.expand("%{version}"), '2.6.0'));} <= 0
Patch0:         0001-Disable-auto-discovery-for-setuptools.patch
%endif
Requires:       ansible-core
Requires:       python3-openstacksdk >= 0.13.0
# oreon:deps
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
# /oreon:deps
%description
Openstack Ansible collections

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{tarsources}-%{upstream_version} -S git

%build

%py3_build
%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%py3_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
