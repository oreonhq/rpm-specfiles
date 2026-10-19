%global source0_hash a4e08ced44cfea1bce080090c626b8dc4f9d617fa5aafcd84b71405f503e9899
Name:           python-pytest-jupyter
Version:        0.11.0
Release:        1%{?dist}
Summary:        A pytest plugin for testing Jupyter libraries and extensions
License:        BSD-3-Clause AND MIT
URL:            https://jupyter.org
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_jupyter/pytest_jupyter-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.10.0
Requires:       python3-pytest-jupyter = %{version}-%{release}
# /oreon:deps
%package -n       python3-pytest-jupyter+docs
Summary:        Metapackage for python3-pytest-jupyter docs extras
Requires:       python3-pytest-jupyter = %{version}-%{release}
Provides:       python3dist(pytest-jupyter[docs]) = %{version}-%{release}

%description -n python3-pytest-jupyter+docs
Metapackage for python3-pytest-jupyter docs extras.

%package -n       python3-pytest-jupyter+client
Summary:        Metapackage for python3-pytest-jupyter client extras
Requires:       python3-pytest-jupyter = %{version}-%{release}
Requires:       python3dist(jupyter-client) >= 7.4.0
Requires:       python3dist(nbformat) >= 5.3
Requires:       python3dist(ipykernel) >= 6.14
Provides:       python3dist(pytest-jupyter[client]) = %{version}-%{release}

%description -n python3-pytest-jupyter+client
Metapackage for python3-pytest-jupyter client extras.

%package -n       python3-pytest-jupyter+server
Summary:        Metapackage for python3-pytest-jupyter server extras
Requires:       python3-pytest-jupyter = %{version}-%{release}
Requires:       python3dist(jupyter-server) >= 1.21
Requires:       python3dist(jupyter-client) >= 7.4.0
Requires:       python3dist(nbformat) >= 5.3
Requires:       python3dist(ipykernel) >= 6.14
Provides:       python3dist(pytest-jupyter[server]) = %{version}-%{release}

%description -n python3-pytest-jupyter+server
Metapackage for python3-pytest-jupyter server extras.

%package -n       python3-pytest-jupyter+test
Summary:        Metapackage for python3-pytest-jupyter test extras
Requires:       python3-pytest-jupyter = %{version}-%{release}
Provides:       python3dist(pytest-jupyter[test]) = %{version}-%{release}

%description -n python3-pytest-jupyter+test
Metapackage for python3-pytest-jupyter test extras.

%description

%package -n     python3-pytest-jupyter
Summary:        A pytest plugin for testing Jupyter libraries and extensions
# oreon:reqs
Requires:       python3dist(jupyter-core) >= 5.7
Requires:       python3dist(pytest) >= 7.0
# /oreon:reqs
%description -n python3-pytest-jupyter

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pytest_jupyter-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytest-jupyter usr/lib/python3*/site-packages/pytest_jupyter* usr/lib64/python3*/site-packages/pytest_jupyter* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytest_jupyter* usr/lib64/python3*/site-packages/pytest_jupyter* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-pytest-jupyter -f %{oreon_filedir}/python3-pytest-jupyter.list

%changelog

%autochangelog
