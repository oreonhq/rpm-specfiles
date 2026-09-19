%global source0_hash 4a9a41671a9d1504c4da241be419a9503fa3486262526edb81eca9e2ebea0baf

Name:           perl-Email-MIME-Encodings
Version:        1.317
Release:        8%{?dist}
Summary:        Unified interface to MIME encoding and decoding
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-MIME-Encodings
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-MIME-Encodings-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(MIME::Base64) >= 3.05
BuildRequires:  perl(MIME::QuotedPrint) >= 3.05
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96
# Dependencies
Requires:       perl(Carp)

%description
This module simply wraps "MIME::Base64" and "MIME::QuotedPrint" so that
you can throw the contents of a "Content-Transfer-Encoding" header at
some text and have the right thing happen.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-MIME-Encodings-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Email/
%{_mandir}/man3/Email::MIME::Encodings.3*

%changelog
%autochangelog
