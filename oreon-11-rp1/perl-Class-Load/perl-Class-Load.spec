%global source0_hash 2a48fa779b5297e56156380e8b32637c6c58decb4f4a7f3c7350523e11275f8f
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_without Class_Load_XS
Name:		perl-Class-Load
Version:	0.25
Release:        1%{?dist}
Summary:        A working (require "Class::Name") and more
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Class-Load
Source0:        https://cpan.metacpan.org/modules/by-module/Class/Class-Load-%{version}.tar.gz
BuildArch:	noarch
%if 0%{!?perl_bootstrap:1} && %{with Class_Load_XS}
%endif
Provides:       perl(Class::Load)
Provides:       perl(Class::Load)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load::XS)
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Implementation)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(version)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
