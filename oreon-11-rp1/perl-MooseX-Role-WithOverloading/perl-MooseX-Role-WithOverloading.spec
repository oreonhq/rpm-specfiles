%global source0_hash 92b095d73f1220f9c2ed2d3aaa5ba072eb5aa2de209b7c455da5a8701b986865
Name:           perl-MooseX-Role-WithOverloading
Version:        0.17
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Roles that support overloading
URL:            https://metacpan.org/release/MooseX-Role-WithOverloading
Source0:        https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-Role-WithOverloading-%{version}.tar.gz
Requires:       perl(XSLoader)
%{?perl_default_filter}
Provides:       perl(MooseX::Role::WithOverloading)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(aliased)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
MooseX::Role::WithOverloading allows you to write a Moose::Role
that defines overloaded operators and allows those operator
overloadings to be composed into the classes/roles/instances it's
compiled to, while plain roles would lose the overloading.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-Role-WithOverloading-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

AUTHOR_TESTING=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
