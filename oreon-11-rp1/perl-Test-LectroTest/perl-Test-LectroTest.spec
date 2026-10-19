%global source0_hash ac2b4f0d95899af1a1a1ec784cb740b2b90256abee11c83e7b291103ec9ed735
Name:           perl-Test-LectroTest
Version:        0.5001
Release:        1%{?dist}
Summary:        Easy, automatic, specification-based tests
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-LectroTest
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMOERTEL/Test-LectroTest-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
