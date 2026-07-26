%global source0_hash 3602ce9d1ada58b063f2052ff013ff8cdd06d66cef918d5f6d048b6f68ccf049

%global srcname paho-mqtt

Name:           python-%{srcname}
Version:        2.1.0
Release:        8%{?dist}
Summary:        Python MQTT version 3.1/3.1.1/5.0 client class

License:        EPL-1.0
URL:            http://eclipse.org/paho/
Source0:        https://github.com/eclipse/paho.mqtt.python/archive/v%{version}/%{srcname}-%{version}.tar.gz
Buildarch:      noarch

%description
This library provides a client class which enable applications to connect to
an MQTT broker to publish messages, and to subscribe to topics and receive
published messages. It also provides some helper functions to make publishing
one off messages to an MQTT server very straightforward.

The MQTT protocol is a machine-to-machine (M2M) connectivity protocol. Designed
as an extremely lightweight publish/subscribe messaging transport, it is useful
for connections with remote locations where a small code footprint is required
and/or network bandwidth is at a premium.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This library provides a client class which enable applications to connect to
an MQTT broker to publish messages, and to subscribe to topics and receive
published messages. It also provides some helper functions to make publishing
one off messages to an MQTT server very straightforward.

The MQTT protocol is a machine-to-machine (M2M) connectivity protocol. Designed
as an extremely lightweight publish/subscribe messaging transport, it is useful
for connections with remote locations where a small code footprint is required
and/or network bandwidth is at a premium.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n paho.mqtt.python-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files paho

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc CONTRIBUTING.md README.rst *.html

%changelog
%autochangelog
