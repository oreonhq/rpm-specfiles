%global source0_hash dcc200a073a21cba48122a5dae0b6a875df93d3f8c8ae9d446dcdd9befaa413a

Name:           perl-DateTime-Format-W3CDTF
Version:        0.08
Release:        15%{?dist}
Summary:        Parse and format W3CDTF datetime strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-W3CDTF
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/DateTime-Format-W3CDTF-%{version}.tar.gz
# Simplify Makefile.PL to skip unwanted dependencies
Patch0:         DateTime-Format-W3CDTF-0.08-Disable-author-features.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(lib)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More) >= 0.61

%description
This module understands the W3CDTF date/time format, an ISO 8601 profile,
defined at http://www.w3.org/TR/NOTE-datetime. This format as the native
date format of RSS 1.0.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-W3CDTF-%{version}
%patch -P0 -p1
rm -rf inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
