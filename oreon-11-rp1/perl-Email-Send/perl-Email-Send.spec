%global source0_hash f03649f7856a41d39d53a7e82774929880982c3c7574f41a5cafaca3dc15c896
Name:           perl-Email-Send
Version:        2.202
Release:        1%{?dist}
Summary:        Module for sending email
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Send
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Send-%{version}.tar.gz
BuildArch:      noarch
Requires:	perl(Module::Pluggable)
Requires:	perl(Return::Value)
# oreon:deps
BuildRequires:  /usr/sbin/sendmail
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Email::Abstract)
BuildRequires:  perl(Email::Address)
BuildRequires:  perl(Email::Simple)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(Mail::Internet)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Return::Value)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
