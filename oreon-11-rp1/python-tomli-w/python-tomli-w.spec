%global source0_hash 3b423098831faf35be897c5018c93e7c67eabf95d3359e1d5e97e5a4c0265ace
%bcond_without check
Name:           python-tomli-w
Version:        1.2.0
Release:        1%{?dist}
Summary:        A Python library for writing TOML
License:        MIT
URL:            https://github.com/hukkin/tomli-w
Source0:        https://github.com/hukkin/tomli-w/archive/refs/tags/1.2.0.tar.gz#/tomli-w-1.2.0.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2.0
Requires:       python3-tomli-w = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-tomli-w
Summary:        A Python library for writing TOML
%description -n python3-tomli-w

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n tomli-w-%{version}
# Measuring coverage is discouraged in Python packaging guidelines:
sed -i '/pytest-cov/d' tests/requirements.txt
# We don't need tomli on Python 3.11+
%if v"%{python3_version}" >= v"3.11"
sed -i '/tomli/d' tests/requirements.txt
sed -Ei 's/tomli(\.|$)/tomllib\1/' tests/*.py
%endif
# This testing dependency is optional and we don't have it in (EP)EL,
# it has many missing transitive dependencies that we don't want to maintain

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-tomli-w usr/lib/python3*/site-packages/tomli_w* usr/lib64/python3*/site-packages/tomli_w* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tomli_w* usr/lib64/python3*/site-packages/tomli_w* usr/bin/*

%check

%pyproject_check_import tomli_w
%if %{with check}
%pytest -v
%endif
%files
%files -n python3-tomli-w -f %{oreon_filedir}/python3-tomli-w.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-1
- Prepare for Oreon 11 (RP1)
