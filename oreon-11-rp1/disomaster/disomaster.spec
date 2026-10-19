%global source0_hash 9f8de28dbb8a3f624fde060ba3b8d73744a0c63eecfb1f9cc6253685e278bd8d
Name:           disomaster
Version:        5.0.8
Release:        1%{?dist}
Summary:        Library to manipulate DISC burning
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/disomaster
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(libisoburn-1)
# /oreon:deps
%description
DISOMaster provides basic optical drive operation and on-disc filesystem
manipulation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's|/lib|/%{_lib}|' libdisomaster/libdisomaster.pro

%build

%qmake_qt5 PREFIX=%{_prefix}
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n disomaster-devel -f %{oreon_filedir}/disomaster-devel.list

%changelog

%autochangelog
