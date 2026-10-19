%global source0_hash 033123b25f42cb084f6fd0a959ddf53100d3202c67e666e5cc57a4e48ec1253c
Name:           impressive
Version:        0.13.2
Release:        1%{?dist}
Summary:        A program that displays presentation slides
License:        GPL-2.0-or-later
URL:            http://impressive.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/Impressive-%{version}.tar.gz
Source1:        %{name}.sh
Patch:          impressive-0.13-escape-escape-sequence.patch
BuildArch:      noarch
Requires:       python3-imaging
Requires:       python3-pygame
Requires:       opengl-games-utils
Requires:       mupdf
Requires:       xdg-utils
Requires:       dejavu-sans-fonts
# oreon:deps
BuildRequires:  python3-devel
# /oreon:deps
%description
Impressive is a program that displays presentation slides. But unlike 
OpenOffice.org Impress or other similar applications, it does so with 
style. 

Smooth alpha-blended slide transitions are provided for the sake 
of eye candy, but in addition to this, Impressive offers some unique tools 
that are really useful for presentations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Impressive-%{version} -p1
sed -i -e '1s#/usr/bin/env python#/usr/bin/python3#' impressive.py

%build

sed -e "s|@PYTHON_SITELIB@|%{python3_sitelib}|" %{SOURCE1} > impressive.sh
%install
rm -rf %{buildroot}
install -D -p -m 755 impressive.py %{buildroot}%{python3_sitelib}/impressive.py
install -D -p -m 644 impressive.1 %{buildroot}%{_mandir}/man1/impressive.1
install -D -p -m 755 impressive.sh %{buildroot}%{_bindir}/impressive
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
