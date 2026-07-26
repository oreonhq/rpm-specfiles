%global source0_hash 513934b208e8513883137ae319ab29c5e706cbac3691242dbddbba85b7916487

Name:           perl-Log-Any-Adapter-Screen
Version:        0.141
Release:        5%{?dist}
Summary:        Send logs to screen, with colors and some other features

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://search.cpan.org/dist/Log-Any-Adapter-Screen/
Source0:        https://www.cpan.org/modules/by-module/Log/Log-Any-Adapter-Screen-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.010
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Adapter) >= 0.11
BuildRequires:  perl(Log::Any::Adapter::Base)
BuildRequires:  perl(Log::Any::Adapter::Util)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod) >=  1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
This Log::Any adapter prints log messages to screen (STDERR/STDOUT).  The
messages are colored according to level (unless coloring is turned off).
It has a few other features: allow passing formatter, allow setting level
from some environment variables, add prefix/timestamps.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Log-Any-Adapter-Screen-%{version} -p 1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
%make_build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
