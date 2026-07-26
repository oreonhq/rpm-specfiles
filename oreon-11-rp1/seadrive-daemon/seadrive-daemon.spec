%global source0_hash 5d239f59276a2e09abebeea5866395e07c406cb5996dea2ea0a0fb45ef237c97

%global _hardened_build 1

%global gh_name seadrive-fuse
Name:           seadrive-daemon
Version:        3.0.18
Release:        2%{?dist}
Summary:        Daemon part of Seafile Drive client

License:        GPL-3.0-only
URL:            https://seafile.com
Source0:        https://github.com/haiwen/%{gh_name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make

BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libargon2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libsearpc)
BuildRequires:  pkgconfig(libwebsockets)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)

%description
Seafile is a next-generation open source cloud storage system, with advanced
support for file syncing, privacy protection and teamwork.

Seafile allows users to create groups with file syncing, wiki, and discussion
to enable easy collaboration around documents within a team.

This package contains the daemon part of Seafile Drive client. The Drive
client enables you to access files on the server without syncing to local
disk.

%package -n     python3-seadrive
Summary:        Python API for Seafile Drive client daemon

BuildRequires:  python3-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-seadrive
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gh_name}-%{version}

%build
./autogen.sh
%configure \
    --disable-static \
    --enable-ws \
    --enable-xattr
%make_build

%install
%make_install

%files
%license LICENSE
%{_bindir}/seadrive

%files -n python3-seadrive
%{python3_sitearch}/seadrive/

%changelog
%autochangelog
