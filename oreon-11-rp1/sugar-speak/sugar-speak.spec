%global source0_hash da10ea259b303d861f181b9b746a5d0e4c6170549d894fae80661c3c50464f92
Name:           sugar-speak
Version:        59
Release:        1%{?dist}
Summary:        Speak for Sugar
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            http://wiki.laptop.org/go/Speak
Source0:        https://download.sugarlabs.org/sources/honey/Speak/Speak-%{version}.tar.bz2
BuildArch:      noarch
Requires:       espeak-ng
Requires:       gstreamer-plugins-espeak
Requires:       python3-numpy
Requires:       sugar
Requires:       sugar-toolkit-gtk3
# oreon:deps
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  sugar-toolkit-gtk3
# /oreon:deps
%description
Speak is a talking face for the XO laptop. Anything you type will be spoken
aloud using the XO's speech synthesizer, espeak. You can adjust the accent,
rate and pitch of the voice as well as the shape of the eyes and mouth. This
is a great way to experiment with the speech synthesizer, learn to type or 
just have fun making a funny face for your XO.  

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Speak-%{version}

sed -i 's/python/python3/' bot/*.py

%build

python3 ./setup.py build
%install
python3 ./setup.py install --prefix=%{buildroot}%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
find  %{buildroot}%{sugaractivitydir}Speak.activity/activity.py  -type f -name \* -exec chmod 644 {} \;
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Speak.activity/
%find_lang vu.lux.olpc.Speak
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
