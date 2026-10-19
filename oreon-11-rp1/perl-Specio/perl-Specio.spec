%global source0_hash 0d0eecfb9e89bd0f5f710fac42e1200a882d513a862f98497eaef5927ac6c183
%bcond_with perl_Specio_enables_optional_test
Name:		perl-Specio
Version:	0.53
Release:        2%{?dist}
Summary:        Type constraints and coercions for Perl
License:	Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:		https://metacpan.org/release/Specio
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Specio-%{version}.tar.gz
BuildArch:	noarch
%if %{with perl_Specio_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
Requires:	perl(Ref::Util) >= 0.112
Requires:	perl(Sub::Util) >= 1.40
Requires:	perl(XString)
%global __provides_exclude ^perl\\(_T::.*\\)
Provides:       perl(Specio)
Provides:       perl(Specio::Declare)
Provides:       perl(Specio::Exporter)
Provides:       perl(Specio::Library::Builtins)
Provides:       perl(Specio::Library::Numeric)
Provides:       perl(Specio::Library::String)
Provides:       perl(Specio::Subs)
Provides:       perl(Specio::PartialDump)
Provides:       perl(Test::Specio)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Clone::PP)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Implementation)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(XString)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Specio distribution provides classes for representing type constraints
and coercion, along with syntax sugar for declaring them.

Note that this is not a proper type system for Perl. Nothing in this
distribution will magically make the Perl interpreter start checking a value's
type on assignment to a variable. In fact, there's no built-in way to apply a
type to a variable at all.

Instead, you can explicitly check a value against a type, and optionally coerce
values to that type.

%package -n perl-Test-Specio
Summary:	Test helpers for Specio
License:	Artistic-2.0
Requires:	%{name} = %{version}-%{release}
%description -n perl-Test-Specio
This package provides some helper functions and variables for testing Specio
types.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Specio-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles perl-Test-Specio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Specio -f %{oreon_filedir}/perl-Test-Specio.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.53-2
- Prepare for Oreon 11 (RP1)
