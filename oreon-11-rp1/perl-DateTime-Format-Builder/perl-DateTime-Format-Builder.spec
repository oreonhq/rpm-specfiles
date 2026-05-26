# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 61ffb23d85b3ca1786b2da3289e99b57e0625fe0e49db02a6dc0cb62c689e2f2
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%if 0%{?rhel} >= 9
%bcond_with perl_DateTime_Format_Builder_enable_optional_tests
%else
%bcond_without perl_DateTime_Format_Builder_enable_optional_tests
%endif

%global real_version   0.83

Name:           perl-DateTime-Format-Builder
# 0.83 in reality, but rpm can't get it
Version:        0.8300
Release:        17%{?dist}
Summary:        Create DateTime parser classes and objects        
# examples/W3CDTF.pm:               GPL-1.0-or-later OR Artistic-1.0-Perl
# examples/MySQL.pm:                GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/DateTime/Format/Builder.pm:   Artistic-2.0
# LICENSE:                          Artistic-2.0 text
License:        Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/DateTime-Format-Builder            
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-Builder-0.83.tar.gz

BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  sed
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime) >= 1.00
BuildRequires:  perl(DateTime::Format::Strptime) >= 1.04
BuildRequires:  perl(Params::Validate) >= 0.72
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88
# Optional Tests
%if %{with perl_DateTime_Format_Builder_enable_optional_tests}
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(DateTime::Format::HTTP)
BuildRequires:  perl(DateTime::Format::Mail)
BuildRequires:  perl(DateTime::Format::IBeat)
BuildRequires:  perl(Devel::Cycle) >= 1.07
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
# Dependencies
Provides:       perl(DateTime::Format::Builder) = %{version}

# Avoid doc-file dependencies from tests
%{?perl_default_filter}

%description
DateTime::Format::Builder creates DateTime parsers. Many string formats of
dates and times are simple and just require a basic regular expression to
extract the relevant information. Builder provides a simple way to do this
without writing reams of structural code.

Builder provides a number of methods, most of which you'll never need, or at
least rarely need. They're provided more for exposing of the module's innards
to any sub-classes, or for when you need to do something slightly beyond what
is expected.

%prep
%oreon_verify_sources
%setup -q -n DateTime-Format-Builder-%{real_version}

# POD doesn't like E<copy> very much...
perl -pi -e 's/E<copy>/(C)/' `find lib/ -type f`

# Silence rpmlint
sed -i '1s~^#!.*perl~#!%{__perl}~' t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md examples/ t/
%{perl_vendorlib}/DateTime/
%{_mandir}/man3/DateTime::Format::Builder.3*
%{_mandir}/man3/DateTime::Format::Builder::Parser.3*
%{_mandir}/man3/DateTime::Format::Builder::Parser::Dispatch.3*
%{_mandir}/man3/DateTime::Format::Builder::Parser::Quick.3*
%{_mandir}/man3/DateTime::Format::Builder::Parser::Regex.3*
%{_mandir}/man3/DateTime::Format::Builder::Parser::Strptime.3*
%{_mandir}/man3/DateTime::Format::Builder::Parser::generic.3*
%{_mandir}/man3/DateTime::Format::Builder::Tutorial.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8300-17
- Prepare for Oreon 11 (RP1)
