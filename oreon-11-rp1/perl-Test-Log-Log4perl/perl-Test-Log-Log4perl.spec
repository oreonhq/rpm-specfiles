%global source0_hash 23ebbb05893a05ebfe397fbce55152df8f9d6500125a8042f1aa6cfa93fc23c4

Name:           perl-Test-Log-Log4perl
Version:        0.32
Release:        23%{?dist}
Summary:        Test log4perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Log-Log4perl
Source0:        https://cpan.metacpan.org/authors/id/C/CL/CLKAO/Test-Log-Log4perl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(:VERSION) >= 5.8.8
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Log::Log4perl::Logger)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(overload)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
# Author tests
# Test::Perl::Critic
# Test::Pod 1.00
# Test::Spelling
# Test::Synopsis

%description
This module can be used to test that you're logging the right thing with
Log::Log4perl. It checks that we get what, and only what, we expect logged
by your code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Log-Log4perl-%{version}
# Remove bundled libraries
rm -rf inc/*
sed -i -e '/^inc\// d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
