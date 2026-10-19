%global source0_hash 3cfe80098372dee5cbe465dc1e5e668037b75dd28442479fb5f66340c4660b99
Name:           perl-Task-Moose
Version:        0.03
Release:        38%{?dist}
Summary:        Moose in a box
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Task-Moose
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/Task-Moose-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moose) >= 0.92
Requires:       perl(MooseX::StrictConstructor) >= 0.08
Requires:       perl(MooseX::Params::Validate) >= 0.06
Requires:       perl(MooseX::Role::TraitConstructor)
Requires:       perl(MooseX::Traits)
Requires:       perl(MooseX::Object::Pluggable)
Requires:       perl(MooseX::Role::Parameterized)
Requires:       perl(MooseX::GlobRef)
Requires:       perl(MooseX::InsideOut)
Requires:       perl(MooseX::Singleton) >= 0.20
Requires:       perl(MooseX::NonMoose) >= 0.06
Requires:       perl(MooseX::Declare)
Requires:       perl(MooseX::Method::Signatures)
Requires:       perl(TryCatch)
Requires:       perl(MooseX::Types) >= 0.20
Requires:       perl(MooseX::Types::Structured)
Requires:       perl(MooseX::Types::Path::Class)
Requires:       perl(MooseX::Types::Set::Object)
Requires:       perl(MooseX::Types::DateTime)
Requires:       perl(MooseX::Getopt)
Requires:       perl(MooseX::ConfigFromFile)
Requires:       perl(MooseX::SimpleConfig)
Requires:       perl(MooseX::App::Cmd)
Requires:       perl(MooseX::Role::Cmd)
Requires:       perl(MooseX::LogDispatch)
Requires:       perl(MooseX::LazyLogDispatch)
Requires:       perl(MooseX::Log::Log4perl)
Requires:       perl(MooseX::POE)
Requires:       perl(MooseX::Workers)
Requires:       perl(MooseX::Daemonize)
Requires:       perl(MooseX::Param)
Requires:       perl(MooseX::Iterator)
Requires:       perl(MooseX::Clone)
Requires:       perl(MooseX::Storage)
Requires:       perl(Moose::Autobox)
Requires:       perl(MooseX::ClassAttribute)
Requires:       perl(MooseX::SemiAffordanceAccessor)
Requires:       perl(namespace::autoclean) >= 0.09
Requires:       perl(Pod::Coverage::Moose)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Autobox)
BuildRequires:  perl(MooseX::App::Cmd)
BuildRequires:  perl(MooseX::ClassAttribute)
BuildRequires:  perl(MooseX::Clone)
BuildRequires:  perl(MooseX::ConfigFromFile)
BuildRequires:  perl(MooseX::Daemonize)
BuildRequires:  perl(MooseX::Declare)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::GlobRef)
BuildRequires:  perl(MooseX::InsideOut)
BuildRequires:  perl(MooseX::Iterator)
BuildRequires:  perl(MooseX::LazyLogDispatch)
BuildRequires:  perl(MooseX::Log::Log4perl)
BuildRequires:  perl(MooseX::LogDispatch)
BuildRequires:  perl(MooseX::Method::Signatures)
BuildRequires:  perl(MooseX::NonMoose)
BuildRequires:  perl(MooseX::Object::Pluggable)
BuildRequires:  perl(MooseX::POE)
BuildRequires:  perl(MooseX::Param)
BuildRequires:  perl(MooseX::Params::Validate)
BuildRequires:  perl(MooseX::Role::Cmd)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(MooseX::Role::TraitConstructor)
BuildRequires:  perl(MooseX::SemiAffordanceAccessor)
BuildRequires:  perl(MooseX::SimpleConfig)
BuildRequires:  perl(MooseX::Singleton)
BuildRequires:  perl(MooseX::Storage)
BuildRequires:  perl(MooseX::StrictConstructor)
BuildRequires:  perl(MooseX::Traits)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::DateTime)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(MooseX::Types::Set::Object)
BuildRequires:  perl(MooseX::Types::Structured)
BuildRequires:  perl(MooseX::Workers)
BuildRequires:  perl(Pod::Coverage::Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(TryCatch)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl-generators
# /oreon:deps
%description
This Task installs Moose and a number of Moose extensions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Task-Moose-%{version}
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT 
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
