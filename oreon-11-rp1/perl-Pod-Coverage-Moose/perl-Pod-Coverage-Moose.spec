%global source0_hash b71d3ab7ed0811109a50d284e333628ef212e5602844bbe47935ddd38a6f8578

Name:           perl-Pod-Coverage-Moose
Version:        0.08
Release:        7%{?dist}
Summary:        Pod::Coverage extension for Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Coverage-Moose
Source0:        https://cpan.metacpan.org/modules/by-module/Pod/Pod-Coverage-Moose-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Moose) >= 2.1300
BuildRequires:  perl(namespace::autoclean) >= 0.08
BuildRequires:  perl(Pod::Coverage)
# Tests:
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
# Optional Tests
BuildRequires:  perl(MooseX::AttributeHelpers)
BuildRequires:  perl(MooseX::Role::WithOverloading)
# Dependencies
# (none)

Provides:       perl(Pod::Coverage::Moose)
Provides:       perl(Pod::Coverage::Moose)
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

%check
./Build test

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/Pod/
%{_mandir}/man3/Pod::Coverage::Moose.3*

%changelog
%autochangelog
