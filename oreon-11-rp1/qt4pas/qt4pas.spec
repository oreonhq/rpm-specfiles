%global source0_hash 825423db80da4df5c21816c0392b3394cddfe2f3293dfd08ace84941726affea

Name:           qt4pas
Version:        2.5
Release:        35%{?dist}
Summary:        Free Pascal Qt4 Binding
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            http://users.telenet.be/Jan.Van.hijfte/qtforfpc/fpcqt4.html
Source0:        http://users.telenet.be/Jan.Van.hijfte/qtforfpc/V%{version}/%{name}-V%{version}_Qt4.5.3.tar.gz

# Remove webview component / webkit dependency
Patch0: 0000-no-webkit.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(QtNetwork)

Requires:       fpc-src

ExclusiveArch:  %{fpc_arches}

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

%autosetup -p1 -n %{name}-V%{version}_Qt4.5.3

%build
%qmake_qt4 Qt4Pas.pro
%make_build

%install
make install INSTALL_ROOT=%{buildroot}

%files
%doc README.TXT
%license COPYING.TXT
%{_libdir}/libQt4Pas.so.*

%files devel
%{_libdir}/libQt4Pas.so

%changelog
%autochangelog
