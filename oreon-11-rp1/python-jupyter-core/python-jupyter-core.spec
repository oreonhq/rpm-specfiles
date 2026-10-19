%global source0_hash 4d09aaff303b9566c3ce657f580bd089ff5c91f5f89cf7d8846c3cdf465b5508
Name:           python-jupyter-core
Version:        5.9.1
Release:        1%{?dist}
Summary:        Jupyter core package. A base package on which Jupyter projects rely.
License:        BSD-3-Clause
URL:            https://jupyter.org
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_core/jupyter_core-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.4
Requires:       python3-jupyter-core = %{version}-%{release}
# /oreon:deps
%package -n       python3-jupyter-core+test
Summary:        Metapackage for python3-jupyter-core test extras
Requires:       python3-jupyter-core = %{version}-%{release}
Requires:       python3dist(pytest) < 9
Provides:       python3dist(jupyter-core[test]) = %{version}-%{release}

%description -n python3-jupyter-core+test
Metapackage for python3-jupyter-core test extras.

%package -n       python3-jupyter-core+docs
Summary:        Metapackage for python3-jupyter-core docs extras
Requires:       python3-jupyter-core = %{version}-%{release}
Provides:       python3dist(jupyter-core[docs]) = %{version}-%{release}

%description -n python3-jupyter-core+docs
Metapackage for python3-jupyter-core docs extras.

%description

%package -n     python3-jupyter-core
Summary:        Jupyter core package. A base package on which Jupyter projects rely.
# oreon:reqs
Requires:       python3dist(platformdirs) >= 2.5
Requires:       python3dist(traitlets) >= 5.3
# /oreon:reqs
%description -n python3-jupyter-core

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jupyter_core-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jupyter-core usr/lib/python3*/site-packages/jupyter_core* usr/lib64/python3*/site-packages/jupyter_core* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jupyter_core* usr/lib64/python3*/site-packages/jupyter_core* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jupyter-core -f %{oreon_filedir}/python3-jupyter-core.list

%changelog

%autochangelog
