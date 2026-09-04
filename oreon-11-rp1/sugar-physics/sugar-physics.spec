%global source0_hash 2dca71584a956a452cc85d25eefb569f08f334bc05930f3f0f52636bd48393bf

Name:           sugar-physics
Version:        35
Release:        16%{?dist}
Summary:        A physical world simulator and playground for Sugar

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://wiki.sugarlabs.org/go/Activities/Physics
Source0:        https://download.sugarlabs.org/sources/honey/Physics/Physics-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3
Requires:       sugar
Requires:       python3-pybox2d
BuildArch:      noarch

%description
You can add squares, circles, triangles, or draw your own shapes in
the Physics Activity, and see them come to life with forces (like gravity),
friction, and inertia.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Physics-%{version}

sed -i 's/python/python3/' setup.py
sed -i 's/python/python3/' physics.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# set appropriate permissions
chmod a+x $RPM_BUILD_ROOT%{sugaractivitydir}Physics.activity/physics.py
chmod a-x $RPM_BUILD_ROOT%{sugaractivitydir}Physics.activity/activity/{activity.info,activity-physics.svg}

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Physics.activity/

%find_lang org.laptop.physics

%files -f org.laptop.physics.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Physics.activity/

%changelog
%autochangelog
