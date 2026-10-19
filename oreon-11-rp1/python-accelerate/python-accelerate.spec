%global source0_hash 5654f8c5eaa0d4fa68b33e287a97765da6849bf6d51dcac874e73fbbddfb6134
Name:           python-accelerate
Version:        1.15.0
Release:        1%{?dist}
Summary:        Accelerate
License:        ...
URL:            https://github.com/huggingface/accelerate
Source0:        https://files.pythonhosted.org/packages/source/a/accelerate/accelerate-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-accelerate = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-accelerate
Summary:        Accelerate
%description -n python3-accelerate

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir accelerate-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-accelerate usr/lib/python3*/site-packages/accelerate* usr/lib64/python3*/site-packages/accelerate* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/accelerate* usr/lib64/python3*/site-packages/accelerate* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-accelerate -f %{oreon_filedir}/python3-accelerate.list

%changelog

%autochangelog
