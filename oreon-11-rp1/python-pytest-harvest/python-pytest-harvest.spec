%global source0_hash 27cfa4cf1f2e43d1e7749c282e0fe72d30e90e89bede6b30a59b626848c7d418
Name:		python-pytest-harvest
Version:	1.10.5
Release:        1%{?dist}
Summary:        Store data created during test execution and retrieve it at the end
License:	BSD-3-Clause
URL:		https://pypi.org/project/pytest-harvest/
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-harvest/pytest-harvest-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 39.2
Requires:       python3-pytest-harvest = %{version}-%{release}
# /oreon:deps
%description
Store data created during your pytest tests execution, and retrieve it
at the end of the session, e.g. for applicative benchmarking purposes.

%package -n python3-pytest-harvest
Summary:        Store data created during test execution and retrieve it at the end
%{?python_provide:%python_provide python3-pytest-harvest}
%description -n python3-pytest-harvest
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pytest-harvest-%{version} -p1

cat >pyproject.toml <<EOF
[build-system]
requires = ["setuptools_scm",
            "wheel",
            "pandas",
            "tabulate",
	    "pypandoc",
	    "six"]
build-backend = "setuptools.build_meta"
EOF

sed -r -i "s/'pandoc', //" setup.py

mv -i -v pytest_harvest/tests/conftest.py .

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-harvest usr/lib/python3*/site-packages/pytest_harvest* usr/lib64/python3*/site-packages/pytest_harvest* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_harvest* usr/lib64/python3*/site-packages/pytest_harvest* usr/bin/*

%check

%python3 -m pytest -v || :
%files
%files -n python3-pytest-harvest -f %{oreon_filedir}/python3-pytest-harvest.list

%changelog

%autochangelog
