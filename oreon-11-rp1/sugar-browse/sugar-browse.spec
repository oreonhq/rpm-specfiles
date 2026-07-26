%global source0_hash bb3564949024611e2bc15c16ab945637195b2687cb2c6919ff35d21e7a9cb161

Name:    sugar-browse
Version: 208
Release: 4%{?dist}
Summary: Browse activity for Sugar
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://wiki.laptop.org/go/Browse
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Browse/Browse-%{version}.tar.bz2

BuildRequires: gobject-introspection-devel
BuildRequires: python3-devel
BuildRequires: sugar-toolkit-gtk3
BuildRequires: webkitgtk4-devel
BuildRequires: gettext
Requires: sugar-toolkit-gtk3
Requires: webkit2gtk4.1

BuildArch: noarch

%description
A browser for the Sugar platform based on the WebKit web browser
engine. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Browse-%{version}

%build
python3 ./setup.py build

%install
mkdir -p %{buildroot}/%{sugaractivitydir}
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{sugaractivitydir}/Browse.activity/

%find_lang org.laptop.WebActivity

%files -f org.laptop.WebActivity.lang
%license COPYING
%doc AUTHORS
%{sugaractivitydir}/Browse.activity/
/usr/share/metainfo/org.laptop.WebActivity.appdata.xml

%changelog
%autochangelog
