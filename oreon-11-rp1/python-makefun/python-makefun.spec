%global source0_hash e14601831570bff1f6d7e68828bcd30d2f5856f24bad5de0ccb22921ceebc947
%bcond tests 0
Name:		python-makefun
Version:	1.16.0
Release:        1%{?dist}
Summary:        Dynamically create python functions with a proper signature
License:	BSD-3-Clause
URL:		https://pypi.org/project/makefun
Source0:        https://files.pythonhosted.org/packages/source/m/makefun/makefun-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 72
BuildRequires:  python3dist(setuptools) >= 39.2
Requires:       python3-makefun = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-makefun
Summary:        Dynamically create python functions with a proper signature
%{?python_provide:%python_provide python3-makefun}
%description -n python3-makefun

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n makefun-%{version}

cat >pyproject.toml <<EOF
[build-system]
requires = ["setuptools_scm", "pypandoc", "six", "wheel"]
build-backend = "setuptools.build_meta"
EOF

sed -r -i "s/'pandoc', //" setup.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-makefun usr/lib/python3*/site-packages/makefun* usr/lib64/python3*/site-packages/makefun* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/makefun* usr/lib64/python3*/site-packages/makefun* usr/bin/*
%if %{with tests}
%check

TESTOPTS=(
)
%pytest -v "${TESTOPTS[@]}"
%endif
%files
%files -n python3-makefun -f %{oreon_filedir}/python3-makefun.list

%changelog

%autochangelog
