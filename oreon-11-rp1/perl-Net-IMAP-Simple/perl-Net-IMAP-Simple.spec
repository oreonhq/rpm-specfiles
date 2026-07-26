%global source0_hash 9812cd0aa3be333768b6069e8b13a761fcd9fe42dc6b8b5a5ea1870dac5b7f55

Name:          perl-Net-IMAP-Simple
Version:       1.2212
Release:       21%{?dist}
Summary:       Simple IMAP account handling
License:       GPL-1.0-or-later OR Artistic-1.0-Perl
URL:           https://metacpan.org/release/Net-IMAP-Simple
Source0:       https://cpan.metacpan.org/authors/id/J/JE/JETTERO/Net-IMAP-Simple-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::Command)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
# Many of the tests do nothing because they need a real IMAP server defined by
# NIS_TEST_HOST environment variable. Because TCP port cannot be redefined,
# it's not possible to run a fake server as a non-root. Therefore many
# dependencies are not exercised by the tests.
BuildRequires: perl(base)
BuildRequires: perl(Carp)
BuildRequires: perl(IO::File)
BuildRequires: perl(IO::Select)
BuildRequires: perl(IO::Socket)
# IO::Socket::SSL not used at tests
BuildRequires: perl(IPC::Open3)
# Net::SSLeay not used at tests
BuildRequires: perl(overload)
BuildRequires: perl(Parse::RecDescent)
BuildRequires: perl(strict)
BuildRequires: perl(Symbol)
BuildRequires: perl(Tie::Handle)
BuildRequires: perl(warnings)
# Optional run-time:
# IO::Socket::INET6 not used at tests
# Tests:
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Socket::INET)
BuildRequires: perl(Test)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)
# Optional tests:
# Test::Perl::Critic not used
# Test::Pod 1.00 not used
# Test::Pod::Coverage 1.00 not used
Requires:      perl(IO::Socket::SSL)
Requires:      perl(Net::SSLeay)

%description
Perl extension for simple IMAP account handling, mostly compatible
with Net::POP3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-IMAP-Simple-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 </dev/null
make %{?_smp_mflags}

%install
make %{?_smp_mflags} pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT

%check
make %{?_smp_mflags} test I_PROMISE_TO_TEST_SINGLE_THREADED=1

%files
%doc README Changes TODO
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/IMAP/
%{perl_vendorlib}/Net/IMAP/Simple.pm
%{perl_vendorlib}/Net/IMAP/Simple.pod
%{perl_vendorlib}/Net/IMAP/Simple/PipeSocket.pm
%{perl_vendorlib}/Net/IMAP/SimpleX.pm
%{perl_vendorlib}/Net/IMAP/SimpleX.pod
%{_mandir}/man3/Net::IMAP::Simple.3*
%{_mandir}/man3/Net::IMAP::Simple::PipeSocket.3*
%{_mandir}/man3/Net::IMAP::SimpleX.3*

%changelog
%autochangelog
