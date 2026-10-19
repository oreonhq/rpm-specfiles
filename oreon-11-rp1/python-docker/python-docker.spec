%global source0_hash cebb93773d334f778e023a7ee352a8d6e13ab1bd3b863a4d4a59dec897df43ac
Name:           python-docker
Version:        7.2.0
Release:        1%{?dist}
Summary:        A Python library for the Docker Engine API.
License:        Apache-2.0
URL:            https://github.com/docker/docker-py
Source0:        https://files.pythonhosted.org/packages/source/d/docker/docker-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-docker = %{version}-%{release}
# /oreon:deps
%package -n       python3-docker+ssh
Summary:        Metapackage for python3-docker ssh extras
Requires:       python3-docker = %{version}-%{release}
Requires:       python3dist(paramiko) >= 2.4.3
Provides:       python3dist(docker[ssh]) = %{version}-%{release}

%description -n python3-docker+ssh
Metapackage for python3-docker ssh extras.

%package -n       python3-docker+tls
Summary:        Metapackage for python3-docker tls extras
Requires:       python3-docker = %{version}-%{release}
Provides:       python3dist(docker[tls]) = %{version}-%{release}

%description -n python3-docker+tls
Metapackage for python3-docker tls extras.

%package -n       python3-docker+websockets
Summary:        Metapackage for python3-docker websockets extras
Requires:       python3-docker = %{version}-%{release}
Requires:       python3dist(websocket-client) >= 1.3.0
Provides:       python3dist(docker[websockets]) = %{version}-%{release}

%description -n python3-docker+websockets
Metapackage for python3-docker websockets extras.

%package -n       python3-docker+docs
Summary:        Metapackage for python3-docker docs extras
Requires:       python3-docker = %{version}-%{release}
Requires:       python3dist(myst-parser) == 0.18.0
Requires:       python3dist(sphinx) == 5.1.1
Provides:       python3dist(docker[docs]) = %{version}-%{release}

%description -n python3-docker+docs
Metapackage for python3-docker docs extras.

%package -n       python3-docker+dev
Summary:        Metapackage for python3-docker dev extras
Requires:       python3-docker = %{version}-%{release}
Requires:       python3dist(coverage) == 7.2.7
Requires:       python3dist(pytest) == 7.4.2
Requires:       python3dist(pytest-cov) == 4.1.0
Requires:       python3dist(pytest-timeout) == 2.1.0
Requires:       python3dist(ruff) == 0.1.8
Provides:       python3dist(docker[dev]) = %{version}-%{release}

%description -n python3-docker+dev
Metapackage for python3-docker dev extras.

%description

%package -n     python3-docker
Summary:        A Python library for the Docker Engine API.
# oreon:reqs
Requires:       python3dist(pywin32) >= 304
Requires:       python3dist(requests) >= 2.26.0
Requires:       python3dist(urllib3) >= 1.26.0
# /oreon:reqs
%description -n python3-docker

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir docker-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-docker usr/lib/python3*/site-packages/docker* usr/lib64/python3*/site-packages/docker* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/docker* usr/lib64/python3*/site-packages/docker* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-docker -f %{oreon_filedir}/python3-docker.list

%changelog

%autochangelog
