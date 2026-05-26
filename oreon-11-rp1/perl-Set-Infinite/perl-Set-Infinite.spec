Name:           perl-Set-Infinite
Version:        0.65
Release:        44%{?dist}
Summary:        Sets of intervals
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Set-Infinite
Source0:        https://cpan.metacpan.org/authors/id/F/FG/FGLOCK/Set-Infinite-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 07bc880734492de40b4a3a8b5a331762f64e69b4629029fd9a9d357b25b87e1f
%global source0_file Set-Infinite-0.65.tar.gz
# oreon url source checksums end
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
Set::Infinite is a Set Theory module for infinite sets.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Set-Infinite-0.65.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "07bc880734492de40b4a3a8b5a331762f64e69b4629029fd9a9d357b25b87e1f" || { echo "oreon: Source0 SHA256 mismatch for Set-Infinite-0.65.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Set-Infinite-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.65-44
- Prepare for Oreon 11 (RP1)
