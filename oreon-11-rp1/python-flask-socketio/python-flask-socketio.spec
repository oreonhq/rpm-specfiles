%global source0_hash 58e169acba5c32bd8115cc50c27558cfc25c0fa9b3f0382579a06e25ebcbfa11
Name:           python-flask-socketio
Version:        5.6.1
Release:        1%{?dist}
Summary:        Socket.IO integration for Flask applications
License:        MIT
URL:            https://github.com/miguelgrinberg/Flask-SocketIO/
Source0:        https://github.com/miguelgrinberg/Flask-SocketIO//archive/v%{version}/Flask-SocketIO-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
Flask-SocketIO gives Flask applications access to low latency bi-directional
communications between the clients and the server. The client-side application
can use any of the SocketIO official clients libraries in Javascript, C++, Java
and Swift, or any compatible client to establish a permanent connection to the
server.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-flask-socketio = %{version}-%{release}
# /oreon:deps
%package -n       python3-flask-socketio+docs
Summary:        Metapackage for python3-flask-socketio docs extras
Requires:       python3-flask-socketio = %{version}-%{release}
Provides:       python3dist(flask-socketio[docs]) = %{version}-%{release}

%description -n python3-flask-socketio+docs
Metapackage for python3-flask-socketio docs extras.

%package -n       python3-flask-socketio+dev
Summary:        Metapackage for python3-flask-socketio dev extras
Requires:       python3-flask-socketio = %{version}-%{release}
Provides:       python3dist(flask-socketio[dev]) = %{version}-%{release}

%description -n python3-flask-socketio+dev
Metapackage for python3-flask-socketio dev extras.

%description %{common_description}

%package -n     python3-flask-socketio
Summary:        Socket.IO integration for Flask applications
Obsoletes:      python-flask-socketio-doc < 5.6.0-2
# oreon:reqs
Requires:       python3dist(flask) >= 2.1.0
Requires:       python3dist(python-socketio) >= 5.12.0
# /oreon:reqs
%description -n python3-flask-socketio %{common_description}

%prep

%autosetup -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i \
    -e 's/--cov[^[:blank:]]*//g' \
    -e '/^[[:blank:]]*(pytest-cov)[[:blank:]]*$/d' \
    tox.ini

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flask-socketio usr/lib/python3*/site-packages/flask_socketio* usr/lib64/python3*/site-packages/flask_socketio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flask_socketio* usr/lib64/python3*/site-packages/flask_socketio* usr/bin/*

%check

%pytest --ignore-glob='*/test_client.py'
%files
%files -n python3-flask-socketio -f %{oreon_filedir}/python3-flask-socketio.list

%changelog

%autochangelog
