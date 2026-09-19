%global source0_hash a3552f6d5fbaef705ca447b0c008a0c19293392d377f7b4208c1c9429d46f69f

%global with_tests 0

Name:          modpoll
Version:       1.6.0
Release:       1%{?dist}
Summary:       A command line tool for Modbus and MQTT
License:       MIT
URL:           https://github.com/gavinying/modpoll
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
# For tests
%if 0%{?with_tests}
BuildRequires: python3-pytest
BuildRequires: python3-prettytable
BuildRequires: python3-pymodbus
%endif

%description
A command line tool for Modbus and MQTT

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if 0%{?with_tests}
%check
%pytest
%endif

%install
%pyproject_install
%pyproject_save_files modpoll

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/modpoll

%changelog
%autochangelog
