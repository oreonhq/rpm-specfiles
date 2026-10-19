%global source0_hash 73b8b65163ebf10f9f671efab9eed3d56f20d2ca68bda83fa64740a92c08f65d
Name:           python-pytest-sugar
Version:        1.1.1
Release:        1%{?dist}
Summary:        Change the default look and feel of pytest
License:        BSD-3-Clause
URL:            https://pypi.org/project/pytest-sugar
Source0:        https://files.pythonhosted.org/packages/source/p/pytest-sugar/pytest-sugar-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 40.6.0
Requires:       python3-pytest-sugar = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-pytest-sugar
Summary:        Change the default look and feel of pytest
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}
%description -n python3-pytest-sugar

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest-sugar-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-sugar usr/lib/python3*/site-packages/pytest_sugar* usr/lib64/python3*/site-packages/pytest_sugar* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_sugar* usr/lib64/python3*/site-packages/pytest_sugar* usr/bin/*

%check

PYTHONPATH=. %{pytest} -v -s
%files
%files -n python3-pytest-sugar -f %{oreon_filedir}/python3-pytest-sugar.list

%changelog

%autochangelog
