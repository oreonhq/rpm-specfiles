%global source0_hash 58bcb5ad3162964ff5a0c4d2dcbaa0202c2c85d9c470496f3b7a998757776313

Name:           perl-Math-Random-MT-Auto
Version:        6.23
Release:        24%{?dist}
Summary:        Auto-seeded Mersenne Twister PRNGs
License:        BSD-3-Clause
URL:            https://metacpan.org/release/Math-Random-MT-Auto
Source0:        https://cpan.metacpan.org/modules/by-module/Math/Math-Random-MT-Auto-%{version}.tar.gz
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
# Config_m not used
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exception::Class) >= 1.32
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Object::InsideOut) >= 3.88
BuildRequires:  perl(Object::InsideOut::Util)
BuildRequires:  perl(Scalar::Util) >= 1.23
# Win32 not used
# Win32::API not used
BuildRequires:  perl(XSLoader)
# Optional run-time:
BuildRequires:  perl(LWP::UserAgent)
# Tests only:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
# Dependencies
Requires:       perl(Exception::Class) >= 1.32
Requires:       perl(Fcntl)
Requires:       perl(Object::InsideOut) >= 3.88
Requires:       perl(Scalar::Util) >= 1.23
# LWP::UserAgent used for option of acquiring seed data from Internet sources
Recommends:     perl(LWP::UserAgent)
Provides:       bundled(mt19937ar)

%{?perl_default_filter}
# Removed under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Exception::Class|Object::InsideOut|Scalar::Util)\\)

%description
The Mersenne Twister is a fast pseudo-random number generator (PRNG) that is
capable of providing large volumes (> 10^6004) of "high quality"
pseudo-random data to applications that may exhaust available "truly" random
data sources or system-provided PRNGs such as rand.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Random-MT-Auto-%{version}
chmod -x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} -c $RPM_BUILD_ROOT

%check
make test

%files
%doc Changes README examples
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Math*
%{_mandir}/man3/*

%changelog
%autochangelog
