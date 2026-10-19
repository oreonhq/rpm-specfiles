%global source0_hash bbe96fc50f6e1cc6bea1e35e9c04fd4b0ec0501b6cf86bbadabd9e144b0a8bd7
Name:           perl-Mail-Sendmail
Version:        0.83
Release:        1%{?dist}
Summary:        Simple platform independent mailer for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Sendmail
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Mail-Sendmail-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(MIME::QuotedPrint)
Recommends:     perl(Digest::MD5)
Recommends:     perl(MIME::Base64)
Provides:       perl(Mail::Sendmail)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Hostname::Long)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Mail::Sendmail is a simple platform independent library for sending
e-mail from your perl script.  It only requires Perl 5 and a network
connection.  Mail::Sendmail contains mainly &sendmail, which takes a
hash with the message to send and sends it. It is intended to be very
easy to setup and use.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Mail-Sendmail-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{?!_with_network_tests:rm t/original.t}
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
