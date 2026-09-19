%global source0_hash f8c5a1e1cbd8f2775bd3d1ce5facc8431f059108bf575a0c8dbda432e5c0bc45

Name:           perl-HTTP-Parser
Version:        0.06
Release:        42%{?dist}
Summary:        Parse HTTP/1.1 request into HTTP::Request/Response object
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Parser
Source0:        https://cpan.metacpan.org/authors/id/E/ED/EDECA/HTTP-Parser-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(strict)
BuildRequires:  perl(URI)
# Tests:
BuildRequires:  perl(Test::More)

%description
This is an HTTP request parser. It takes chunks of text as received and
returns a 'hint' as to what is required, or returns the HTTP::Request when
a complete request has been read. HTTP/1.1 chunked transfer encoding is
supported. It dies if it finds an error.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Parser-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
