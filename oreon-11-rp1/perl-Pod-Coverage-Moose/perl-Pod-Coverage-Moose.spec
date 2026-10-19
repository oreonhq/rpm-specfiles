%global source0_hash b71d3ab7ed0811109a50d284e333628ef212e5602844bbe47935ddd38a6f8578
Name:           perl-Pod-Coverage-Moose
Version:        0.08
Release:        1%{?dist}
Summary:        Pod::Coverage extension for Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Coverage-Moose
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-Coverage-Moose-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Pod::Coverage::Moose)
Provides:       perl(Pod::Coverage::Moose)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::AttributeHelpers)
BuildRequires:  perl(MooseX::Role::WithOverloading)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
When using Pod::Coverage in combination with Moose, it will report any
method imported from a Role. This is especially bad when used in
combination with Test::Pod::Coverage, since it takes away its ease of use.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-Coverage-Moose-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
