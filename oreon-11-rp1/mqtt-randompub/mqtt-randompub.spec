%global source0_hash b03e1f2d9baba9cbba787741023e9dc7cbf7bc1f4ec9c413d63fe10068b76ee7
%global pypi_name mqtt-randompub
Name:           %{pypi_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        Tool for generating MQTT messages on various topics
License:        MIT
URL:            https://github.com/fabaff/mqtt-randompub/
Source0:        https://github.com/fabaff/%{name}//archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mqtt-randompub = %{version}-%{release}
# /oreon:deps
%package -n       python3-mqtt-randompub+test
Summary:        Metapackage for python3-mqtt-randompub test extras
Requires:       python3-mqtt-randompub = %{version}-%{release}
Requires:       python3dist(pytest) >= 9
Provides:       python3dist(mqtt-randompub[test]) = %{version}-%{release}

%description -n python3-mqtt-randompub+test
Metapackage for python3-mqtt-randompub test extras.

%description
For testing application and tools which are handling MQTT messages
it's often needed to send continuously messages on random topics to
a broker. mqtt-randompub contains options to send a single message,
a specific count of messages, or a constant flow of messages till
the tool is terminated. Configuration files can be used to store
lists of topics to create repeatable test scenarios.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%files

%changelog

%autochangelog
