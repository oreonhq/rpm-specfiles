%global source0_hash 8ae5c4e85299e5c8bddd1b196f2eea38f00709e0dc0cb60454dc9114ae3fff0d

# Provides/Requires filtering is different from rpm 4.9 onwards
%global rpm49 %(rpm --version | perl -p -e 's/^.* (\\d+)\\.(\\d+).*/sprintf("%d.%03d",$1,$2) ge 4.009 ? 1 : 0/e' 2>/dev/null || echo 0)

Name:		perl-Readonly-XS
Version:	1.05
Release:	56%{?dist}
Summary:	Companion module for Readonly
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Readonly-XS
Source0:	https://cpan.metacpan.org/authors/id/R/RO/ROODE/Readonly-XS-%{version}.tar.gz
Patch0:		Readonly-XS-1.05-prereq.patch
Patch1:		Readonly-XS-1.05-interpreter.patch
# Build (perl-devel split from main perl package at F-7)
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test suite
BuildRequires:	perl(Test::More)
# Runtime
Requires:	perl(Carp)
Requires:	perl(Readonly) >= 1.02

# Don't provide the private XS.so() lib
%{?perl_default_filter}

%description
Readonly::XS is a companion module for Readonly, to speed up read-only
scalar variables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Readonly-XS-%{version}

# Build process does not actually need perl(Readonly)
%patch -P 0

# Fix script interpreter for test suite since we're packaging it
%patch -P 1

# And tests don't need to be executable either
chmod -c -x t/test.t

# Avoid doc-file dependencies from tests if we don't have %%perl_default_filter
%if ! %{rpm49}
%global perl_reqfilt /bin/sh -c "%{__perl_requires} | grep -Fvx 'perl(Test::More)'"
%global __perl_requires %{perl_reqfilt}
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc README Changes t/
%{perl_vendorarch}/auto/Readonly/
%{perl_vendorarch}/Readonly/
%{_mandir}/man3/Readonly::XS.3*

%changelog
%autochangelog
