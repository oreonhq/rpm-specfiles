%global source0_hash 9812cd0aa3be333768b6069e8b13a761fcd9fe42dc6b8b5a5ea1870dac5b7f55
Name:          perl-Net-IMAP-Simple
Version:       1.2212
Release:        21%{?dist}
Summary:        Simple IMAP account handling
License:       GPL-1.0-or-later OR Artistic-1.0-Perl
URL:           https://metacpan.org/release/Net-IMAP-Simple
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JETTERO/Net-IMAP-Simple-%{version}.tar.gz
BuildArch:     noarch
Requires:      perl(IO::Socket::SSL)
Requires:      perl(Net::SSLeay)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::Command)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make %{?_smp_mflags} test I_PROMISE_TO_TEST_SINGLE_THREADED=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
