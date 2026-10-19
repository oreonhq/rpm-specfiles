%global source0_hash 5f9e8a29b4a8e55ddd740216ddb0a8a5e97f1c9c7f6bfdac91863473a8c60f9c
Name:           python-pytest-gitconfig
Version:        0.9.0
Release:        1%{?dist}
Summary:        Provide a Git config sandbox for testing
License:        MIT
URL:            https://github.com/noirbizarre/pytest-gitconfig
VCS:            git:%{url}.git
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_gitconfig/pytest_gitconfig-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytest-gitconfig = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytest-gitconfig
Summary:        Provide a Git config sandbox for testing
# oreon:reqs
Requires:       python3dist(pytest) >= 7.1.2
# /oreon:reqs
%description -n python3-pytest-gitconfig

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest_gitconfig-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-gitconfig usr/lib/python3*/site-packages/pytest_gitconfig* usr/lib64/python3*/site-packages/pytest_gitconfig* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_gitconfig* usr/lib64/python3*/site-packages/pytest_gitconfig* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-pytest-gitconfig -f %{oreon_filedir}/python3-pytest-gitconfig.list

%changelog

%autochangelog
