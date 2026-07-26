%global source0_hash 33d3a2d525afe1ad7874474feb43436410c7720f2385bfae2f72a70c6151907d

Name:           sugar-clock
Version:        22.1
Release:        15%{?dist}
Summary:        Clock activity for Sugar

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://wiki.laptop.org/go/Clock
Source0:        https://download.sugarlabs.org/sources/honey/Clock/Clock-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3

Requires:       sugar
Requires:       sugar-toolkit-gtk3

%description
This activity displays time in analog, digital, and "natural" forms.
The "natural" form will be an image of a sun or moon arcing across
the sky, rising and setting as the day progresses. This is more than
a simple clock; the user will be able to grab any element and readjust
it, which will update each of the other elements. In this manner,
hopefully the children can explore and understand different methods of
telling time. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Clock-%{version}

sed -i 's/python/python3/' speaker.py clock.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Clock.activity/

%find_lang tv.alterna.Clock

%files -f tv.alterna.Clock.lang
%doc README.md
%{sugaractivitydir}/Clock.activity/

%changelog
%autochangelog
