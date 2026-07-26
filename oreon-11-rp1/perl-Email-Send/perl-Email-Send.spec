%global source0_hash f03649f7856a41d39d53a7e82774929880982c3c7574f41a5cafaca3dc15c896

Name:           perl-Email-Send
Version:        2.202
Release:        4%{?dist}
Summary:        Module for sending email
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Send
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Send-%{version}.tar.gz
BuildRequires:  coreutils, findutils, make
BuildRequires:  perl-generators, perl-interpreter
BuildRequires:  perl(blib), perl(Capture::Tiny), perl(Cwd), perl(Email::Abstract)
BuildRequires:  perl(Email::Address), perl(Email::Simple), perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path), perl(File::Spec), perl(File::Temp), perl(IO::All),
BuildRequires:  perl(IO::Handle), perl(IPC::Open3), perl(lib),
BuildRequires:  perl(Mail::Internet), perl(MIME::Entity), perl(Module::Pluggable)
BuildRequires:  perl(Return::Value), perl(Scalar::Util), perl(strict), perl(Symbol),
BuildRequires:  perl(Test::More), perl(Test::Pod), perl(Test::Pod::Coverage)
BuildRequires:  perl(vars), perl(version), perl(warnings),
BuildRequires:  sed
BuildRequires:  /usr/sbin/sendmail
BuildArch:      noarch
# Not automatically detected, but needed.
# See https://bugzilla.redhat.com/show_bug.cgi?id=1000737
#     https://bugzilla.redhat.com/show_bug.cgi?id=1031298
Requires:	perl(Module::Pluggable)
Requires:	perl(Return::Value)

%description
This module provides a very simple, very clean, very specific interface
to multiple Email mailers. The goal of this software is to be small and
simple, easy to use, and easy to extend.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-Send-%{version}

%build
sed -i '/LICENSE/ d' Makefile.PL
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf $RPM_BUILD_ROOT _docs
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README.md LICENSE
%{perl_vendorlib}/Email/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
