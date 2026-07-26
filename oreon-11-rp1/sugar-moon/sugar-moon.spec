%global source0_hash 4e501d503ae0f1d3f682be4dd75d58a892b4bf01e97748d47fa143a4a12f0421

Version:   19
Release:   20%{?dist}
Name:      sugar-moon
Summary:   Moon phases activity for sugar
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:   Apache-2.0
BuildArch: noarch
URL:       http://wiki.laptop.org/go/Moon
Source0:   http://download.sugarlabs.org/sources/honey/Moon/Moon-%{version}.tar.bz2

BuildRequires: gettext
BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
Requires: sugar 
Requires: sugar-toolkit-gtk3

%description
Moon is a simple Lunar phase activity for Sugar.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Moon-%{version}
sed -i 's/env python/env python3/' setup.py

%build
python3 ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Moon.activity/

%find_lang com.garycmartin.Moon

%files -f com.garycmartin.Moon.lang
%license COPYING
%doc AUTHORS
%{sugaractivitydir}/Moon.activity/

%changelog
%autochangelog
