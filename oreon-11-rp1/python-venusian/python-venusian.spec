%global source0_hash 534fb3b355669283eb3954581931e5d1d071fce61d029d58f3219a5e3a6f0c41
Name:           python-venusian
Version:        3.1.1
Release:        1%{?dist}
Summary:        A library for deferring decorator actions
License:        BSD-3-Clause-Modification AND ZPL-2.1
URL:            https://github.com/Pylons/venusian
Source0:        https://files.pythonhosted.org/packages/source/v/venusian/venusian-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
Venusian is a library which allows framework authors to defer decorator
actions. Instead of taking actions when a function (or class) decorator is
executed at import time, you can defer the action usually taken by the
decorator until a separate “scan” phase.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.9.0
Requires:       python3-venusian = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-venusian
Summary:        A library for deferring decorator actions
%description -n python3-venusian %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n venusian-%{version} -p1

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/ --cov[^[:blank:]]*//g' setup.cfg

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-venusian usr/lib/python3*/site-packages/venusian* usr/lib64/python3*/site-packages/venusian* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/venusian* usr/lib64/python3*/site-packages/venusian* usr/bin/*

%check

%pytest
%files
%files -n python3-venusian -f %{oreon_filedir}/python3-venusian.list

%changelog

%autochangelog
