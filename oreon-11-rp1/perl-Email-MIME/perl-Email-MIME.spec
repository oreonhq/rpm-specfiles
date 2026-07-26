%global source0_hash 6dd69b01435b645aecc5354d9854a70cb87641eb446a525e7ab241cefa3cc4d3

Name:           perl-Email-MIME
Version:        1.954
Release:        5%{?dist}
Summary:        Easy MIME message parsing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-MIME
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-MIME-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Email::Address)
BuildRequires:  perl(Email::Address::XS)
BuildRequires:  perl(Email::MessageID)
BuildRequires:  perl(Email::MIME::ContentType) >= 1.023
BuildRequires:  perl(Email::MIME::Encodings) >= 1.314
BuildRequires:  perl(Email::Simple) >= 2.102
BuildRequires:  perl(Email::Simple::Creator)
BuildRequires:  perl(Email::Simple::Header)
BuildRequires:  perl(Encode) >= 1.9801
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Types) >= 1.13
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(utf8)
BuildRequires:  perl(version) > 0.99
# Release Tests
BuildRequires:  perl(Test::Pod) >= 1.41
# Dependencies
Requires:       perl(Email::Simple::Creator)
Requires:       perl(MIME::Types) >= 1.13

Obsoletes:      perl-Email-MIME-Creator < 1.457
Obsoletes:      perl-Email-MIME-Modifier < 1.445
Provides:       perl-Email-MIME-Creator = %{version}
Provides:       perl-Email-MIME-Modifier = %{version}

%description
This is an extension of the Email::Simple module, to handle MIME
encoded messages. It takes a message as a string, splits it up
into its constituent parts, and allows you access to various
parts of the message. Headers are decoded from MIME encoding.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-MIME-%{version}

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
%{_mandir}/man3/Email::MIME.3*
%{_mandir}/man3/Email::MIME::Creator.3*
%{_mandir}/man3/Email::MIME::Encode.3*
%{_mandir}/man3/Email::MIME::Header.3*
%{_mandir}/man3/Email::MIME::Header::AddressList.3*
%{_mandir}/man3/Email::MIME::Modifier.3*

%changelog
%autochangelog
