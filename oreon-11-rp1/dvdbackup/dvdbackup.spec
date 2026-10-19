%global source0_hash ef8c56fbb82b15b7eef00d2d3118c8253f9770009ed7bb2a5d4849acf88183e6
Name:           dvdbackup
Version:        0.4.2
Release:        1%{?dist}
Summary:        Command line tool for ripping video DVDs
License:        GPL-3.0-or-later
URL:            http://dvdbackup.sourceforge.net/
Source0:        http://downloads.sourceforge.net/dvdbackup/%{name}-%{version}.tar.xz
Patch0:         %{name}-0.4.2-libdvdread-6.1.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libdvdread-devel
BuildRequires:  make
# /oreon:deps
%description
dvdbackup is a tool to rip video DVDs from the command line. It has
the advantages of being small, fast, and easy to use.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .orig

%build

%configure
make %{?_smp_mflags}
%install
%make_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
