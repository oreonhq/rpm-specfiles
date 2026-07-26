%global source0_hash 1c7641278d2cfa4875742e9d2330f28a9a49dd2c949ecd8e69721a433407f4f8

Name:           qarma
Version:        1.0.0
Release:        3%{?dist}
Summary:        Tool for creating Qt dialog boxes

License:        GPL-2.0-only
URL:            https://github.com/luebking/qarma
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)

%description
Qarma is a tool to create dialog boxes, based on Qt. It's a clone of
Zenity which was written for GTK+.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%qmake_qt6
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
