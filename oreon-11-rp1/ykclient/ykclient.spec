%global source0_hash f461cdefe7955d58bbd09d0eb7a15b36cb3576b88adbd68008f40ea978ea5016
Name:           ykclient
Version:        2.15
Release:        1%{?dist}
Summary:        Yubikey management library and client
License:        LicenseRef-Callaway-BSD
URL:            http://opensource.yubico.com/yubico-c-client/
Source0:        http://opensource.yubico.com/yubico-c-client/releases/ykclient-%{version}.tar.gz
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  curl-devel
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  make
# /oreon:deps
%description
commandline for yubikeys

%package devel
Summary:  Development headers and libraries for ykclient
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
development files for ykclient  needed to build applications to
take advantage of yubikey authentication.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --enable-static=no
%make_build
%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/libykclient.la
chrpath -d $RPM_BUILD_ROOT%{_bindir}/ykclient
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ykclient-devel -f %{oreon_filedir}/ykclient-devel.list

%changelog

%autochangelog
