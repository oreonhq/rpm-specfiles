%global source0_hash 784f4e55efa149f8910400de71309047cdb561ef123bd3c3a6b8015356a88e1f
Name:           perl-MooseX-InsideOut
Version:        0.106
Release:        1%{?dist}
Summary:        Inside-out objects with Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-InsideOut
Source0:        https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-InsideOut-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Class::MOP) >= 0.80
Requires:       perl(Moose) >= 0.94
Requires:       perl(namespace::clean) >= 0.11
Provides:       perl(MooseX::InsideOut)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Hash::Util::FieldHash::Compat)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
MooseX::InsideOut provides meta-roles for inside-out objects. That is, it
sets up attribute slot storage somewhere other than inside $self. This
means that you can extend non-Moose classes, whose internals you either
don't want to care about or aren't hash-based.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-InsideOut-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test RELEASE_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
