%global source0_hash 8017e13e562bc2cb8f8fdeed472fd538e054204c87078d18c3dbf8a91bef0fce

# This package depends on automagic byte compilation

%global debug_package %{nil}

Name:          sugar-pippy
Version:       75
Release:       16%{?dist}
Summary:       Pippy for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://wiki.laptop.org/go/Pippy
Source0:       http://download.sugarlabs.org/sources/sucrose/fructose/Pippy/Pippy-%{version}.tar.bz2

BuildRequires: python3-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gettext 
BuildRequires: sugar-toolkit-gtk3

Requires:      gobject-introspection
Requires:      python3-pybox2d
Requires:      python3-pygame
Requires:      sugar >= 0.116

%description
Teaches Python programming by providing access to Python code samples
and a fully interactive Python interpreter.

The user can type and execute simple Python expressions. For example,
it would be possible for a user to write Python statements to calculate
expressions, play sounds, or make simple text animation. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pippy-%{version}

sed -i 's#!/usr/bin/env python#!/usr/bin/env python3#' setup.py
sed -i 's#!/usr/bin/python#!/usr/bin/python3#' activity.py

# Remove shebang
for Files in pippy_app.py ; do
  sed -i.orig -e 1d ${Files}
  touch -r ${Files}.orig ${Files}
  rm ${Files}.orig
done

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
%find_lang org.laptop.Pippy

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Pippy.activity/

%files -f org.laptop.Pippy.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Pippy.activity/

%changelog
%autochangelog
