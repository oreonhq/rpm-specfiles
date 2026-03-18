# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Ref_Util_enables_optional_test
%else
%bcond_with perl_Ref_Util_enables_optional_test
%endif

Name:		perl-Ref-Util
Version:	0.204
Release:	24%{?dist}
Summary:	Utility functions for checking references
License:	MIT
URL:		https://metacpan.org/release/Ref-Util
Source0:	https://cpan.metacpan.org/modules/by-module/Ref/Ref-Util-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(lib)
BuildRequires:	perl(Text::ParseWords)
# Dependencies of bundled ExtUtils::HasCompiler
BuildRequires:	gcc
BuildRequires:	perl-devel
BuildRequires:	perl(base)
BuildRequires:	perl(Config)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
# Module
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IPC::Open2)
BuildRequires:	perl(Ref::Util::XS)
BuildRequires:	perl(Test::More) >= 0.96
%if %{with perl_Ref_Util_enables_optional_test}
# Optional Tests
BuildRequires:	perl(B::Concise)
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(Readonly)
%endif
# Dependencies
Requires:	perl(Ref::Util::XS)

%description
Ref::Util introduces several functions to help identify references in a faster
and smarter way.

%prep
%setup -q -n Ref-Util-%{version}

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
%doc Changes README
%{perl_vendorlib}/Ref/
%{_mandir}/man3/Ref::Util.3*
%{_mandir}/man3/Ref::Util::PP.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.204-24
- Prepare for Oreon 11 (RP1)
