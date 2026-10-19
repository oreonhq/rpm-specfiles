%global source0_hash ab02608d63f7baf14483682ee6213c9330401f2a14d7a63489b872f6830a9848
Name:           python-pytest-param-files
Version:        0.6.0
Release:        8%{?dist}
Summary:        Create pytest parametrize decorators from external files
License:        MIT
URL:            https://pypi.org/project/pytest_param_files/
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_param_files/pytest_param_files-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-pytest-param-files = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-param-files+codecov
Summary:        Metapackage for python3-pytest-param-files codecov extras
Requires:       python3-pytest-param-files = %{version}-%{release}
Provides:       python3dist(pytest-param-files[codecov]) = %{version}-%{release}

%description -n python3-pytest-param-files+codecov
Metapackage for python3-pytest-param-files codecov extras.

%description

%package -n     python3-pytest-param-files
Summary:        Create pytest parametrize decorators from external files
# oreon:reqs
Requires:       python3dist(ruamel.yaml) >= 0.15
# /oreon:reqs
%description -n python3-pytest-param-files

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest_param_files-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-param-files usr/lib/python3*/site-packages/pytest_param_files* usr/lib64/python3*/site-packages/pytest_param_files* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_param_files* usr/lib64/python3*/site-packages/pytest_param_files* usr/bin/*

%check

%pytest
%files
%files -n python3-pytest-param-files -f %{oreon_filedir}/python3-pytest-param-files.list

%changelog

%autochangelog
