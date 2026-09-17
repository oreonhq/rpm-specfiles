%global source0_hash 537b85fb3320af05675360a0dacf1748daadb3e1d48730dde9b9f83a01cfd505

%global pypi_name mqtt-randompub

Name:           %{pypi_name}
Version:        0.3.0
Release:        %autorelease
Summary:        Tool for generating MQTT messages on various topics

License:        MIT
URL:            https://github.com/fabaff/mqtt-randompub/
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

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

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mqtt_randompub

%files -f %{pyproject_files}
%license LICENSE
%doc AUTHORS ChangeLog README.rst
%{_bindir}/mqtt-randompub

%changelog
%autochangelog
