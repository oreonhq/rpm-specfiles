%global source0_hash 28d5695400c0f4e2bd209793cb74f6da2b9257356aacb2947c603425e09618d6

Name:           perl-Lingua-EN-Number-IsOrdinal
Version:        0.05
Release:        31%{?dist}
Summary:        Detect if English number is ordinal or cardinal
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-EN-Number-IsOrdinal
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/Lingua-EN-Number-IsOrdinal-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Lingua::EN::FindNumber)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny)

%description
This module will tell you if a number, either in words or as digits, is a
cardinal or ordinal number.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-EN-Number-IsOrdinal-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
