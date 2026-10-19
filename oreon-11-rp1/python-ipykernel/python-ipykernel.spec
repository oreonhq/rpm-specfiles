%global source0_hash 9acaaaf97d16355166e4085afe9d225bfbdf2b7ef520f9df3be8f2b248275e09
Name:           python-ipykernel
Version:        7.3.0
Release:        1%{?dist}
Summary:        IPython Kernel for Jupyter
License:        BSD-3-Clause
URL:            https://ipython.org
Source0:        https://files.pythonhosted.org/packages/source/i/ipykernel/ipykernel-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.22
BuildRequires:  python3dist(jupyter-client) >= 6
Requires:       python3-ipykernel = %{version}-%{release}
# /oreon:deps
%package -n       python3-ipykernel+docs
Summary:        Metapackage for python3-ipykernel docs extras
Requires:       python3-ipykernel = %{version}-%{release}
Provides:       python3dist(ipykernel[docs]) = %{version}-%{release}

%description -n python3-ipykernel+docs
Metapackage for python3-ipykernel docs extras.

%package -n       python3-ipykernel+test
Summary:        Metapackage for python3-ipykernel test extras
Requires:       python3-ipykernel = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.0
Requires:       python3dist(pytest) < 10
Requires:       python3dist(pytest-asyncio) >= 0.23.5
Provides:       python3dist(ipykernel[test]) = %{version}-%{release}

%description -n python3-ipykernel+test
Metapackage for python3-ipykernel test extras.

%package -n       python3-ipykernel+cov
Summary:        Metapackage for python3-ipykernel cov extras
Requires:       python3-ipykernel = %{version}-%{release}
Provides:       python3dist(ipykernel[cov]) = %{version}-%{release}

%description -n python3-ipykernel+cov
Metapackage for python3-ipykernel cov extras.

%package -n       python3-ipykernel+pyqt5
Summary:        Metapackage for python3-ipykernel pyqt5 extras
Requires:       python3-ipykernel = %{version}-%{release}
Provides:       python3dist(ipykernel[pyqt5]) = %{version}-%{release}

%description -n python3-ipykernel+pyqt5
Metapackage for python3-ipykernel pyqt5 extras.

%package -n       python3-ipykernel+pyside6
Summary:        Metapackage for python3-ipykernel pyside6 extras
Requires:       python3-ipykernel = %{version}-%{release}
Provides:       python3dist(ipykernel[pyside6]) = %{version}-%{release}

%description -n python3-ipykernel+pyside6
Metapackage for python3-ipykernel pyside6 extras.

%description

%package -n     python3-ipykernel
Summary:        IPython Kernel for Jupyter
# oreon:reqs
Requires:       python3dist(appnope) >= 0.1.2
Requires:       python3dist(comm) >= 0.1.1
Requires:       python3dist(debugpy) >= 1.6.5
Requires:       python3dist(ipython) >= 7.23.1
Requires:       python3dist(jupyter-client) >= 8.9.0
Requires:       python3dist(jupyter-core) >= 5.1
Requires:       python3dist(matplotlib-inline) >= 0.1
Requires:       python3dist(nest-asyncio2) >= 1.7.0
Requires:       python3dist(packaging) >= 22
Requires:       python3dist(psutil) >= 5.7
Requires:       python3dist(pyzmq) >= 25
Requires:       python3dist(tornado) >= 6.4.1
Requires:       python3dist(traitlets) >= 5.4.0
# /oreon:reqs
%description -n python3-ipykernel

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ipykernel-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ipykernel usr/lib/python3*/site-packages/ipykernel* usr/lib64/python3*/site-packages/ipykernel* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ipykernel* usr/lib64/python3*/site-packages/ipykernel* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ipykernel -f %{oreon_filedir}/python3-ipykernel.list

%changelog

%autochangelog
