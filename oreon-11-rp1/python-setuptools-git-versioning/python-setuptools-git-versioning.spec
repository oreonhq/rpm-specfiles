%global source0_hash 612dfcf184addac9e1c2216f4f229724b2390e5bf613fb925ae80b84f2529172
Name:           python-setuptools-git-versioning
Version:        3.1.0
Release:        1%{?dist}
Summary:        Use git repo data for building a version number according to PEP-440
License:        MIT
URL:            https://setuptools-git-versioning.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/s/setuptools_git_versioning/setuptools_git_versioning-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(tomli) >= 2.0.1
Requires:       python3-setuptools-git-versioning = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-setuptools-git-versioning
Summary:        Use git repo data for building a version number according to PEP-440
# oreon:reqs
Requires:       python3dist(tomli) >= 2.0.1
# /oreon:reqs
%description -n python3-setuptools-git-versioning

%prep
%global oreon_srcdir setuptools_git_versioning-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-setuptools-git-versioning usr/lib/python3*/site-packages/setuptools_git_versioning* usr/lib64/python3*/site-packages/setuptools_git_versioning* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/setuptools_git_versioning* usr/lib64/python3*/site-packages/setuptools_git_versioning* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-setuptools-git-versioning -f %{oreon_filedir}/python3-setuptools-git-versioning.list

%changelog

%autochangelog
