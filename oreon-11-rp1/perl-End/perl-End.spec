%global source0_hash f4346857781dd6351d37db43e43824012ac09a96953cc5158985abb6c866172e

Name:           perl-End
Version:        2009110401
Release:        39%{?dist}
Summary:        Generalized END blocks
License:        MIT
URL:            https://metacpan.org/release/End
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABIGAIL/End-%{version}.tar.gz
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
# Tests
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00

%{?perl_default_filter}

%description
The module End exports a single subroutine which allows you to set up some code
that is run whenever the current block is exited, regardless whether that is
due to a return, next, last, redo, exit, die, goto or just reaching the end of
the block.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n End-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
