%global source0_hash 61877935b1987044ddff4bb90a05200ca7164678a355e170bf5f1a5556cc9f29
%define _lto_cflags %{nil}
Summary:        Collection of Type 1 and 2 font manipulation utilities
Name:           t1utils
Version:        1.42
Release:        1%{?dist}
License:        MIT
URL:            http://www.lcdf.org/~eddietwo/type/
Source0:        http://www.lcdf.org/~eddietwo/type/t1utils-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
t1utils is a collection of programs for manipulating PostScript type 1
and type 2 fonts containing programs to convert between PFA (ASCII)
format, PFB (binary) format, a human-readable and editable ASCII format,
and Macintosh resource forks.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
