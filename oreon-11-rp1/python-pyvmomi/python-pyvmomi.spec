%global source0_hash eeed490ca13b7bdc055d6c514d3a905aba6a10cf2749a8fb514790e7d515d3ee

%global srcname pyvmomi

%global desc %{expand:
pyVmomi is the Python SDK for the vSphere API that allows you to manage\
ESX, ESXi, and vCenter.}

Name:           python-%{srcname}
Version:        9.0.0.0
Release:        1%{?dist}
Summary:        vSphere Python SDK
License:        Apache-2.0
URL:            https://github.com/vmware/%{srcname}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

# Downstream only patch:
# Remove un-needed test deps.  Changed to use pytest.

Patch0:         00-test-requirements.patch
BuildArch:      noarch

%description %desc

%dnl---------------------------------------------------------------------------
%package -n     python3-%{srcname}
Summary:        vSphere SDK for Python3
BuildRequires:  python3-devel
BuildRequires:  dos2unix
BuildRequires:  pytest

%description -n python3-%{srcname} %desc

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

# fix line endings
find . -name '*' -exec dos2unix -o {} \;

# shebang fix
find . -name '*.py' -exec sed -i 's@/usr/bin/env python@@' {} \;

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyVmomi pyVim vsanapiutils vsanmgmtObjects

%check
%tox

%changelog
%autochangelog
