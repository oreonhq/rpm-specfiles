%global source0_hash 58bcb5ad3162964ff5a0c4d2dcbaa0202c2c85d9c470496f3b7a998757776313
Name:           perl-Math-Random-MT-Auto
Version:        6.23
Release:        24%{?dist}
Summary:        Auto-seeded Mersenne Twister PRNGs
License:        BSD-3-Clause
URL:            https://metacpan.org/release/Math-Random-MT-Auto
Source0:        https://cpan.metacpan.org/modules/by-module/Math/Math-Random-MT-Auto-%{version}.tar.gz
Requires:       perl(Exception::Class) >= 1.32
Requires:       perl(Fcntl)
Requires:       perl(Object::InsideOut) >= 3.88
Requires:       perl(Scalar::Util) >= 1.23
Recommends:     perl(LWP::UserAgent)
Provides:       bundled(mt19937ar)
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Exception::Class|Object::InsideOut|Scalar::Util)\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Object::InsideOut)
BuildRequires:  perl(Object::InsideOut::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
