%global source0_hash d461167b8b4aa9244f736a7a740830141e61dddee301e456bf642e81d3cea193
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_YAML_enables_test
%else
%bcond_with perl_YAML_enables_test
%endif
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_YAML_enables_extra_test
%else
%bcond_with perl_YAML_enables_extra_test
%endif
Name:           perl-YAML
Version:        1.321
Release:        1%{?dist}
Summary:        YAML Ain't Markup Language (tm)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/YAML
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-%{version}.tar.gz
Source1:        YAML-free
BuildArch:      noarch
%if %{with perl_YAML_enables_test} && !%{defined perl_bootstrap}
%if %{with perl_YAML_enables_extra_test}
%endif
%endif
Requires:       perl(B::Deparse)
Requires:       perl(Carp)
%global __provides_exclude ^perl\\(yaml_
Provides:       perl(YAML)
Provides:       perl(YAML::XS)
Provides:       perl(YAML::Tests)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::YAML)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%if %{with perl_YAML_enables_test} && !%{defined perl_bootstrap}
make test AUTHOR_TESTING=%{with perl_YAML_enables_extra_test}
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
