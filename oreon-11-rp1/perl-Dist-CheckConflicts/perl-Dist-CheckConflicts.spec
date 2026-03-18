# Run extra test
%if 0%{?fedora}
%bcond_without perl_Dist_CheckConflicts_enables_extra_test
%else
%bcond_with perl_Dist_CheckConflicts_enables_extra_test
%endif

Name:		perl-Dist-CheckConflicts
Version:	0.11
Release:	34%{?dist}
Summary:	Declare version conflicts for your dist
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Dist-CheckConflicts
Source0:	https://cpan.metacpan.org/modules/by-module/Dist/Dist-CheckConflicts-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.30
# Module
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Module::Runtime) >= 0.009
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.88
# Extra Tests
%if %{with perl_Dist_CheckConflicts_enables_extra_test}
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::EOL)
BuildRequires:	perl(Test::NoTabs)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
%endif
# Dependencies
# (none)

%description
One shortcoming of the CPAN clients that currently exist is that they have no
way of specifying conflicting downstream dependencies of modules. This module
attempts to work around this issue by allowing you to specify conflicting
versions of modules separately, and deal with them after the module is done
installing.

For instance, say you have a module Foo, and some other module Bar uses Foo. If
Foo were to change its API in a non-backwards-compatible way, this would cause
Bar to break until it is updated to use the new API. Foo can't just depend on
the fixed version of Bar, because this will cause a circular dependency
(because Bar is already depending on Foo), and this doesn't express intent
properly anyway - Foo doesn't use Bar at all. The ideal solution would be for
there to be a way to specify conflicting versions of modules in a way that would
let CPAN clients update conflicting modules automatically after an existing
module is upgraded, but until that happens, this module will allow users to do
this manually.

%prep
%setup -q -n Dist-CheckConflicts-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test
%if %{with perl_Dist_CheckConflicts_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Dist/
%{_mandir}/man3/Dist::CheckConflicts.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.11-34
- Prepare for Oreon 11 (RP1)
