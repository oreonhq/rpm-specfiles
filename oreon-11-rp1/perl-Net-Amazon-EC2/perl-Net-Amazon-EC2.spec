%global source0_hash 4e283692e7f066c2418edae9233e3b62400f9355f4d521f99515e52f7b7d72f1

Summary: Perl interface to the Amazon Elastic Compute Cloud (EC2)
Name: perl-Net-Amazon-EC2
Version: 0.36
Release: 24%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License: GPL-1.0-or-later OR Artistic-1.0-Perl
URL: https://metacpan.org/release/Net-Amazon-EC2
Source0: https://cpan.metacpan.org/authors/id/M/MA/MALLEN/Net-Amazon-EC2-%{version}.tar.gz

BuildArch: noarch
BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# Run-time:
BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(Encode)
BuildRequires: perl(LWP::Protocol::https)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Moose)
BuildRequires: perl(overload)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(POSIX)
BuildRequires: perl(URI)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(XML::Simple)
# Tests:
BuildRequires: perl(blib)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
Requires: perl(Moose) >= 0.38
Requires: perl(XML::Simple) >= 2.18

%description
This module provides an interface to the Amazon Elastic Compute Cloud (EC2).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Amazon-EC2-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}

%check
# Avoid online tests
set AWS_ACCESS_KEY_ID=
set SECRET_ACCESS_KEY=
make test

%files
%license LICENSE
%doc Changelog
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
