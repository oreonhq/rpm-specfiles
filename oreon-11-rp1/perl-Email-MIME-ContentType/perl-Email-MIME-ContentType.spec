%global source0_hash e7950246433f7ed6c3e4fd4df2227e0f2341137c3cab1989018fc370f58145c4

Name:           perl-Email-MIME-ContentType
Version:        1.028
Release:        9%{?dist}
Summary:        Parse a MIME Content-Type Header
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-MIME-ContentType
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-MIME-ContentType-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 2.87
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Text::Unidecode)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96
# Extra Tests
BuildRequires:  perl(Test::Pod) >= 1.41
# Dependencies

%description
This module is responsible for parsing email content type headers according
to section 5.1 of RFC 2045. It returns a hash with entries for the type, the
subtype, and a hash of attributes.

For backward compatibility with a really unfortunate misunderstanding of RFC
2045 by the early implementors of this module, 'discrete' and 'composite' are
also present in the returned hashref, with the values of 'type' and 'subtype'
respectively.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-MIME-ContentType-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Email/
%{_mandir}/man3/Email::MIME::ContentType.3*

%changelog
%autochangelog
