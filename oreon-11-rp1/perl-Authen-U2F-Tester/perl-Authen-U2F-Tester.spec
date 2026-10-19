%global source0_hash d9d39ab18dd41061a246da095ecbfb60115996ddaf7f3afdda68854a987d97c2
Name:           perl-Authen-U2F-Tester
Version:        0.03
Release:        1%{?dist}
Summary:        FIDO/U2F Authentication Test Client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Authen-U2F-Tester
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHOUT/Authen-U2F-Tester-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Authen::U2F)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::Misc)
BuildRequires:  perl(Crypt::OpenSSL::X509)
BuildRequires:  perl(Crypt::PK::ECC)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::AttributeShortcuts)
BuildRequires:  perl(MooseX::SingleArg)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(strictures)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements a FIDO/U2F tester that can be used for testing web
applications that support FIDO/U2F. Think of this module as a "virtual" U2F
security key.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Authen-U2F-Tester-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%make_build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
