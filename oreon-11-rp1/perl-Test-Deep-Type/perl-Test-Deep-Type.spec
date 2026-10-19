%global source0_hash 6e7bea1a2f1e75319a22d1c51996ebac50ca5e3663d1bc223130887e62e959f1
Name:           perl-Test-Deep-Type
Version:        0.008
Release:        1%{?dist}
Summary:        Test::Deep plugin for validating type constraints
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Deep-Type
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Deep-Type-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep::Cmp)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(if)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test::Deep::Type provides the sub is_type to indicate that the data being
tested must validate against the passed type. This is an actual type
object, not a string name -- for example something provided via
MooseX::Types, or a plain old coderef that returns a bool (such as what
might be used in a Moo type constraint).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Deep-Type-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
