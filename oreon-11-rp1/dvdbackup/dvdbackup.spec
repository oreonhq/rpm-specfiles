%global source0_hash ef8c56fbb82b15b7eef00d2d3118c8253f9770009ed7bb2a5d4849acf88183e6

Name:           dvdbackup
Version:        0.4.2
Release:        30%{?dist}
Summary:        Command line tool for ripping video DVDs
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://dvdbackup.sourceforge.net/
Source0:        http://downloads.sourceforge.net/dvdbackup/%{name}-%{version}.tar.xz
# fix build with libdvdread-6.1
# based on patch by Felix Palmen
# https://bugs.launchpad.net/dvdbackup/+bug/1869226
Patch0:         %{name}-0.4.2-libdvdread-6.1.patch

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libdvdread-devel
BuildRequires: make

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

%files -f %{name}.lang
%exclude %{_datadir}/doc/*
%doc AUTHORS README NEWS
%license COPYING
%{_bindir}/dvdbackup
%{_mandir}/man1/*

%changelog
%autochangelog
