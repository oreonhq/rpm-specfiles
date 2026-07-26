%global source0_hash 4f851490896f3dc65d9e508cada22a9939cc45dbadb1597612a406a61e7624d2

Name:		perl-Mail-Transport
Version:	4.01
Release:	2%{?dist}
Summary:	Email message exchange
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Mail-Transport
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Mail-Transport-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(:VERSION) >= 5.16
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(IO::Handle)
# Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Errno)
BuildRequires:	perl(File::Spec) >= 0.7
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Log::Report) >= 1.42
BuildRequires:	perl(Mail::Reporter) >= 4.00
BuildRequires:	perl(Net::Config)
BuildRequires:	perl(Net::Domain)
BuildRequires:	perl(Net::SMTP)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More)
# Dependencies
Requires:	perl(IO::Socket)
Requires:	perl(List::Util)
Requires:	perl(Log::Report) >= 1.42
Requires:	perl(Mail::Reporter) >= 4.00
Requires:	perl(Net::Config)
Requires:	perl(Net::Domain)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Log::Report\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Mail::Reporter\\)

%description
Email message exchange code, formerly part of the Mail::Box package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mail-Transport-%{version}

%build
yes y | perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc ChangeLog README.md
%{perl_vendorlib}/Mail/
%{_mandir}/man3/Mail::Transport.3*
%{_mandir}/man3/Mail::Transport::Exim.3*
%{_mandir}/man3/Mail::Transport::Mailx.3*
%{_mandir}/man3/Mail::Transport::Qmail.3*
%{_mandir}/man3/Mail::Transport::Receive.3*
%{_mandir}/man3/Mail::Transport::SMTP.3*
%{_mandir}/man3/Mail::Transport::Send.3*
%{_mandir}/man3/Mail::Transport::Sendmail.3*

%changelog
%autochangelog
