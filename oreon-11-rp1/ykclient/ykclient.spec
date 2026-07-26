%global source0_hash f461cdefe7955d58bbd09d0eb7a15b36cb3576b88adbd68008f40ea978ea5016

Name:           ykclient
Version:        2.15
Release:        23%{?dist}
Summary:        Yubikey management library and client

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://opensource.yubico.com/yubico-c-client/
Source0:	http://opensource.yubico.com/yubico-c-client/releases/ykclient-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  curl-devel, chrpath, help2man

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

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/ykclient
%{_libdir}/libykclient.so.3*
%{_mandir}/man1/ykclient.1.gz

%files devel
%{_includedir}/*.h
%{_libdir}/libykclient.so

%changelog
%autochangelog
