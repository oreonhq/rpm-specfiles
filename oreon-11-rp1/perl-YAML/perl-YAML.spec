%global source0_hash a0ce30381657dce8e694df9a09e95d818d13beb03698fd2cf79d0c8d564a9b8e

# Run test
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_YAML_enables_test
%else
%bcond_with perl_YAML_enables_test
%endif
# Run extra test
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_YAML_enables_extra_test
%else
%bcond_with perl_YAML_enables_extra_test
%endif

Name:           perl-YAML
Version:        1.31
Release:        7%{?dist}
Summary:        YAML Ain't Markup Language (tm)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/YAML
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/YAML-%{version}.tar.gz
# Script to remove non-free content from upstream tarball
# Usage: YAML-free YAML-%%{version}.tar.gz
Source1:        YAML-free
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) > 6.75
# Module Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
# Avoid circular build deps Test::YAML → Test::Base → YAML when bootstrapping
%if %{with perl_YAML_enables_test} && !%{defined perl_bootstrap}
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::YAML) >= 1.05
BuildRequires:  perl(utf8)
%if %{with perl_YAML_enables_extra_test}
# Author Tests
BuildRequires:  perl(Test::Pod) >= 1.41
%endif
%endif
# Dependencies
Requires:       perl(B::Deparse)
Requires:       perl(Carp)

# Filter private provides:
# perl(yaml_mapping) perl(yaml_scalar) perl(yaml_sequence)
%global __provides_exclude ^perl\\(yaml_

Provides:       perl(YAML)
Provides:       perl(YAML::XS)
Provides:       perl(YAML::Tests)
%description
If you need to use YAML with Perl, it is likely that you will have a look at
this module (YAML.pm) first. There are several YAML modules in Perl and they
all support the simple Load() and Dump() API. Since this one has the obvious
name "YAML", it may seem obvious to pick this one.

The author of this module humbly asks you to choose another. YAML.pm was the
very first YAML implementation in the world, released in 2001. It was
originally made as a prototype, over 2 years before the YAML 1.0 spec was
published. Although it may work for your needs, it has numerous bugs and is
barely maintained.

Please consider using these first:
 * YAML::PP - Pure Perl, full featured, well maintained
 * YAML::PP::LibYAML - A libyaml Perl binding like YAML::XS but with the
   YAML::PP API

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n YAML-%{version}
rm t/load-slides.t
sed -i -e '/^t\/load-slides.t/d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
# Avoid circular build deps Test::YAML → Test::Base → YAML when bootstrapping
%if %{with perl_YAML_enables_test} && !%{defined perl_bootstrap}
make test AUTHOR_TESTING=%{with perl_YAML_enables_extra_test}
%endif

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%dir %{perl_vendorlib}/YAML/
%dir %{perl_vendorlib}/YAML/Dumper/
%dir %{perl_vendorlib}/YAML/Loader/
%doc %{perl_vendorlib}/YAML.pod
%doc %{perl_vendorlib}/YAML/Any.pod
%doc %{perl_vendorlib}/YAML/Dumper.pod
%doc %{perl_vendorlib}/YAML/Dumper/Base.pod
%doc %{perl_vendorlib}/YAML/Error.pod
%doc %{perl_vendorlib}/YAML/Loader.pod
%doc %{perl_vendorlib}/YAML/Loader/Base.pod
%doc %{perl_vendorlib}/YAML/Marshall.pod
%doc %{perl_vendorlib}/YAML/Node.pod
%doc %{perl_vendorlib}/YAML/Tag.pod
%doc %{perl_vendorlib}/YAML/Types.pod
%{perl_vendorlib}/YAML.pm
%{perl_vendorlib}/YAML/Any.pm
%{perl_vendorlib}/YAML/Dumper.pm
%{perl_vendorlib}/YAML/Dumper/Base.pm
%{perl_vendorlib}/YAML/Error.pm
%{perl_vendorlib}/YAML/Loader.pm
%{perl_vendorlib}/YAML/Loader/Base.pm
%{perl_vendorlib}/YAML/Marshall.pm
%{perl_vendorlib}/YAML/Mo.pm
%{perl_vendorlib}/YAML/Node.pm
%{perl_vendorlib}/YAML/Tag.pm
%{perl_vendorlib}/YAML/Types.pm
%{_mandir}/man3/YAML.3*
%{_mandir}/man3/YAML::Any.3*
%{_mandir}/man3/YAML::Dumper.3*
%{_mandir}/man3/YAML::Dumper::Base.3*
%{_mandir}/man3/YAML::Error.3*
%{_mandir}/man3/YAML::Loader.3*
%{_mandir}/man3/YAML::Loader::Base.3*
%{_mandir}/man3/YAML::Marshall.3*
%{_mandir}/man3/YAML::Node.3*
%{_mandir}/man3/YAML::Tag.3*
%{_mandir}/man3/YAML::Types.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.31-7
- Import
