%global source0_hash 54252968134b5e549ea5b872f1df1168bd7defe1a52fed5a358c194e1943ddc3
%global pypi_name jsonpath-ng
Name:           python-%{pypi_name}
Version:        1.8.0
Release:        1%{?dist}
Summary:        Implementation of JSONPath for Python
License:        Apache-2.0 AND WTFPL
URL:            https://github.com/h2non/jsonpath-ng
Source0:        https://files.pythonhosted.org/packages/source/j/jsonpath_ng/jsonpath_ng-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-jsonpath-ng = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-%{pypi_name}
Summary:        Implementation of JSONPath for Python
%description -n python3-%{pypi_name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jsonpath_ng-%{version}
sed -i -e '/^#!\//, 1d' jsonpath_ng/bin/jsonpath.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/jsonpath_ng* usr/lib64/python3*/site-packages/jsonpath_ng* usr/bin/*

%check

%{pytest} -v
%files
%files -n python3-jsonpath-ng -f %{oreon_filedir}/python3-jsonpath-ng.list

%changelog

%autochangelog
