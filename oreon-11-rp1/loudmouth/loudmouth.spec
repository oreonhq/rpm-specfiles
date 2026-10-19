%global source1_hash 147eba6ea585bdd5bb7e737255b01482b2b7e0e288657e73a6a5ec84973715e5
%global source0_hash 31cbc91c1fddcc5346b3373b8fb45594e9ea9cc7fe36d0595e8912c47ad94d0d
Name:           loudmouth
Version:        1.5.4
Release:        1%{?dist}
Summary:        XMPP/Jabber C programming library
License:        LGPL-2.0-or-later
URL:            https://github.com/mcabber/loudmouth/
Source0:        https://mcabber.com/files/loudmouth/loudmouth-%{version}.tar.bz2
Source1:        https://mcabber.com/files/loudmouth/loudmouth-%{version}.tar.bz2.asc
Source2:        gpgkey-EACADFF156849BC89653139E3C2900DEACB7FC95.gpg
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gpg
BuildRequires:  gtk-doc
BuildRequires:  libasyncns-devel
BuildRequires:  libidn-devel
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
Loudmouth is a lightweight and easy-to-use C library for programming
with the XMPP/Jabber protocol. It's designed to be easy to get started
with and yet extensible to let you do anything the XMPP protocol allows.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       glib2-devel
Requires:       libidn-devel
Requires:       pkgconfig
Requires:       gnutls-devel
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gpgv --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q

%build

%configure --enable-static=no --with-asyncns=yes --with-ssl=openssl \
  --enable-gtk-doc --with-compile-warnings=yes
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n loudmouth-devel -f %{oreon_filedir}/loudmouth-devel.list

%changelog

%autochangelog
