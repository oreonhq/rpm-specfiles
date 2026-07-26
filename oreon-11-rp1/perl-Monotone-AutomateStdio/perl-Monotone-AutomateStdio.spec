%global source0_hash 237d95dc2714d7df07086f31a0492059a83b9b79032d477584f620d8b165f2a3

Name:           perl-Monotone-AutomateStdio
Version:        1.10
Release:        30%{?dist}
Summary:        Perl interface to Monotone via automate stdio
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/Monotone-AutomateStdio
Source0:        https://cpan.metacpan.org/authors/id/A/AE/AECOOPER/monotone/Monotone-AutomateStdio-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Poll)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(locale)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
The Monotone::AutomateStdio class gives a Perl developer access to
Monotone's automate stdio facility via an easy to use interface. All
command, option and output formats are handled internally by this
class. Any structured information returned by Monotone is parsed and
returned back to the caller as lists of records for ease of access
(detailed below). One also has the option of accessing Monotone's
output as one large string should you prefer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Monotone-AutomateStdio-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README
%license COPYING
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
