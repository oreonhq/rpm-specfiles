%global source0_hash 043d995b6b249d9ebc04c467db31bb7ddc2e55faa08e885bdb050b1f2336b73f

Name:           perl-Signal-Mask
Version:        0.008
Release:        35%{?dist}
Summary:        Signal masks made easy
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Signal-Mask
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Signal-Mask-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IPC::Signal)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Thread::SigMask)
BuildRequires:  perl(warnings)

%description
Signal::Mask is an abstraction around your process or thread signal mask.
It is used to fetch and/or change the signal mask of the calling process or
thread. The signal mask is the set of signals whose delivery is currently
blocked for the caller. It is available as the global hash Signal::Mask.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Signal-Mask-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
