%global source0_hash 8e5a56afe9de3c2906b5a9cace2414215ebeeb85f03c0a9592256552b36a600d
%bcond uvicorn 1
Name:           python-socketio
Version:        5.17.0
Release:        1%{?dist}
Summary:        Socket.IO server
License:        MIT
URL:            https://github.com/miguelgrinberg/python-socketio
Source0:        https://github.com/miguelgrinberg/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          0001-Downstream-only-patch-out-test-coverage-analysis.patch
BuildArch:      noarch
%global common_description %{expand:
Socket.IO is a transport protocol that enables real-time bidirectional
event-based communication between clients (typically, though not always, web
browsers) and a server. The official implementations of the client and server
components are written in JavaScript. This package provides Python
implementations of both, each with standard and asyncio variants.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-socketio = %{version}-%{release}
# /oreon:deps
%package -n       python3-socketio+client
Summary:        Metapackage for python3-socketio client extras
Requires:       python3-socketio = %{version}-%{release}
Requires:       python3dist(requests) >= 2.21.0
Requires:       python3dist(websocket-client) >= 0.54.0
Provides:       python3dist(socketio[client]) = %{version}-%{release}

%description -n python3-socketio+client
Metapackage for python3-socketio client extras.

%package -n       python3-socketio+asyncio_client
Summary:        Metapackage for python3-socketio asyncio_client extras
Requires:       python3-socketio = %{version}-%{release}
Requires:       python3dist(aiohttp) >= 3.4
Provides:       python3dist(socketio[asyncio_client]) = %{version}-%{release}

%description -n python3-socketio+asyncio_client
Metapackage for python3-socketio asyncio_client extras.

%package -n       python3-socketio+dev
Summary:        Metapackage for python3-socketio dev extras
Requires:       python3-socketio = %{version}-%{release}
Provides:       python3dist(socketio[dev]) = %{version}-%{release}

%description -n python3-socketio+dev
Metapackage for python3-socketio dev extras.

%package -n       python3-socketio+docs
Summary:        Metapackage for python3-socketio docs extras
Requires:       python3-socketio = %{version}-%{release}
Provides:       python3dist(socketio[docs]) = %{version}-%{release}

%description -n python3-socketio+docs
Metapackage for python3-socketio docs extras.

%description %{common_description}

%package -n     python3-socketio
Summary:        Socket.IO server
Obsoletes:      python-socketio-doc < 5.11.2-4
# oreon:reqs
Requires:       python3dist(bidict) >= 0.21.0
Requires:       python3dist(python-engineio) >= 4.13.2
# /oreon:reqs
%description -n python3-socketio %{common_description}

%prep

%autosetup -p1
%if %{without uvicorn}
sed -r -i 's/^([[:blank:]]*)(uvicorn)\b/\1# \2/' tox.ini
%endif

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-socketio usr/lib/python3*/site-packages/socketio* usr/lib64/python3*/site-packages/socketio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/socketio* usr/lib64/python3*/site-packages/socketio* usr/bin/*

%check

%if %{without uvicorn}
ignore="${ignore-} --ignore=tests/async/test_admin.py"
%endif
%pytest ${ignore-}
%files
%files -n python3-socketio -f %{oreon_filedir}/python3-socketio.list

%changelog

%autochangelog
