# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 7b6497173f1b6adb29f5d51d8cf9ec36d2f1219412b4b2410e9d77a901e84a6d
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Params_ValidationCompiler_enables_optional_test
%else
%bcond_with perl_Params_ValidationCompiler_enables_optional_test
%endif

Name:		perl-Params-ValidationCompiler
Version:	0.31
Release:	9%{?dist}
Summary:	Build an optimized subroutine parameter validator once, use it forever
License:	Artistic-2.0
URL:		https://metacpan.org/release/Params-ValidationCompiler
Source0:	https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Params-ValidationCompiler-0.31.tar.gz

BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) > 6.75
# Module
BuildRequires:	perl(B)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::XSAccessor) >= 1.17
BuildRequires:	perl(Eval::Closure)
BuildRequires:	perl(Exception::Class)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(List::Util) >= 1.29
BuildRequires:	perl(overload)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Optional Functionality
BuildRequires:	perl(Sub::Util) >= 1.40
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Specio) >= 0.14
BuildRequires:	perl(Specio::Declare)
BuildRequires:	perl(Specio::Library::Builtins)
BuildRequires:	perl(Test2::Plugin::NoWarnings)
BuildRequires:	perl(Test2::Require::Module)
BuildRequires:	perl(Test2::V0)
BuildRequires:	perl(Test::More) >= 1.302015
BuildRequires:	perl(Test::Without::Module)
%if %{with perl_Params_ValidationCompiler_enables_optional_test}
# Optional Tests
BuildRequires:	perl(Const::Fast)
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
BuildRequires:	perl(Hash::Util)
%if !%{defined perl_bootstrap}
# Avoid build dependency cycles via Moose and DateTime
BuildRequires:	perl(Moose::Util::TypeConstraints)
BuildRequires:	perl(Types::Standard)
%endif
%endif
# Dependencies
Recommends:	perl(Class::XSAccessor) >= 1.17
Recommends:	perl(Sub::Util) >= 1.40

%description
Create a customized, optimized, non-lobotomized, uncompromised, and thoroughly
specialized parameter checking subroutine.

%prep
%oreon_verify_sources
%setup -q -n Params-ValidationCompiler-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md eg/ README.md
%{perl_vendorlib}/Params/
%{_mandir}/man3/Params::ValidationCompiler.3*
%{_mandir}/man3/Params::ValidationCompiler::Compiler.3*
%{_mandir}/man3/Params::ValidationCompiler::Exceptions.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.31-9
- Prepare for Oreon 11 (RP1)
