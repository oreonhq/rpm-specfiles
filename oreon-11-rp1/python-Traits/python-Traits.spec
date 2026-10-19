%global source0_hash af4775747e11e05ffe13d3ba463d92f67f1f3d1a9e4f46ba33a44ea22b0c9644
Name:           python-traits
Version:        7.1.0
Release:        1%{?dist}
Summary:        Observable typed attributes for Python classes
License:        ...
URL:            https://github.com/enthought/traits
Source0:        https://files.pythonhosted.org/packages/source/t/traits/traits-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-traits = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-traits
Summary:        Observable typed attributes for Python classes
%description -n python3-traits

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir traits-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-traits usr/lib/python3*/site-packages/traits* usr/lib64/python3*/site-packages/traits* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/traits* usr/lib64/python3*/site-packages/traits* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-traits -f %{oreon_filedir}/python3-traits.list

%changelog

%autochangelog
