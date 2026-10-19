%global source0_hash e9342979e32a1997b14e3bb3cd980619e8320c495873342d3b5eb30eb6f16b6a
%global repo qtdbusextended
Name:           libdbusextended-qt5
Summary:        Extended DBus for Qt
Version:        0.0.3
Release:        18%{?dist}
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/nemomobile/qtdbusextended
Source0:        https://github.com/nemomobile/%{repo}/archive/%{version}/%{repo}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
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
%files -n libdbusextended-qt5-devel -f %{oreon_filedir}/libdbusextended-qt5-devel.list

%changelog

%autochangelog
