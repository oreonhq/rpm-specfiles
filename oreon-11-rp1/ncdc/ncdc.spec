%global source0_hash 2a8ab9ad7d43f018fc73ba8babd689dfa44aba8cec53b88e4770185cb97778f7

# support for IP-to-country lookups
%bcond_without geoip

Name:           ncdc
Version:        1.24.1
Release:        3%{?dist}
Summary:        Modern and lightweight direct connect client

License:        MIT
URL:            http://dev.yorhel.nl/ncdc
Source0:        http://dev.yorhel.nl/download/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(zlib)
%if %{with geoip}
BuildRequires:	pkgconfig(geoip)
BuildRequires:	pkgconfig(libmaxminddb)
%endif

%description
Ncdc is a modern and lightweight direct connect client with a 
friendly ncurses interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --disable-silent-rules \
  %{?with_geoip:--with-geoip=yes}
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
