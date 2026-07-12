%global source0_hash bbe96fc50f6e1cc6bea1e35e9c04fd4b0ec0501b6cf86bbadabd9e144b0a8bd7

Name:           perl-Mail-Sendmail
Version:        0.83
Release:        1%{?dist}
Summary:        Simple platform independent mailer for Perl

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Sendmail
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Mail-Sendmail-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(parent)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Hostname::Long)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::TCP)
# Not picked up automatically.
Requires:       perl(MIME::QuotedPrint)
Recommends:     perl(Digest::MD5)
Recommends:     perl(MIME::Base64)


Provides:       perl(Mail::Sendmail)
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


%check
%{?!_with_network_tests:rm t/original.t}
make test


%files
%license LICENSE
%doc Changes README Todo
%{perl_vendorlib}/Mail/
%{_mandir}/man3/Mail::Sendmail.3pm*


%changelog
%autochangelog
