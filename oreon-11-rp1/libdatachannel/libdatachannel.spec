%global source0_hash 454537c3cd526bed935d847bb2dff4046f266eef84d43b2a5f2f2f293c0026f4
%define soversion() %(echo "%1" | awk -F. '{print $1"."$2}')
Name:           libdatachannel
Version:        0.24.5
Release:        1%{?dist}
Summary:        WebRTC network library featuring Data Channels, Media Transport, and WebSockets
License:        MPL-2.0
URL:            https://libdatachannel.org/
Source0:        https://github.com/paullouisageneau/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(plog)
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  libsrtp-devel
BuildRequires:  make
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(nice)
BuildRequires:  usrsctp-devel
# /oreon:deps
%description
libdatachannel is a standalone implementation of WebRTC Data Channels,
WebRTC Media Transport, and WebSockets in C++17 with C bindings for POSIX platforms
(including GNU/Linux, Android, FreeBSD, Apple macOS and iOS) and Microsoft Windows.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_prep
%build

%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DPREFER_SYSTEM_LIB=ON -DUSE_GNUTLS=ON -DUSE_NICE=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libdatachannel-devel -f %{oreon_filedir}/libdatachannel-devel.list

%changelog

%autochangelog
