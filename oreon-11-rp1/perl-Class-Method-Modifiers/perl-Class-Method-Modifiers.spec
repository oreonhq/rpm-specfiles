%global source0_hash 65cd85bfe475d066e9186f7a8cc636070985b30b0ebb1cde8681cf062c2e15fc
%{bcond_with perl_Class_Method_Modifiers_enables_optional_test}
Name:           perl-Class-Method-Modifiers
Summary:        Provides Moose-like method modifiers
Version:        2.15
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Method-Modifiers
Source0:        https://cpan.metacpan.org/modules/by-module/Class/Class-Method-Modifiers-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Class_Method_Modifiers_enables_optional_test}
%endif
Requires:       perl(B)
Requires:       perl(Carp)
%{?perl_default_filter}
Provides:       perl(Class::Method::Modifiers)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(if)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Method modifiers are a powerful feature from the CLOS (Common Lisp Object
System) world.

In its most basic form, a method modifier is just a method that calls
'$self->SUPER::foo(@_)'. I for one have trouble remembering that exact
invocation, so my classes seldom re-dispatch to their base classes. Very
bad!

'Class::Method::Modifiers' provides three modifiers: 'before', 'around',
and 'after'. 'before' and 'after' are run just before and after the method
they modify, but can not really affect that original method. 'around' is
run in place of the original method, with a hook to easily call that
original method. See the 'MODIFIERS' section for more details on how the
particular modifiers work.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Class-Method-Modifiers-%{version}

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.15-8
- Prepare for Oreon 11 (RP1)
