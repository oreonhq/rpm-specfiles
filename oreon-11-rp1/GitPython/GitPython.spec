%global source0_hash fb92310af6844d96adc95ca066ed2e617c00e1dbd146a326626c81e72e18cc2e
%global srcname GitPython
Name:           %{srcname}
Version:        3.2.0
Release:        1%{?dist}
Summary:        Python Git Library
License:        BSD-3-Clause
URL:            https://github.com/gitpython-developers/GitPython
Source0:        https://files.pythonhosted.org/packages/source/g/gitpython/gitpython-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 62.6
Requires:       python3-GitPython = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{srcname}
Summary:        Python Git Library
BuildRequires:  python3-devel
BuildRequires:  git-core
Requires:       git-core
%description -n python3-%{srcname}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gitpython-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/GitPython* usr/lib64/python3*/site-packages/GitPython* usr/bin/*

%check

%pyproject_check_import
%files

%changelog

%autochangelog
