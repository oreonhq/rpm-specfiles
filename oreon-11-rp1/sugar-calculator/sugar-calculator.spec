%global source0_hash 3ffa4dc00f88e0ddd43d6173fd278f74eeaca03f5098c3e301f41fd7e278fc90

Name:           sugar-calculator
Version:        47
Release:        12%{?dist}
Summary:        Calculator for Sugar

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://wiki.laptop.org/go/Calculate
Source0:        http://download.sugarlabs.org/sources/sucrose/fructose/Calculate/Calculate-%{version}.tar.bz2

BuildRequires:  python3 gettext python3-devel sugar-toolkit-gtk3
Requires:       sugar >= 0.116
BuildArch:      noarch

%description
The calculate activity provides a calculator for the Sugar interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Calculate-%{version}
sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Calculator.activity/

%find_lang org.laptop.Calculate

%files -f org.laptop.Calculate.lang
%doc NEWS
%{sugaractivitydir}/Calculate.activity/

%changelog
%autochangelog
