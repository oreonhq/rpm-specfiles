%global source0_hash 0c3c2418d51021ce280916e63dfe4cba8386b4e2787be5c25433c98f560ddb31
Name:           python-jupyterlab-server
Version:        2.28.1
Release:        1%{?dist}
Summary:        A set of server components for JupyterLab and JupyterLab like applications.
License:        ...
URL:            https://jupyterlab-server.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/j/jupyterlab_server/jupyterlab_server-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.7
Requires:       python3-jupyterlab-server = %{version}-%{release}
# /oreon:deps
%package -n       python3-jupyterlab-server+docs
Summary:        Metapackage for python3-jupyterlab-server docs extras
Requires:       python3-jupyterlab-server = %{version}-%{release}
Requires:       python3dist(sphinxcontrib-openapi) > 0.8
Requires:       python3dist(mistune) < 4
Requires:       python3dist(jinja2) < 3.2.0
Provides:       python3dist(jupyterlab-server[docs]) = %{version}-%{release}

%description -n python3-jupyterlab-server+docs
Metapackage for python3-jupyterlab-server docs extras.

%package -n       python3-jupyterlab-server+openapi
Summary:        Metapackage for python3-jupyterlab-server openapi extras
Requires:       python3-jupyterlab-server = %{version}-%{release}
Requires:       python3dist(openapi-core) >= 0.18.0
Provides:       python3dist(jupyterlab-server[openapi]) = %{version}-%{release}

%description -n python3-jupyterlab-server+openapi
Metapackage for python3-jupyterlab-server openapi extras.

%package -n       python3-jupyterlab-server+test
Summary:        Metapackage for python3-jupyterlab-server test extras
Requires:       python3-jupyterlab-server = %{version}-%{release}
Requires:       python3dist(pytest-jupyter[server]) >= 0.6.2
Requires:       python3dist(openapi-core) >= 0.18.0
Requires:       python3dist(openapi-spec-validator) >= 0.6.0
Requires:       python3dist(openapi-spec-validator) < 0.8.0
Requires:       python3dist(pytest) >= 7.0
Requires:       python3dist(pytest) < 8
Provides:       python3dist(jupyterlab-server[test]) = %{version}-%{release}

%description -n python3-jupyterlab-server+test
Metapackage for python3-jupyterlab-server test extras.

%description

%package -n     python3-jupyterlab-server
Summary:        A set of server components for JupyterLab and JupyterLab like applications.
# oreon:reqs
Requires:       python3dist(babel) >= 2.10
Requires:       python3dist(jinja2) >= 3.0.3
Requires:       python3dist(json5) >= 0.9.0
Requires:       python3dist(jsonschema) >= 4.18.0
Requires:       python3dist(jupyter-server) < 3
Requires:       python3dist(jupyter-server) >= 1.21
Requires:       python3dist(packaging) >= 21.3
Requires:       python3dist(requests) >= 2.31
# /oreon:reqs
%description -n python3-jupyterlab-server

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jupyterlab_server-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jupyterlab-server usr/lib/python3*/site-packages/jupyterlab_server* usr/lib64/python3*/site-packages/jupyterlab_server* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jupyterlab_server* usr/lib64/python3*/site-packages/jupyterlab_server* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jupyterlab-server -f %{oreon_filedir}/python3-jupyterlab-server.list

%changelog

%autochangelog
