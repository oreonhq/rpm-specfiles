# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 1f300d034f46298cb92960912cc04bac33fb27f05b8852d8f051e110b9cd995f
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Perform author tests
%bcond_without perl_Test_YAML_enables_extra_test

Name:		perl-Test-YAML
Version:	1.07
Release:	23%{?dist}
Summary:	Testing Module for YAML Implementations
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-YAML
Source0:	https://cpan.metacpan.org/authors/id/T/TI/TINITA/Test-YAML-1.07.tar.gz

BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) > 6.75
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Test::Base) >= 0.89
BuildRequires:	perl(Test::Base::Filter)
# Test Suite
BuildRequires:	perl(Test::More)
%if %{with perl_Test_YAML_enables_extra_test}
BuildRequires:	perl(Test::Pod) >= 1.41
%endif
# Dependencies
Requires:	perl(Data::Dumper)

%description
Test::YAML is a subclass of Test::Base with YAML specific support.

%prep
%oreon_verify_sources
%setup -q -n Test-YAML-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}

# Exclude script that does nothing
rm %{buildroot}%{_bindir}/test-yaml

%check
unset AUTHOR_TESTING
make test %{?with_perl_Test_YAML_enables_extra_test:AUTHOR_TESTING=1}

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::YAML.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.07-23
- Prepare for Oreon 11 (RP1)
