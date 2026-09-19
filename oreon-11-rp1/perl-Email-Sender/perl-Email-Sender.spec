%global source0_hash dead783d62a968a5104c962e5562172d1e4dfebfa07a323ca62a4f9b455d000d

Name:           perl-Email-Sender
Epoch:          1
Version:        2.601
Release:        6%{?dist}
Summary:        A library for sending email
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Email-Sender
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Sender-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Capture::Tiny) >= 0.08
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Email::Abstract) >= 3.006
BuildRequires:  perl(Email::Address)
BuildRequires:  perl(Email::Simple) >= 1.998
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path) >= 2.06
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.000008
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(Net::SMTP::SSL)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Sub::Override)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Throwable::Error) >= 0.200003
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
Requires:       perl(Email::Abstract) >= 3.006
Requires:       perl(Net::SMTP::SSL)
Requires:       perl(Throwable::Error) >= 0.200003

%{?perl_default_filter}

%description
Email::Sender replaces the old and sometimes problematic Email::Send library,
which did a decent job at handling very simple email sending tasks, but was not
suitable for serious use, for a variety of reasons.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-Sender-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 %{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Email*
%{_mandir}/man3/Email*

%changelog
%autochangelog
