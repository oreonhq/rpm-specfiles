%global source0_hash bb6019fe3576d97e207b9c9ccfd6fd749b057a109ae57b0103b46188dbc28b29

Name:    sugar-terminal
Version: 47
Release: 16%{?dist}
Summary: Terminal for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://wiki.laptop.org/go/Terminal
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Terminal/Terminal-%{version}.tar.bz2

BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext

Requires: sugar
Requires: vte291

BuildArch: noarch

%description
The terminal activity provides a vte-based terminal for the Sugar interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Terminal-%{version}
sed -i 's#/usr/bin/python#/usr/bin/python3#' setup.py

# remove bogus pseudo.po
rm -vf po/pseudo.po

%build
python3 ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Terminal.activity/

%find_lang org.laptop.Terminal

%files -f org.laptop.Terminal.lang
%license COPYING.GPLv3 COPYING
%{sugaractivitydir}/Terminal.activity/

%changelog
%autochangelog
