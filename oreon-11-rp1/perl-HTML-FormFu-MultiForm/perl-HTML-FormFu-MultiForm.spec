%global source0_hash 36f00cd76bb896e4da09dd2bb0e5d890667f70c78f54251af4d258c82149159f

Name:           perl-HTML-FormFu-MultiForm
Version:        1.03
Release:        27%{?dist}
Summary:        Handle multi-page/stage forms
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-FormFu-MultiForm
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NIGELM/HTML-FormFu-MultiForm-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Crypt::CBC)
# Crypt::Cipher::AES is a default cipher used by the Crypt::CBC, bug #1939432
BuildRequires:  perl(Crypt::Cipher::AES)
BuildRequires:  perl(HTML::FormFu)
BuildRequires:  perl(HTML::FormFu::Attribute)
BuildRequires:  perl(HTML::FormFu::ObjectUtil)
BuildRequires:  perl(HTML::FormFu::QueryType::CGI)
BuildRequires:  perl(HTML::FormFu::Role::FormAndElementMethods)
BuildRequires:  perl(HTML::FormFu::Role::FormBlockAndFieldMethods)
BuildRequires:  perl(HTML::FormFu::Role::NestedHashUtils)
BuildRequires:  perl(HTML::FormFu::Role::Populate)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Attribute::Chained)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
# Test:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(YAML::XS)
# Crypt::Cipher::AES is a default cipher used by the Crypt::CBC, bug #1939432
Requires:       perl(Crypt::Cipher::AES)
Requires:       perl(HTML::FormFu::Role::FormAndElementMethods)
Requires:       perl(HTML::FormFu::Role::FormBlockAndFieldMethods)
Requires:       perl(HTML::FormFu::Role::NestedHashUtils)
Requires:       perl(HTML::FormFu::Role::Populate)

%description
Multi-page support for HTML::FormFu, a Perl HTML form framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-FormFu-MultiForm-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
