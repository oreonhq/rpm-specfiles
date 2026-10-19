%global source0_hash febf9fa1f256914f2300cad07896aa645f9d808dd67994a1fa385fca36408ac2
Name:      sugar-read
Version:   124
Release:        1%{?dist}
Summary:        A document reader for Sugar
License:   GPL-2.0-or-later
URL:       http://wiki.laptop.org/go/Read
Source0:        http://download.sugarlabs.org/sources/sucrose/fructose/Read/Read-%{version}.tar.bz2
BuildArch: noarch
Requires: evince-libs
Requires: evince-djvu
Requires: python3-beautifulsoup4
Requires: sugar-toolkit-gtk3
# oreon:deps
BuildRequires:  evince-devel
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  sugar-toolkit-gtk3-devel
# /oreon:deps
%description
The Read activity allows the laptop to act as a book reader. It has a
simple interface, and will view many kinds of text and image-based book-
like materials. It will have particular strengths in handheld mode, with
extremely low power consumption and simple navigation controls.

Read can read PDF files, single-page TIFF files, and also read DJVU files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Read-%{version}
sed -i 's#usr/bin/env python#usr/bin/env python3#' setup.py

%build

python3 ./setup.py build
%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm -rf $RPM_BUILD_ROOT%{sugaractivitydir}/Read.activity/screenshots/
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Read.activity/
%find_lang org.laptop.sugar.ReadActivity
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
