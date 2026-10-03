%global source0_hash 61877935b1987044ddff4bb90a05200ca7164678a355e170bf5f1a5556cc9f29

%define _lto_cflags %{nil}

Summary:        Collection of Type 1 and 2 font manipulation utilities
Name:           t1utils
Version:        1.42
Release:        12%{?dist}
License:        MIT
URL:            http://www.lcdf.org/~eddietwo/type/
Source0:        http://www.lcdf.org/~eddietwo/type/t1utils-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make

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

%files
%license LICENSE
%doc NEWS.md README.md
%{_bindir}/t1ascii
%{_bindir}/t1asm
%{_bindir}/t1binary
%{_bindir}/t1disasm
%{_bindir}/t1mac
%{_bindir}/t1unmac
%{_mandir}/man1/t1ascii.1*
%{_mandir}/man1/t1asm.1*
%{_mandir}/man1/t1binary.1*
%{_mandir}/man1/t1disasm.1*
%{_mandir}/man1/t1mac.1*
%{_mandir}/man1/t1unmac.1*

%changelog
%autochangelog
