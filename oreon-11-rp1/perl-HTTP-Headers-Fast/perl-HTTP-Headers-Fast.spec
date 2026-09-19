%global source0_hash cc431db68496dd884db4bc0c0b7112c1f4a4f1dc68c4f5a3caa757a1e7481b48

Name:           perl-HTTP-Headers-Fast
Version:        0.22
Release:        21%{?dist}
Summary:        Faster implementation of HTTP::Headers
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Headers-Fast
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/HTTP-Headers-Fast-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Storable)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(URI)
# Optional tests:
BuildRequires:  perl(HTTP::Headers) >= 5.822
Requires:       perl(HTTP::Date)
Requires:       perl(MIME::Base64)
Requires:       perl(Storable)

%description
HTTP::Headers::Fast is a perl class for parsing/writing HTTP headers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Headers-Fast-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
