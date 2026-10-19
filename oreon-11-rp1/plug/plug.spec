%global source0_hash 932b4e3d70af59570dc493e95f9d52647c53e04dfc09efd9aca894cc9be90cbd
Name: plug
Version: 1.5.0
Release:        1%{?dist}
Summary:        Linux software for Fender Mustang amplifiers
License: GPL-3.0-or-later
Url: https://github.com/offa/plug
Source0:        https://github.com/offa/plug/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gmock-devel
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Linux replacement for Fender FUSE software for Mustang amps.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build
%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
rm -rf %{buildroot}%{_libdir}/cmake/plug
%oreon_autofiles main

%check

make unittest -C %__cmake_builddir
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
