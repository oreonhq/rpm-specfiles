%global source0_hash 582353422e0a26fabf188f1bbdcf91603158af19d65fff7a6c761a28eaabcfd5
Name:           udisks2-qt5
Version:        5.0.6
Release:        1%{?dist}
Summary:        Qt5 binding for udisks2
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/udisks2-qt5
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
# /oreon:deps
%description
This package provides a Qt5 binding for udisks2.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?isa}
%description devel
Header files and libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's|/lib|/%{_lib}|' udisks2.pro

%build

export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n udisks2-qt5-devel -f %{oreon_filedir}/udisks2-qt5-devel.list

%changelog

%autochangelog
