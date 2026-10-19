%global source0_hash 901fa43c2b3b7c3326801a21eb89bf0bafbebe8611de0c68d3bb7a77f8c0ccba
%global __cmake_in_source_build 1
Summary:        GUI client for Fwknop
Name: fwknop-gui
Version: 1.3.1
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: https://incomsystems.biz/fwknop-gui/
Source0:        https://incomsystems.biz/%{name}//downloads/%{name}-%{version}.tar.gz
Patch: fwknop-gui-cmake4.patch
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fwknop-devel
BuildRequires:  gcc-c++
BuildRequires:  gpgme-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
Fwknop-gui is a cross platform gui that can save
and send knocks to a server running fwknopd.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%cmake . -DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-config-3.2
%cmake_build
%install
%cmake_install
install -p -m0644 -D %{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/fwknop-gui.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
