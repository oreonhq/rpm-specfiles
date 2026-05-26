Name:           perl-Test-FailWarnings
Version:        0.008
Release:        37%{?dist}
Summary:        Add test failures if warnings are caught
License:        Apache-2.0

URL:            https://metacpan.org/release/Test-FailWarnings
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-FailWarnings-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 da34ef9029f6849d6026201d49127d054ee6ac4b979c82210315f5721964a96f
%global source0_file Test-FailWarnings-0.008.tar.gz
# oreon url source checksums end

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.86
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(Capture::Tiny) >= 0.12
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)

%{?perl_default_filter}

%description
This module hooks $SIG{__WARN__} and converts warnings to Test::More's
fail() calls. It is designed to be used with done_testing, when you don't
need to know the test count in advance.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Test-FailWarnings-0.008.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "da34ef9029f6849d6026201d49127d054ee6ac4b979c82210315f5721964a96f" || { echo "oreon: Source0 SHA256 mismatch for Test-FailWarnings-0.008.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Test-FailWarnings-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes CONTRIBUTING LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.008-37
- Prepare for Oreon 11 (RP1)
