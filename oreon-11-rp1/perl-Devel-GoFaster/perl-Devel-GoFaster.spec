%global source0_hash a0a10e72e1818a99e4d2321fb2fa16271b503d5b0e18a6707b1e14d5dfcd290f

Name:           perl-Devel-GoFaster
Version:        0.001
Release:        30%{?dist}
Summary:        Optimise executable Perl ops
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-GoFaster
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Devel-GoFaster-%{version}.tar.gz
# Build
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
# XXX: BuildRequires:  perl(Carp)
BuildRequires:  perl(Lexical::SealRequireHints) >= 0.008
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(Carp)
Requires:       perl(XSLoader)

%description
This module implements some optimisations in compiled Perl code, which
should make it run slightly faster without visibly affecting behaviour. The
optimisations are applied at the peephole optimisation step, augmenting
Perl's built-in optimisations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-GoFaster-%{version}

%build
perl Build.PL --installdirs=vendor --optimize="%{optflags}"
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Devel*
%{_mandir}/man3/*

%changelog
%autochangelog
