%global source0_hash d4ea1952689ec7e331f9d4ebc9adb15f1d01c2c9dcfabb72e752c9869ab7e97e

Name:           python-gpiozero
Version:        2.0.1
Release:        9%{?dist}
Summary:        Interface to GPIO on Raspberry Pi

License:        BSD-3-Clause
URL:            https://github.com/RPi-Distro/python-gpiozero
Source:         %{pypi_source gpiozero}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
A simple interface to GPIO devices with Raspberry Pi.

%package -n     python3-gpiozero
Summary:        %{summary}
# Several files have `import pkg_resources`
Requires:       python3dist(setuptools)
Recommends:     python3dist(pigpio)

%description -n python3-gpiozero
A simple interface to GPIO devices with Raspberry Pi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gpiozero-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gpiozero gpiozerocli

%check
# running the actual testsuite requires a real Raspberry Pi
%pyproject_check_import -e 'gpiozero.pins.*io'

%files -n python3-gpiozero -f %{pyproject_files}
%doc README.rst
%{_bindir}/pinout
%{_bindir}/pintest

%changelog
%autochangelog
