%global source0_hash 4e283692e7f066c2418edae9233e3b62400f9355f4d521f99515e52f7b7d72f1
Summary:        Perl interface to the Amazon Elastic Compute Cloud (EC2)
Name: perl-Net-Amazon-EC2
Version: 0.36
Release:        1%{?dist}
License: GPL-1.0-or-later OR Artistic-1.0-Perl
URL: https://metacpan.org/release/Net-Amazon-EC2
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MALLEN/Net-Amazon-EC2-%{version}.tar.gz
BuildArch: noarch
Requires: perl(Moose) >= 0.38
Requires: perl(XML::Simple) >= 2.18
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Moose)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(blib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

set AWS_ACCESS_KEY_ID=
set SECRET_ACCESS_KEY=
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
