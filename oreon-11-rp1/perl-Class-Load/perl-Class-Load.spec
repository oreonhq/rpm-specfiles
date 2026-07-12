%global source0_hash 2a48fa779b5297e56156380e8b32637c6c58decb4f4a7f3c7350523e11275f8f

# Class::Load::XS is an optional extra
%if 0%{?rhel:1}
%bcond_with Class_Load_XS
%else
%bcond_without Class_Load_XS
%endif

Name:		perl-Class-Load
Version:	0.25
Release:	29%{?dist}
Summary:	A working (require "Class::Name") and more
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Class-Load
Source0:	https://cpan.metacpan.org/modules/by-module/Class/Class-Load-%{version}.tar.gz
BuildArch:	noarch
# ===================================================================
# Module build requirements
# ===================================================================
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Data::OptList) >= 0.110
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Module::Implementation) >= 0.04
BuildRequires:	perl(Module::Runtime) >= 0.012
BuildRequires:	perl(Package::Stash) >= 0.14
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Try::Tiny)
# ===================================================================
# Regular test suite requirements
# ===================================================================
# Class::Load::XS → Class::Load
%if 0%{!?perl_bootstrap:1} && %{with Class_Load_XS}
BuildRequires:	perl(Class::Load::XS)
%endif
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Needs)
BuildRequires:	perl(Test::Without::Module)
BuildRequires:	perl(version)
# ===================================================================
# Runtime requirements
# ===================================================================
# Also requires core module perl(Exporter) via a "use base" construct

Provides:       perl(Class::Load)
Provides:       perl(Class::Load)
%description
require EXPR only accepts Class/Name.pm style module names, not Class::Name.
How frustrating! For that, we provide load_class 'Class::Name'.

It's often useful to test whether a module can be loaded, instead of throwing
an error when it's not available. For that, we provide
try_load_class 'Class::Name'.

Finally, sometimes we need to know whether a particular class has been loaded.
Asking %%INC is an option, but that will miss inner packages and any class for
which the filename does not correspond to the package name. For that, we
provide is_class_loaded 'Class::Name'.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Class-Load-%{version}

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
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/Class/
%{_mandir}/man3/Class::Load.3*

%changelog
%autochangelog
