%global source0_hash 5f61e23c3de1b52bd70c68d323957ac12b65e4cd05bdf224ad432dc6bb72cc4c
Name:           python-spyder-kernels
Version:        3.1.6
Release:        1%{?dist}
Summary:        Jupyter kernels for Spyder_s console
License:        MIT
URL:            https://github.com/spyder-ide/spyder-kernels
Source0:        https://files.pythonhosted.org/packages/source/s/spyder_kernels/spyder_kernels-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-spyder-kernels = %{version}-%{release}
# /oreon:deps
%package -n       python3-spyder-kernels+test
Summary:        Metapackage for python3-spyder-kernels test extras
Requires:       python3-spyder-kernels = %{version}-%{release}
Provides:       python3dist(spyder-kernels[test]) = %{version}-%{release}

%description -n python3-spyder-kernels+test
Metapackage for python3-spyder-kernels test extras.

%description

%package -n     python3-spyder-kernels
Summary:        Jupyter kernels for Spyder_s console
# oreon:reqs
Requires:       python3dist(ipykernel) < 7
Requires:       python3dist(ipykernel) >= 6.29.3
Requires:       python3dist(ipython) < 10
Requires:       python3dist(ipython) >= 8.15.0
Requires:       python3dist(jupyter-client) < 9
Requires:       python3dist(jupyter-client) >= 7.4.9
Requires:       python3dist(pyxdg) >= 0.26
Requires:       python3dist(pyzmq) >= 24.0.0
Requires:       python3dist(traitlets) >= 5.14.3
Requires:       python3dist(wurlitzer) >= 1.0.3
# /oreon:reqs
%description -n python3-spyder-kernels

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir spyder_kernels-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-spyder-kernels usr/lib/python3*/site-packages/spyder_kernels* usr/lib64/python3*/site-packages/spyder_kernels* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/spyder_kernels* usr/lib64/python3*/site-packages/spyder_kernels* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-spyder-kernels -f %{oreon_filedir}/python3-spyder-kernels.list

%changelog

%autochangelog
