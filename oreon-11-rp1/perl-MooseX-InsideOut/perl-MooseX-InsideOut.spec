%global source0_hash 784f4e55efa149f8910400de71309047cdb561ef123bd3c3a6b8015356a88e1f

Name:           perl-MooseX-InsideOut
Version:        0.106
Release:        42%{?dist}
Summary:        Inside-out objects with Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-InsideOut
Source0:        https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-InsideOut-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:  perl(Class::MOP) >= 0.80
BuildRequires:  perl(Hash::Util::FieldHash::Compat)
BuildRequires:  perl(Moose) >= 0.94
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(namespace::clean) >= 0.11
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Release Tests
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
# Dependencies
Requires:       perl(Class::MOP) >= 0.80
Requires:       perl(Moose) >= 0.94
Requires:       perl(namespace::clean) >= 0.11

Provides:       perl(MooseX::InsideOut)
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

%check
make test RELEASE_TESTING=1

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/MooseX/
%{_mandir}/man3/MooseX::InsideOut.3*
%{_mandir}/man3/MooseX::InsideOut::Role::Meta::Instance.3*

%changelog
%autochangelog
