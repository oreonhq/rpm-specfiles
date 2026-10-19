%global source0_hash 89b2a440123eeaa400392ce1736e7d60ce9041843027d76819753c5a8246bfdd
Name:		samtools
Version:	1.24
Release:        1%{?dist}
Summary:        Tools for nucleotide sequence alignments in the SAM format
License:	MIT
URL:		http://www.htslib.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  htslib-devel
BuildRequires:  htslib-tools
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl-interpreter
BuildRequires:  zlib-devel
# /oreon:deps
%description
SAM (Sequence Alignment/Map) is a flexible generic format for storing
nucleotide sequence alignment.
SAM Tools provide various utilities for manipulating alignments in the
SAM format, including sorting, merging, indexing and generating
alignments in a per-position format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Remove INSTALL file to suppress rpmlint warning.
rm -f INSTALL

%build

%configure CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" \
  --prefix=%{_prefix} \
  --with-htslib=system
%make_build
%install
%make_install
for file in $(grep -l '^#!/usr/bin/env perl' %{buildroot}%{_bindir}/*); do
  sed -i '1 s|/usr/bin/env perl|/usr/bin/perl|' "${file}"
done
%oreon_autofiles main

%check

ldd samtools | grep -E -e '/lib(64)?/libhts\.so\.' -e '/lib64/lp64d/libhts\.so\.'
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
