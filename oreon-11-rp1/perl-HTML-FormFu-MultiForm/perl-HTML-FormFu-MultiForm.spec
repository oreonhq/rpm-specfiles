%global source0_hash 36f00cd76bb896e4da09dd2bb0e5d890667f70c78f54251af4d258c82149159f
Name:           perl-HTML-FormFu-MultiForm
Version:        1.03
Release:        1%{?dist}
Summary:        Handle multi-page/stage forms
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-FormFu-MultiForm
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NIGELM/HTML-FormFu-MultiForm-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Crypt::Cipher::AES)
Requires:       perl(HTML::FormFu::Role::FormAndElementMethods)
Requires:       perl(HTML::FormFu::Role::FormBlockAndFieldMethods)
Requires:       perl(HTML::FormFu::Role::NestedHashUtils)
Requires:       perl(HTML::FormFu::Role::Populate)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Crypt::Cipher::AES)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Spec)
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
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
