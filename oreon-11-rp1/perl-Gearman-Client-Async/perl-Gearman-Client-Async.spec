%global source0_hash 8f8fa7722c82a27130224828629b8c680eb99e15e562d17e02d57c3f097826ea

Name:           perl-Gearman-Client-Async
Version:        0.94
Release:        52%{?dist}
Summary:        Asynchronous Client for the Gearman distributed job system
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Gearman-Client-Async
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRADFITZ/Gearman-Client-Async-%{version}.tar.gz
# Adapt to Gearman-1.12.007, CPAN RT#115026
Patch0:         Gearman-Client-Async-0.94-Do-not-use-removed-Gearman-Objects.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Danga::Socket) >= 1.52
BuildRequires:  perl(fields)
BuildRequires:  perl(Gearman::JobStatus)
BuildRequires:  perl(Gearman::ResponseParser)
BuildRequires:  perl(Gearman::Task)
BuildRequires:  perl(Gearman::Util)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Gearman::Server)
BuildRequires:  perl(Gearman::Worker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)

# Filter double Requires:
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Danga::Socket\\)$

%description
Asynchronous Client for the Gearman distributed job system

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gearman-Client-Async-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
mv README.txt README

%check
# t/err1.t blocks (CPAN RT#73048, 82700)
rm t/err1.t
# t/err3.t fails (CPAN RT#87063)
rm t/err3.t
# t/err4.t fais on x86_64 koji
rm t/err4.t
# this test fails to run on x86_64 (#246356)
rm t/err8.t
make test

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%files
%doc CHANGES README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
