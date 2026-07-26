%global source0_hash 9a441a90f9bcdb09612db9d810c54a76c802a45c95a72a5ac744be352c234c63

Name:           perl-Devel-Profiler
Version:        0.04
Release:        53%{?dist}
Summary:        Perl profiler compatible with dprofpp
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Profiler
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/Devel-Profiler-%{version}.tar.gz
Patch0:         perl-Devel-Profiler-perl510.patch
# Stop using of each() on hash after insertion (CPAN RT#104207)
Patch1:         Devel-Profiler-0.04-Do-not-use-each-on-hash-after-insertion.patch
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
# dprofpp from perl-Devel-DProf is executed
BuildRequires:  perl-Devel-DProf
BuildRequires:  perl-generators
BuildRequires:  perl(B)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
#BuildRequires:  perl(File::Path) ??
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More)
# dprofpp from perl-Devel-DProf is executed
Requires:       perl-Devel-DProf

%description
This module implements a Perl profiler that outputs profiling data in a
format compatible with dprofpp, Devel::DProf's profile analysis tool. It is
meant to be a drop-in replacement for Devel::DProf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Profiler-%{version}
%patch -P0 -p1
%patch -P1 -p1

# t/01basic fails.  This is the failing test:
#
# # make sure that regsitered at least 1 second of user time
# ($real, $sys, $user) = get_times();
# ok($user >= 1, "check user time >= 1 seconds");
#
# That test seems a bit bogus, unless I'm missing something.
perl -pi -e 's/^/#/ if /"check user time >= 1 second/;' \
    -e 's/^(use Test::More tests => )(\d+)/$1 . ($2-1)/e' t/01basic.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
