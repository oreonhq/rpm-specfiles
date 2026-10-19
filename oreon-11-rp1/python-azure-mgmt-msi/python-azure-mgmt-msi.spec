%global source0_hash 1a01a089f1f66cb0d4b2886603d5ba415f360eff0be6f685737ecdd59c78225b
%bcond_with     tests
%global         srcname     azure-mgmt-msi
Name:           python-%{srcname}
Version:        7.1.0
Release:        1%{?dist}
Summary:        Microsoft Azure MSI Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        https://files.pythonhosted.org/packages/source/a/azure_mgmt_msi/azure_mgmt_msi-%{version}.tar.gz
BuildArch:      noarch
Epoch:          1
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-azure-mgmt-msi = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        Microsoft Azure MSI Management Client Library for Python
%description -n python3-%{srcname}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir azure_mgmt_msi-%{version}
%oreon_prep
%build

%pyproject_wheel
%check

%pyproject_check_import
%if %{with tests}
%pytest
%endif
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/azure_mgmt_msi* usr/lib64/python3*/site-packages/azure_mgmt_msi* usr/bin/*

%files
%files -n python3-azure-mgmt-msi -f %{oreon_filedir}/python3-azure-mgmt-msi.list

%changelog

%autochangelog
