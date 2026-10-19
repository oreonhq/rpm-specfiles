%global source0_hash 825423db80da4df5c21816c0392b3394cddfe2f3293dfd08ace84941726affea
Name:           qt4pas
Version:        2.5
Release:        1%{?dist}
Summary:        Free Pascal Qt4 Binding
License:        LGPL-3.0-only
URL:            http://users.telenet.be/Jan.Van.hijfte/qtforfpc/fpcqt4.html
Source0:        http://users.telenet.be/Jan.Van.hijfte/qtforfpc/V%{version}/%{name}-V%{version}_Qt4.5.3.tar.gz
Patch0: 0000-no-webkit.patch
Requires:       fpc-src
ExclusiveArch:  %{fpc_arches}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(QtNetwork)
# /oreon:deps
%description
The Free Pascal Qt4 binding allows Free Pascal to interface with the 
C++ Library Qt.

This binding does not cover the whole Qt4 framework but only the 
classes needed by the Cross Platform Lazarus IDE to use Qt as a 
Widget set.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-V%{version}_Qt4.5.3
%oreon_prep
%build

%qmake_qt4 Qt4Pas.pro
%make_build
%install
make install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qt4pas-devel -f %{oreon_filedir}/qt4pas-devel.list

%changelog

%autochangelog
