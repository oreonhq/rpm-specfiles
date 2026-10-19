%global source0_hash eb0072e7d2b35910689cb4f8702693c54cf1fd6d180337533e2525871b873593
Name:           python-pyvirtualdisplay
Version:        3.0
Release:        7%{?dist}
Summary:        Python wrapper for Xvfb, Xephyr and Xvnc
License:        BSD-2-Clause
URL:            https://github.com/ponty/PyVirtualDisplay
Source0:        https://github.com/ponty/PyVirtualDisplay/archive/%{version}/PyVirtualDisplay-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyvirtualdisplay = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyvirtualdisplay
Summary:        Python wrapper for Xvfb, Xephyr and Xvnc
Requires:       %{py3_dist py}
Requires:       xorg-x11-server-Xvfb
%description -n python3-pyvirtualdisplay

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n PyVirtualDisplay-%{version}
# TODO: package entrypoint2 and vncdotool and enable these tests
rm tests/test_race.py
rm tests/test_xvnc.py
sed -i -E -e '/^(types-pillow|entrypoint2|vncdotool=.*)$/d' requirements-test.txt

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyvirtualdisplay usr/lib/python3*/site-packages/pyvirtualdisplay* usr/lib64/python3*/site-packages/pyvirtualdisplay* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyvirtualdisplay* usr/lib64/python3*/site-packages/pyvirtualdisplay* usr/bin/*

%check

%tox
%files
%files -n python3-pyvirtualdisplay -f %{oreon_filedir}/python3-pyvirtualdisplay.list

%changelog

%autochangelog
