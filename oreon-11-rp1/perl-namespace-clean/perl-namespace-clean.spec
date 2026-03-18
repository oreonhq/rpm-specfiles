# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_namespace_clean_enables_optional_test
%else
%bcond_with perl_namespace_clean_enables_optional_test
%endif

Name:		perl-namespace-clean
Summary:	Keep your namespace tidy
Version:	0.27
Release:	30%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/namespace-clean
Source0:	https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/namespace-clean-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter >= 4:5.12
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
# Module Runtime
BuildRequires:	perl(B::Hooks::EndOfScope) >= 0.12
BuildRequires:	perl(base)
BuildRequires:	perl(constant)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Package::Stash) >= 0.23
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Config)
BuildRequires:	perl(DB)
BuildRequires:	perl(File::Glob)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(IPC::Open2)
BuildRequires:	perl(lib)
BuildRequires:	perl(sort)
BuildRequires:	perl(Test::More)
%if %{with perl_namespace_clean_enables_optional_test}
# Optional Tests
BuildRequires:	perl(Variable::Magic)
%endif
# Runtime
Requires:	perl(B::Hooks::EndOfScope) >= 0.12
Requires:	perl(Package::Stash) >= 0.23

# Avoid unwanted requires/provides that come with the test suite
%{?perl_default_filter}
# namespace::clean::_Util is a private package
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(namespace::clean::_Util\\)

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
%setup -q -n namespace-clean-%{version}

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
%doc Changes t/
%{perl_vendorlib}/namespace/
%{_mandir}/man3/namespace::clean.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.27-30
- Prepare for Oreon 11 (RP1)
