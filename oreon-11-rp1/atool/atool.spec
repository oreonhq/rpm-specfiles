%global source0_hash 97e14e42566d0d4a4347e7803ff21bf4a3b176f1c9c602709af20c6343509b2b
Name:		atool
Version:	0.39.0
Release:        1%{?dist}
Summary:        A perl script for managing file archives of various types
License:	GPL-2.0-or-later
URL:		http://www.nongnu.org/atool/
Source0:        http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
