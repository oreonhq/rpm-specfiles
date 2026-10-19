%global source0_hash 4fa95cadc09110af9aa5454cb28dbf5cb59874026a6428a84bedc6f2755604ec
%global repo qtmpris
Name:           libmpris-qt5
Summary:        Qt and QML MPRIS interface and adaptor
Version:        1.0.6
Release:        1%{?dist}
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://git.merproject.org/mer-core/%{repo}
Source0:        https://git.merproject.org/mer-core/%{repo}/-/archive/%{version}/%{repo}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(dbusextended-qt5)
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files and libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{repo}-%{version}

%build

%qmake_qt5
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmpris-qt5-devel -f %{oreon_filedir}/libmpris-qt5-devel.list

%changelog

%autochangelog
