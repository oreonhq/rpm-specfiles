%global source0_hash b9be58e7dbe677f2ac1c472f6e76fad618a65e2f8bf1c7b9d3d97bc169feb740
%bcond_without geoip
Name:           ncdc
Version:        1.25
Release:        1%{?dist}
Summary:        Modern and lightweight direct connect client
License:        MIT
URL:            http://dev.yorhel.nl/ncdc
Source0:        http://dev.yorhel.nl/download/%{name}-%{version}.tar.gz
%if %{with geoip}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(geoip)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Ncdc is a modern and lightweight direct connect client with a 
friendly ncurses interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-silent-rules \
  %{?with_geoip:--with-geoip=yes}
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
