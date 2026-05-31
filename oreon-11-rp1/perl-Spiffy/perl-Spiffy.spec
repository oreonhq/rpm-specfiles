%global source0_hash 8f58620a8420255c49b6c43c5ff5802bd25e4f09240c51e5bf2b022833d41da3

# Perform release tests
%bcond_without perl_Spiffy_enables_extra_test

Name:           perl-Spiffy
Version:        0.46
Release:        34%{?dist}
Summary:        Framework for doing object oriented (OO) programming in Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Spiffy
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Spiffy-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
%if %{with perl_Spiffy_enables_extra_test}
# Release Tests:
BuildRequires:  perl(Test::Pod) >= 1.41
%endif
# Dependencies:
Requires:       perl(Data::Dumper)
Requires:       perl(Filter::Util::Call)
Requires:       perl(overload)
Requires:       perl(Scalar::Util)
Requires:       perl(warnings)
Requires:       perl(YAML)

# Filter bogus provide of perl(DB)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DB\\)

%description
"Spiffy" is a framework and methodology for doing object oriented (OO)
programming in Perl. Spiffy combines the best parts of Exporter.pm, base.pm,
mixin.pm and SUPER.pm into one magic foundation class. It attempts to fix all
the nits and warts of traditional Perl OO, in a clean, straightforward and
(perhaps someday) standard way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Spiffy-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
unset RELEASE_TESTING
make test %{?with_perl_Spiffy_enables_extra_test:RELEASE_TESTING=1}

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/Spiffy.pm
%doc %{perl_vendorlib}/Spiffy.pod
%{perl_vendorlib}/Spiffy/
%{_mandir}/man3/Spiffy.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.46-34
- Prepare for Oreon 11 (RP1)
