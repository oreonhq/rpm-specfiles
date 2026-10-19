%global source0_hash 45a2702386d594b112d16e957373d18ba77ba3d41d0bdbac2960016b286a17bc
%global _hardened_build 1
Name:           seafile
Version:        9.0.16
Release:        1%{?dist}
Summary:        Cloud storage cli client
License:        GPL-2.0-or-later WITH GPL-3.0-linking-source-exception
URL:            http://seafile.com/
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libargon2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libevent_pthreads)
BuildRequires:  pkgconfig(libsearpc)
BuildRequires:  pkgconfig(libwebsockets)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  sqlite-devel
BuildRequires:  vala
# /oreon:deps
%description
Seafile is a next-generation open source cloud storage system with advanced
support for file syncing, privacy protection and teamwork.

Seafile allows users to create groups with file syncing, wiki, and discussion
to enable easy collaboration around documents within a team.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i -e /\(DESTDIR\)/d lib/libseafile.pc.in

%build

./autogen.sh
%configure --disable-static --with-python3
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n seafile-devel -f %{oreon_filedir}/seafile-devel.list

%changelog

%autochangelog
