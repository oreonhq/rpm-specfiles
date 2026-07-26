%global source0_hash aaf60095884abb872e25f8e919a8a63d0dabaeca46faeba87d12812d6efc703b

Name:		atool
Version:	0.39.0
Release:	30%{?dist}
Summary:	A perl script for managing file archives of various types

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.nongnu.org/atool/
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	perl-generators
BuildRequires: make

%description
atool is a script for managing file archives of various types.

It includes aunpack (to extract archives), apack (to create archives),
als (to list files), acat (to extract files to the standard output),
etc.

atool relies on external programs to handle the archives.
It determines the archive types using file extensions whenever possible,
with a fallback on 'file'.

It includes support for tarballs, gzip, bzip, bzip2, lzop, lzma, pkzip, rar,
ace, arj, rpm, cpio, arc, 7z, alzip.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Convert to UTF-8 while keeping the original timestamp
iconv -f iso8859-1 -t utf-8 NEWS -o tmp
touch -r NEWS tmp
mv -f tmp NEWS
chmod 0644 NEWS

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/*
%doc NEWS README TODO AUTHORS COPYING
%{_mandir}/man1/*

%changelog
%autochangelog
