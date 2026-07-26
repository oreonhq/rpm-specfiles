%global source0_hash a8c601db345cf6929812f382062f71f5eaacad3f4f1be15b3be9d73d291a74dd

Name:           perl-Devel-Confess
Version:        0.009004
Release:        27%{?dist}
Summary:        Include stack traces on all warnings and errors
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Confess
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Devel-Confess-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
# Win32::Console::ANSI - not used
# Tests
BuildRequires:  perl-debugger
BuildRequires:  perl(base)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter::Heavy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(threads)
# Optional tests
BuildRequires:  perl(UNIVERSAL::can)
BuildRequires:  perl(UNIVERSAL::isa)
Requires:       perl(Data::Dumper)

%description
This module is meant as a debugging aid. It can be used to make a script
complain loudly with stack backtraces when warn()ing or die()ing. Unlike
other similar modules (e.g. Carp::Always), stack traces will also be
included when exception objects are thrown.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Confess-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
