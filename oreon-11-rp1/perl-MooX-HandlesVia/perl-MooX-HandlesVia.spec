%global source0_hash 716353e38894ecb7e8e4c17bc95483db5f59002b03541b54a72c27f2a8f36c12

Name:           perl-MooX-HandlesVia
Version:        0.001009
Release:        16%{?dist}
Summary:        NativeTrait-like behavior for Moo
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-HandlesVia
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/MooX-HandlesVia-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators

BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Data::Perl) >= 0.002006
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.003000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Types::MooseLike::Base) >= 0.23
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(strictures) >= 1
BuildRequires:  perl(warnings)

# Redundant to BR: perl(Data::Perl)
BuildRequires:  perl(Data::Perl::Role::Bool)
BuildRequires:  perl(Data::Perl::Role::Code)
BuildRequires:  perl(Data::Perl::Role::Collection::Array)
BuildRequires:  perl(Data::Perl::Role::Collection::Hash)
BuildRequires:  perl(Data::Perl::Role::Counter)
BuildRequires:  perl(Data::Perl::Role::Number)
BuildRequires:  perl(Data::Perl::Role::String)

Requires:       perl(Data::Perl) >= 0.002006
Requires:       perl(Moo) >= 1.003000

Provides:       perl(MooX::HandlesVia)
Provides:       perl(MooX::HandlesVia)
%description
MooX::HandlesVia is an extension of Moo's 'handles' attribute
functionality. It provides a means of proxying functionality from an
external class to the given atttribute. This is most commonly used as a way
to emulate 'Native Trait' behavior that has become commonplace in Moose
code, for which there was no Moo alternative.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooX-HandlesVia-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes TODO
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
