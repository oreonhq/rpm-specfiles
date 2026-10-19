%global source0_hash 7b6497173f1b6adb29f5d51d8cf9ec36d2f1219412b4b2410e9d77a901e84a6d
%bcond_with perl_Params_ValidationCompiler_enables_optional_test
Name:		perl-Params-ValidationCompiler
Version:	0.31
Release:        1%{?dist}
Summary:        Build an optimized subroutine parameter validator once, use it forever
License:	Artistic-2.0
URL:		https://metacpan.org/release/Params-ValidationCompiler
Source0:        https://cpan.metacpan.org/modules/by-module/Params/Params-ValidationCompiler-%{version}.tar.gz
BuildArch:	noarch
%if %{with perl_Params_ValidationCompiler_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
Recommends:	perl(Class::XSAccessor) >= 1.17
Recommends:	perl(Sub::Util) >= 1.40
Provides:       perl(Params::ValidationCompiler)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Specio)
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test2::Plugin::NoWarnings)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Create a customized, optimized, non-lobotomized, uncompromised, and thoroughly
specialized parameter checking subroutine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Params-ValidationCompiler-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.31-9
- Prepare for Oreon 11 (RP1)
