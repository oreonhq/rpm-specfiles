%global source0_hash 3df5cfd2ca1a4c5ca7ff7bab3cc8d53ad2064e134cbf11004f3cf8c4b9055bff
%global         _hardened_build 1
Name:           perl-Text-Fuzzy
Version:        0.29
Release:        19%{?dist}
Summary:        Partial string matching using edit distances
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Fuzzy
Source0:        https://cpan.metacpan.org/authors/id/B/BK/BKB/Text-Fuzzy-%{version}.tar.gz
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Levenshtein::Damerau::XS)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module calculates edit distances between words, and searches arrays
and files to find the nearest entry by edit distance. It handles both byte
strings and character strings (strings containing Unicode), treating each
Unicode character as a single entity.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Fuzzy-%{version}

%build

export CFLAGS="%{optflags} -Wl,-z,relro -Wl,-z,now"
export LDFLAGS="%{?__global_ldflags} -Wl,-z,now -Wl,--as-needed"
perl -pi -e 's|#!.*$|#!/usr/bin/perl|' examples/{*.cgi,*.pl}
rm -f make-pod.pl
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$CFLAGS"
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
chmod a-x -c examples/{*.cgi,*.pl}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
