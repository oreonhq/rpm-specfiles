%global source0_hash d3b32c82e1d2caa9d58b8c8075965240e6cab66ab9350bd6f6bea4ca07e938d6
%bcond_with perl_namespace_autoclean_enables_optional_test
Name:           perl-namespace-autoclean
Version:        0.31
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Keep imports out of your namespace
URL:            https://metacpan.org/release/namespace-autoclean
Source0:        https://cpan.metacpan.org/modules/by-module/namespace/namespace-autoclean-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_namespace_autoclean_enables_optional_test}
%if ! %{defined perl_bootstrap}
%endif
%endif
Requires:       perl(Sub::Util) >= 1.40
Provides:       perl(namespace::autoclean)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B::Hooks::EndOfScope)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(constant)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
When you import a function into a Perl package, it will naturally also be
available as a method. The 'namespace::autoclean' pragma will remove all
imported symbols at the end of the current package's compile cycle. Functions
called in the package itself will still be bound by their name, but they won't
show up as methods on your class or instances. This module is very similar to
namespace::clean, except it will clean all imported functions, no matter if you
imported them before or after you 'use'd the pragma. It will also not touch
anything that looks like a method.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n namespace-autoclean-%{version}

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.31-4
- Prepare for Oreon 11 (RP1)
