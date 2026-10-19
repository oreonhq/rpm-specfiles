%global source0_hash 1c7641278d2cfa4875742e9d2330f28a9a49dd2c949ecd8e69721a433407f4f8
Name:           qarma
Version:        1.1.1
Release:        1%{?dist}
Summary:        Tool for creating Qt dialog boxes
License:        GPL-2.0-only
URL:            https://github.com/luebking/qarma
Source0:        https://github.com/luebking/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  gcc-c++
# /oreon:deps
%description
Qarma is a tool to create dialog boxes, based on Qt. It's a clone of
Zenity which was written for GTK+.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%qmake_qt6
%make_build
%install
%make_install INSTALL_ROOT="%{buildroot}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
