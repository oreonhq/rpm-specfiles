%global source0_hash eb0072e7d2b35910689cb4f8702693c54cf1fd6d180337533e2525871b873593

Name:           python-pyvirtualdisplay
Version:        3.0
Release:        7%{?dist}
Summary:        Python wrapper for Xvfb, Xephyr and Xvnc

License:        BSD-2-Clause
URL:            https://github.com/ponty/PyVirtualDisplay
Source0:        %{url}/archive/%{version}/PyVirtualDisplay-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# For Tests
BuildRequires:  xmessage
BuildRequires:  xorg-x11-server-Xephyr
BuildRequires:  xorg-x11-server-Xvfb

%global _description %{expand:
pyvirtualdisplay is a python wrapper for Xvfb, Xephyr and Xvnc}

%description %_description

%package -n     python3-pyvirtualdisplay
Summary:        %{summary}

Requires:       %{py3_dist py}
Requires:       xorg-x11-server-Xvfb
%description -n python3-pyvirtualdisplay %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n PyVirtualDisplay-%{version}
# TODO: package entrypoint2 and vncdotool and enable these tests
rm tests/test_race.py
rm tests/test_xvnc.py
sed -i -E -e '/^(types-pillow|entrypoint2|vncdotool=.*)$/d' requirements-test.txt

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pyvirtualdisplay

%check
%tox

%files -n python3-pyvirtualdisplay -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
