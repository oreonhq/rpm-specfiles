%global source0_hash 6dd69b01435b645aecc5354d9854a70cb87641eb446a525e7ab241cefa3cc4d3
Name:           perl-Email-MIME
Version:        1.954
Release:        5%{?dist}
Summary:        Easy MIME message parsing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-MIME
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-MIME-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Email::Simple::Creator)
Requires:       perl(MIME::Types) >= 1.13
Obsoletes:      perl-Email-MIME-Creator < 1.457
Obsoletes:      perl-Email-MIME-Modifier < 1.445
Provides:       perl-Email-MIME-Creator = %{version}
Provides:       perl-Email-MIME-Modifier = %{version}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Email::Address)
BuildRequires:  perl(Email::Address::XS)
BuildRequires:  perl(Email::MIME::ContentType)
BuildRequires:  perl(Email::MIME::Encodings)
BuildRequires:  perl(Email::MessageID)
BuildRequires:  perl(Email::Simple)
BuildRequires:  perl(Email::Simple::Creator)
BuildRequires:  perl(Email::Simple::Header)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
