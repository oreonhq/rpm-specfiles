%global source0_hash ea0944f2f5ec98d895bef6d503e6e4a376fea6383a6bc64c7670d46ff2218cad
%bcond_with perl_Eval_Closure_enables_optional_test
Name:           perl-Eval-Closure
Version:        0.14
Release:        1%{?dist}
Summary:        Safely and cleanly create closures via string eval
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Eval-Closure
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/Eval-Closure-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Eval_Closure_enables_optional_test}
%endif
Requires:       perl(Devel::LexAlias) >= 0.05
Requires:       perl(Perl::Tidy)
Provides:       perl(Eval::Closure)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::LexAlias)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
String eval is often used for dynamic code generation. For instance, Moose uses
it heavily, to generate inlined versions of accessors and constructors, which
speeds code up at runtime by a significant amount. String eval is not without
its issues however - it's difficult to control the scope it's used in (which
determines which variables are in scope inside the eval), and it can be quite
slow, especially if doing a large number of evals.
 
This module attempts to solve both of those problems. It provides an
eval_closure function, which evals a string in a clean environment, other than
a fixed list of specified variables. It also caches the result of the eval, so
that doing repeated evals of the same source, even with a different
environment, will be much faster (but note that the description is part of the
string to be evaled, so it must also be the same (or non-existent) if caching
is to work properly).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Eval-Closure-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14-27
- Prepare for Oreon 11 (RP1)
