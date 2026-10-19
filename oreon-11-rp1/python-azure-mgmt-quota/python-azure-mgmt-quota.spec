%global source0_hash 73241af843763f2ad0a45b0af98d8c2a618cbe6b0f317ee198ec563db290bd15
%global         srcname azure-mgmt-quota
%global         upstream_version 3.0.1
Name:           python-%{srcname}
Version:        %{upstream_version}
Release:        1%{?dist}
Summary:        Microsoft Azure Quota Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        https://files.pythonhosted.org/packages/source/a/azure_mgmt_quota/azure_mgmt_quota-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-azure-mgmt-quota = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        Microsoft Azure Quota Management Client Library for Python
%description -n python3-%{srcname}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n azure_mgmt_quota-%{upstream_version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/azure_mgmt_quota* usr/lib64/python3*/site-packages/azure_mgmt_quota* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-azure-mgmt-quota -f %{oreon_filedir}/python3-azure-mgmt-quota.list

%changelog

%autochangelog
