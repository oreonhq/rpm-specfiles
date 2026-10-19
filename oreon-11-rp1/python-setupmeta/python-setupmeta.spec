%global source0_hash c1719697ac8407dd84018f5699121cdb4ec70bde28263b665a35e36f108aac29
Name:           python-setupmeta
Version:        3.9.0
Release:        1%{?dist}
Summary:        Simplify your setup.py
License:        MIT
URL:            https://pypi.org/pypi/setupmeta
Source0:        https://files.pythonhosted.org/packages/source/s/setupmeta/setupmeta-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-setupmeta = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-setupmeta
Summary:        Simplify your setup.py
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  git-core
%description -n python3-setupmeta

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir setupmeta-%{version}
%oreon_prep
%build

%pyproject_wheel
export PYTHONPATH=%{_pyproject_wheeldir}/setupmeta-0.0.0-py3-none-any.whl
%pyproject_wheel
rm %{_pyproject_wheeldir}/setupmeta-0.0.0-py3-none-any.whl
%install
%pyproject_install
%oreon_autofiles python3-setupmeta usr/lib/python3*/site-packages/setupmeta* usr/lib64/python3*/site-packages/setupmeta* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/setupmeta* usr/lib64/python3*/site-packages/setupmeta* usr/bin/*

%check

git config --global user.email "you@example.com"
git config --global user.name "Your Name"
%pytest -k "not test_check_dependencies"
%files
%files -n python3-setupmeta -f %{oreon_filedir}/python3-setupmeta.list

%changelog

%autochangelog
