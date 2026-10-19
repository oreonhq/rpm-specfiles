%global source0_hash 8a10a83c3e183dc78f9e7b7aa4d09b47c11fb4e7d3a33b9a12912fd22e31af9d
%bcond_with perl_namespace_clean_enables_optional_test
Name:		perl-namespace-clean
Summary:        Keep your namespace tidy
Version:	0.27
Release:        30%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/namespace-clean
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/namespace-clean-%{version}.tar.gz
BuildArch:	noarch
%if %{with perl_namespace_clean_enables_optional_test}
%endif
Requires:	perl(B::Hooks::EndOfScope) >= 0.12
Requires:	perl(Package::Stash) >= 0.23
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(namespace::clean::_Util\\)
Provides:       perl(namespace::clean)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B::Hooks::EndOfScope)
BuildRequires:  perl(Config)
BuildRequires:  perl(DB)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(sort)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
When you define a function, or import one, into a Perl package, it will
naturally also be available as a method. This does not per se cause
problems, but it can complicate subclassing and, for example, plugin
classes that are included via multiple inheritance by loading them as
base classes.

The 'namespace::clean' pragma will remove all previously declared or
imported symbols at the end of the current package's compile cycle.
Functions called in the package itself will still be bound by their
name, but they won't show up as methods on your class or instances.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n namespace-clean-%{version}

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.27-30
- Prepare for Oreon 11 (RP1)
