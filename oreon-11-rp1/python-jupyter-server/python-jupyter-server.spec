%global source0_hash a8960aa29263f6041283e97d4756b099fb49b767baab6371891ecb1bd40a63df
Name:           python-jupyter-server
Version:        2.21.1
Release:        1%{?dist}
Summary:        The backend—i.e. core services, APIs, and REST endpoints—to Jupyter web applications.
License:        ...
URL:            https://jupyter-server.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/j/jupyter_server/jupyter_server-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-jupyter-server = %{version}-%{release}
# /oreon:deps
%package -n       python3-jupyter-server+test
Summary:        Metapackage for python3-jupyter-server test extras
Requires:       python3-jupyter-server = %{version}-%{release}
Provides:       python3dist(jupyter-server[test]) = %{version}-%{release}

%description -n python3-jupyter-server+test
Metapackage for python3-jupyter-server test extras.

%description

%package -n     python3-jupyter-server
Summary:        The backend—i.e. core services, APIs, and REST endpoints—to Jupyter web applications.
%description -n python3-jupyter-server

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jupyter_server-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jupyter-server usr/lib/python3*/site-packages/jupyter_server* usr/lib64/python3*/site-packages/jupyter_server* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jupyter_server* usr/lib64/python3*/site-packages/jupyter_server* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jupyter-server -f %{oreon_filedir}/python3-jupyter-server.list

%changelog

%autochangelog
