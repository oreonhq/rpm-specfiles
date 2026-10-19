%global source0_hash c046801442fd39c9f6a265ebd9dd536ca8310a0e805be3e5ace6b11629de4d80
Name:           python-pygments-git
Version:        1.9.0
Release:        1%{?dist}
Summary:        Pygments lexers for Git output and files.
License:        MIT
URL:            https://github.com/adamchainz/pygments-git
Source0:        https://files.pythonhosted.org/packages/source/p/pygments_git/pygments_git-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-pygments-git = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pygments-git
Summary:        Pygments lexers for Git output and files.
%description -n python3-pygments-git

%prep
%global oreon_srcdir pygments_git-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygments-git usr/lib/python3*/site-packages/pygments_git* usr/lib64/python3*/site-packages/pygments_git* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pygments_git* usr/lib64/python3*/site-packages/pygments_git* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pygments-git -f %{oreon_filedir}/python3-pygments-git.list

%changelog

%autochangelog
