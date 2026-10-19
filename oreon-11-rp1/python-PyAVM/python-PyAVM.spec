%global source0_hash bc0f605d957c1fd6d7765523fcba8b9a72377ac6c51461c2a838fe44600bcd9a
Name:           python-pyavm
Version:        0.9.9
Release:        1%{?dist}
Summary:        Simple pure-python AVM meta-data handling
License:        MIT
URL:            http://astrofrog.github.io/pyavm/
Source0:        https://files.pythonhosted.org/packages/source/p/pyavm/pyavm-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyavm = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyavm+test
Summary:        Metapackage for python3-pyavm test extras
Requires:       python3-pyavm = %{version}-%{release}
Provides:       python3dist(pyavm[test]) = %{version}-%{release}

%description -n python3-pyavm+test
Metapackage for python3-pyavm test extras.

%package -n       python3-pyavm+testall
Summary:        Metapackage for python3-pyavm testall extras
Requires:       python3-pyavm = %{version}-%{release}
Provides:       python3dist(pyavm[testall]) = %{version}-%{release}

%description -n python3-pyavm+testall
Metapackage for python3-pyavm testall extras.

%description

%package -n     python3-pyavm
Summary:        Simple pure-python AVM meta-data handling
%description -n python3-pyavm

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyavm-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyavm usr/lib/python3*/site-packages/pyavm* usr/lib64/python3*/site-packages/pyavm* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyavm* usr/lib64/python3*/site-packages/pyavm* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyavm -f %{oreon_filedir}/python3-pyavm.list

%changelog

%autochangelog
