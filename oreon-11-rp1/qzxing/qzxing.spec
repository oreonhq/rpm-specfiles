%global source0_hash 2cb1c8889544e1c2d8ce77ef607db0219bd947322eb550faed636b4853072fa2
%global qtver 5
%global qmake %{expand:%{qmake_qt%{qtver}}}
%global forgeurl    https://github.com/ftylitak/%{name}
Version:        3.3.0
%forgemeta
Name:           qzxing
Release:        1%{?dist}
Summary:        Qt/QML wrapper library for the ZXing library
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-fix-libdir.patch
Patch2:         0002-match-badly-printed-QR-codes.patch
Provides:       bundled(zxing)
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
# /oreon:deps
%description
Qt/QML wrapper library for the ZXing bar-code image processing library.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%qmake PREFIX=%{_prefix} INSTALL_LIBDIR=%{_libdir} src/ -o build/
%make_build -C build
%install
%make_install INSTALL_ROOT=%{buildroot} -C build
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qzxing-devel -f %{oreon_filedir}/qzxing-devel.list

%changelog

%autochangelog
