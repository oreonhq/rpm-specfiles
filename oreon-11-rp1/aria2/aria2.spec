%global source0_hash 60a420ad7085eb616cb6e2bdf0a7206d68ff3d37fb5a956dc44242eb2f79b66b
%define binname aria2c
Name:           aria2
Version:        1.37.0
Release:        1%{?dist}
Summary:        High speed download utility with resuming and segmented downloading
License:        LicenseRef-Callaway-GPLv2+-with-exceptions
URL:            http://aria2.github.io/
Source0:        https://github.com/aria2/%{name}/releases/download/release-%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  bison
BuildRequires:  c-ares-devel
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gnutls-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  sqlite-devel
# /oreon:deps
%description
aria2 is a download utility with resuming and segmented downloading.
Supported protocols are HTTP/HTTPS/FTP/BitTorrent. It also supports Metalink
version 3.0.

Currently it has following features:
- HTTP/HTTPS GET support
- HTTP Proxy support
- HTTP BASIC authentication support
- HTTP Proxy authentication support
- FTP support(active, passive mode)
- FTP through HTTP proxy(GET command or tunneling)
- Segmented download
- Cookie support
- It can run as a daemon process.
- BitTorrent protocol support with fast extension.
- Selective download in multi-file torrent
- Metalink version 3.0 support(HTTP/FTP/BitTorrent).
- Limiting download/upload speed

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure CXX="g++" \
           --enable-bittorrent \
           --enable-metalink \
           --enable-epoll\
           --disable-rpath \
           --with-gnutls \
           --with-libcares \
           --with-libxml2 \
           --without-openssl \
           --with-libz \
           --with-sqlite3 \
V=1 make %{?_smp_mflags}
%install
%make_install
%find_lang %{name}
rm -f $RPM_BUILD_ROOT%{_datadir}/locale/locale.alias
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
