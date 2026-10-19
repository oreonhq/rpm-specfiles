%global source0_hash 8f8fa7722c82a27130224828629b8c680eb99e15e562d17e02d57c3f097826ea
Name:           perl-Gearman-Client-Async
Version:        0.94
Release:        1%{?dist}
Summary:        Asynchronous Client for the Gearman distributed job system
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Gearman-Client-Async
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRADFITZ/Gearman-Client-Async-%{version}.tar.gz
Patch0:         Gearman-Client-Async-0.94-Do-not-use-removed-Gearman-Objects.patch
BuildArch:      noarch
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Danga::Socket\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Danga::Socket)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Gearman::JobStatus)
BuildRequires:  perl(Gearman::ResponseParser)
BuildRequires:  perl(Gearman::Server)
BuildRequires:  perl(Gearman::Task)
BuildRequires:  perl(Gearman::Util)
BuildRequires:  perl(Gearman::Worker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(fields)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

rm t/err1.t
rm t/err3.t
rm t/err4.t
rm t/err8.t
make test
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
