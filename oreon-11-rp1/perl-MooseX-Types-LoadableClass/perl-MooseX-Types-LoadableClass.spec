%global source0_hash f105b69bcb44cd9856edfd62753ff58c35519ffa96e17cfc9ef30bdb98994ccc

Name:           perl-MooseX-Types-LoadableClass
Version:        0.016
Release:        3%{?dist}
Summary:        ClassName type constraint with coercion to load the class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/MooseX-Types-LoadableClass
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-LoadableClass-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny) >= 0.030
# Run-time:
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)

%{?perl_default_filter}

%description
ClassName type constraint with coercion to load the class.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-LoadableClass-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install '--destdir=%{buildroot}' --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%license LICENCE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*

%changelog
%autochangelog
