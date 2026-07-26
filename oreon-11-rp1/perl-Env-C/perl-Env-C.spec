%global source0_hash ee9971b46e5d39399704d6e334654617326885431b419650e19e7bf0abf34823

Name:           perl-Env-C
Version:        0.15
Release:        27%{?dist}
Summary:        Get/set/unset environment variables on the C level
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Env-C
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHOUT/Env-C-%{version}.tar.gz
# Obey to perl's PERL_USE_SAFE_PUTENV default
Patch1:         Env-C-0.14-Obey-to-perl-s-PERL_USE_SAFE_PUTENV-default.patch
# Disable unreliable t/leak.t instead. ppc64 usually fails.
# <https://github.com/mschout/env-c/issues/3>
Patch2:         Env-C-0.14-Skip-unreliable-t-leat.t-test.patch
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(DynaLoader)
# Tests
BuildRequires:  perl(Test::More)

%description
This module provides a Perl API for getenv(3), setenv(3) and unsetenv(3).
It also can return all the environ variables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Env-C-%{version}
%patch -P1 -p1
%patch -P2 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Env*
%{_mandir}/man3/*

%changelog
%autochangelog
