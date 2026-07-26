%global source0_hash c9d971d6184769501a55ef3a60f471d1dd7c76c859d92a9c27ca24dc0fecfe9c

%global commit0 4e9be7e91da6d1431e604338c1d3b8aff848541e
%global date 20240130
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary:        Speedy, parallel, and modular, login brute-forcer
Name:           medusa
Version:        2.3
Release:        6.%{date}git%{shortcommit0}%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.foofus.net/jmk/medusa/medusa.html

Source0:        https://github.com/jmk-foofus/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

# https://github.com/jmk-foofus/medusa/pull/72
# https://bugzilla.redhat.com/show_bug.cgi?id=2340838
# Fix build with GCC 15
Patch:          0001-Fix-build-with-GCC-15-by-simplifying-libssh-callback.patch

BuildRequires:  apr-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freerdp2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libpq-devel
BuildRequires:  libssh2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  perl-Carp
BuildRequires:  subversion-devel

%description
Medusa is a speedy, massively parallel, modular, login brute-forcer for network
services. Some of the key features of Medusa are:

* Thread-based parallel testing. Brute-force testing can be performed against
  multiple hosts, users or passwords concurrently.
* Flexible user input. Target information (host/user/password) can be specified
  in a variety of ways.  For example, each item can be either a single entry or
  a file containing multiple entries.  Additionally, a combination file format
  allows the user to refine their target listing.
* Modular design. Each service module exists as an independent .mod file. This
  means that no modifications are necessary to the core application in order to
  extend the supported list of services for brute-forcing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit0}

%build
autoreconf -vif
%configure \
    --enable-module-afp=no \
    --with-default-mod-path=%{_libdir}/medusa/modules
%make_build

%install
%make_install
 
%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_libdir}/%{name}

%changelog
%autochangelog
