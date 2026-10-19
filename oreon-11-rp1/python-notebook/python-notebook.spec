%global source0_hash cc02b5f0bb972160cccfe44ad8a1a202036206ba3439469c514f03aefa9ae807
Name:           python-notebook
Version:        7.6.2
Release:        1%{?dist}
Summary:        Jupyter Notebook - A web-based notebook environment for interactive computing
License:        ...
URL:            https://github.com/jupyter/notebook
Source0:        https://files.pythonhosted.org/packages/source/n/notebook/notebook-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-jupyter-builder) >= 0.5
BuildRequires:  python3dist(hatchling) >= 1.11
BuildRequires:  python3dist(jupyter-builder) < 2
BuildRequires:  python3dist(jupyter-builder) >= 1.0.2
Requires:       python3-notebook = %{version}-%{release}
# /oreon:deps
%package -n       python3-notebook+test
Summary:        Metapackage for python3-notebook test extras
Requires:       python3-notebook = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.0
Requires:       python3dist(jupyter-server[test]) >= 2.19.0
Requires:       python3dist(jupyter-server[test]) < 3
Requires:       python3dist(jupyterlab-server[test]) >= 2.28.0
Requires:       python3dist(jupyterlab-server[test]) < 3
Provides:       python3dist(notebook[test]) = %{version}-%{release}

%description -n python3-notebook+test
Metapackage for python3-notebook test extras.

%package -n       python3-notebook+docs
Summary:        Metapackage for python3-notebook docs extras
Requires:       python3-notebook = %{version}-%{release}
Requires:       python3dist(sphinx) >= 1.3.6
Provides:       python3dist(notebook[docs]) = %{version}-%{release}

%description -n python3-notebook+docs
Metapackage for python3-notebook docs extras.

%package -n       python3-notebook+dev
Summary:        Metapackage for python3-notebook dev extras
Requires:       python3-notebook = %{version}-%{release}
Provides:       python3dist(notebook[dev]) = %{version}-%{release}

%description -n python3-notebook+dev
Metapackage for python3-notebook dev extras.

%description

%package -n     python3-notebook
Summary:        Jupyter Notebook - A web-based notebook environment for interactive computing
# oreon:reqs
Requires:       python3dist(jupyter-builder) < 2
Requires:       python3dist(jupyter-builder) >= 1.0.2
Requires:       python3dist(jupyter-server) < 3
Requires:       python3dist(jupyter-server) >= 2.19.0
Requires:       python3dist(jupyterlab) < 4.7
Requires:       python3dist(jupyterlab) >= 4.6.3
Requires:       python3dist(jupyterlab-server) < 3
Requires:       python3dist(jupyterlab-server) >= 2.28.0
Requires:       python3dist(notebook-shim) < 0.3
Requires:       python3dist(notebook-shim) >= 0.2
Requires:       python3dist(tornado) >= 6.2.0
# /oreon:reqs
%description -n python3-notebook

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir notebook-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-notebook usr/lib/python3*/site-packages/notebook* usr/lib64/python3*/site-packages/notebook* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/notebook* usr/lib64/python3*/site-packages/notebook* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-notebook -f %{oreon_filedir}/python3-notebook.list

%changelog

%autochangelog
