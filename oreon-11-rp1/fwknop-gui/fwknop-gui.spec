%global source0_hash 901fa43c2b3b7c3326801a21eb89bf0bafbebe8611de0c68d3bb7a77f8c0ccba

%global __cmake_in_source_build 1

Summary: GUI client for Fwknop
Name: fwknop-gui
Version: 1.3.1
Release: 28%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://incomsystems.biz/fwknop-gui/
Source: %{url}/downloads/%{name}-%{version}.tar.gz
Patch: fwknop-gui-cmake4.patch

BuildRequires: gcc-c++ cmake
BuildRequires: fwknop-devel
BuildRequires: wxGTK-devel
BuildRequires: libcurl-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gpgme-devel
BuildRequires: pkgconfig(libqrencode)
BuildRequires: asciidoc

%description
Fwknop-gui is a cross platform gui that can save
and send knocks to a server running fwknopd.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name} -p1

%build
%cmake . -DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-config-3.2
%cmake_build

%install
%cmake_install
install -p -m0644 -D %{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/fwknop-gui.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%license LICENSE
%dir %{_datadir}/%{name}
%doc %{_datadir}/%{name}/help.html
%doc %{_mandir}/man8/%{name}.8*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
%autochangelog
