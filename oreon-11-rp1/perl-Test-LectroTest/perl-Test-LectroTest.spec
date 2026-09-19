%global source0_hash ac2b4f0d95899af1a1a1ec784cb740b2b90256abee11c83e7b291103ec9ed735

Name:           perl-Test-LectroTest
Version:        0.5001
Release:        37%{?dist}
Summary:        Easy, automatic, specification-based tests
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-LectroTest
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMOERTEL/Test-LectroTest-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Filter::Util::Call)
# POSIX is optional
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
# Optional tests:
# Module::Signature not needed
# Socket not needed
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00

%description
LectroTest is an automated, specification-based testing system. To use it,
declare properties that specify the expected behavior of your software. Then
invoke LectroTest to test whether those properties hold.

LectroTest does this by running repeated random trials against your software.
If LectroTest finds that a property doesn't hold, it emits the counterexample
that "broke" your software. You can then plug the counterexample into your
software to debug the problem.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-LectroTest-%{version}
# Remove test know to fail, bug #1p28134
rm t/gens.t
sed -i -e '/^t\/gens\.t/d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README THANKS TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
