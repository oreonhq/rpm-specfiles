%global source0_hash fe8609a5a77fa8ba8399ac15921cb2cc041c2ef458d5522ff6eb143ec3e37e2d
Name:           python-lion-pytorch
Version:        0.2.5
Release:        1%{?dist}
Summary:        Lion Optimizer - Pytorch
License:        MIT
URL:            https://pypi.org/project/lion-pytorch/
Source0:        https://files.pythonhosted.org/packages/source/l/lion_pytorch/lion_pytorch-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-lion-pytorch = %{version}-%{release}
# /oreon:deps
%package -n       python3-lion-pytorch+test
Summary:        Metapackage for python3-lion-pytorch test extras
Requires:       python3-lion-pytorch = %{version}-%{release}
Provides:       python3dist(lion-pytorch[test]) = %{version}-%{release}

%description -n python3-lion-pytorch+test
Metapackage for python3-lion-pytorch test extras.

%description

%package -n     python3-lion-pytorch
Summary:        Lion Optimizer - Pytorch
# oreon:reqs
Requires:       python3dist(torch) >= 1.6
# /oreon:reqs
%description -n python3-lion-pytorch

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir lion_pytorch-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lion-pytorch usr/lib/python3*/site-packages/lion_pytorch* usr/lib64/python3*/site-packages/lion_pytorch* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lion_pytorch* usr/lib64/python3*/site-packages/lion_pytorch* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-lion-pytorch -f %{oreon_filedir}/python3-lion-pytorch.list

%changelog

%autochangelog
