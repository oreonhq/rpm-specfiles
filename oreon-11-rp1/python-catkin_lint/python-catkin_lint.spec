%global source0_hash 67df66e327579500e4c465348c2dd9aa8238f0b0268ded4e156bc0f304abaf5a
Name:           python-catkin-lint
Version:        1.6.25
Release:        1%{?dist}
Summary:        Check catkin packages for common errors
License:        ...
URL:            https://github.com/fkie/catkin_lint
Source0:        https://files.pythonhosted.org/packages/source/c/catkin_lint/catkin_lint-%{version}.tar.gz
BuildArch:      noarch
Patch:          0001-Handle-changed-ntpath.isabs-behaviour-in-Python-3.13.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-catkin-lint = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-catkin-lint
Summary:        Check catkin packages for common errors
%description -n python3-catkin-lint

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir catkin_lint-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-catkin-lint usr/lib/python3*/site-packages/catkin_lint* usr/lib64/python3*/site-packages/catkin_lint* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/catkin_lint* usr/lib64/python3*/site-packages/catkin_lint* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-catkin-lint -f %{oreon_filedir}/python3-catkin-lint.list

%changelog

%autochangelog
