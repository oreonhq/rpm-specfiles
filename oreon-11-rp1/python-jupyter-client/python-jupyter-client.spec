%global source0_hash 9f7116294dca55f1785be880057d44544db9b1567718d92cb33c58886afb9497
Name:           python-jupyter-client
Version:        8.10.0
Release:        1%{?dist}
Summary:        Jupyter protocol implementation and client libraries
License:        ...
URL:            https://jupyter.org
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_client/jupyter_client-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.5
Requires:       python3-jupyter-client = %{version}-%{release}
# /oreon:deps
%package -n       python3-jupyter-client+test
Summary:        Metapackage for python3-jupyter-client test extras
Requires:       python3-jupyter-client = %{version}-%{release}
Requires:       python3dist(ipykernel) >= 6.14
Requires:       python3dist(pytest-jupyter[client]) >= 0.6.2
Provides:       python3dist(jupyter-client[test]) = %{version}-%{release}

%description -n python3-jupyter-client+test
Metapackage for python3-jupyter-client test extras.

%package -n       python3-jupyter-client+docs
Summary:        Metapackage for python3-jupyter-client docs extras
Requires:       python3-jupyter-client = %{version}-%{release}
Requires:       python3dist(sphinx) >= 4
Provides:       python3dist(jupyter-client[docs]) = %{version}-%{release}

%description -n python3-jupyter-client+docs
Metapackage for python3-jupyter-client docs extras.

%package -n       python3-jupyter-client+orjson
Summary:        Metapackage for python3-jupyter-client orjson extras
Requires:       python3-jupyter-client = %{version}-%{release}
Provides:       python3dist(jupyter-client[orjson]) = %{version}-%{release}

%description -n python3-jupyter-client+orjson
Metapackage for python3-jupyter-client orjson extras.

%description

%package -n     python3-jupyter-client
Summary:        Jupyter protocol implementation and client libraries
# oreon:reqs
Requires:       python3dist(jupyter-core) >= 5.1
Requires:       python3dist(python-dateutil) >= 2.8.2
Requires:       python3dist(pyzmq) >= 25.0
Requires:       python3dist(tornado) >= 6.4.1
Requires:       python3dist(traitlets) >= 5.3
Requires:       python3dist(typing-extensions) >= 4.13.0
# /oreon:reqs
%description -n python3-jupyter-client

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jupyter_client-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jupyter-client usr/lib/python3*/site-packages/jupyter_client* usr/lib64/python3*/site-packages/jupyter_client* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jupyter_client* usr/lib64/python3*/site-packages/jupyter_client* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jupyter-client -f %{oreon_filedir}/python3-jupyter-client.list

%changelog

%autochangelog
