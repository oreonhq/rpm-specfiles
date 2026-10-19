%global source0_hash f66bd0aba3a5b46a2d29b9fac004842b81822c750ee39ca96ea627d8111927ad
%bcond_without test
Name:           py3status
Version:        3.64
Release:        1%{?dist}
Summary:        An extensible i3status wrapper written in python
License:        BSD-3-Clause
URL:            https://github.com/ultrabug/py3status
Source0:        https://github.com/ultrabug/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
%if %{with test}
%endif
Requires:       i3status
Obsoletes:      %{name}-doc < 3.44-1
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.26.1
Requires:       python3-py3status = %{version}-%{release}
# /oreon:deps
%package -n       python3-py3status+dbus
Summary:        Metapackage for python3-py3status dbus extras
Requires:       python3-py3status = %{version}-%{release}
Requires:       python3dist(dbus-python) == 1.3.2
Requires:       python3dist(pygobject) == 3.46.0
Provides:       python3dist(py3status[dbus]) = %{version}-%{release}

%description -n python3-py3status+dbus
Metapackage for python3-py3status dbus extras.

%package -n       python3-py3status+udev
Summary:        Metapackage for python3-py3status udev extras
Requires:       python3-py3status = %{version}-%{release}
Requires:       python3dist(pyudev) >= 0.21.0
Provides:       python3dist(py3status[udev]) = %{version}-%{release}

%description -n python3-py3status+udev
Metapackage for python3-py3status udev extras.

%description
Using py3status, you can take control of your i3bar easily by:
- writing your own modules and have their output displayed on your bar
- handling click events on your i3bar and play with them in no time
- seeing your clock tick every second whatever your i3status interval
No extra configuration file needed, just install & enjoy !

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
# allow upwards dependency matches
sed -i -e 's/dbus-python\s*==\s*/dbus-python >= /' pyproject.toml
sed -i -e 's/PyGObject\s*==\s*/PyGObject >= /' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main
%if %{with test}
%check

%pytest
%endif
%files

%changelog

%autochangelog
