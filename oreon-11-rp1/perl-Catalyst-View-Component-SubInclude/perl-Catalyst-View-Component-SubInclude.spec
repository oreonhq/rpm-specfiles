%global source0_hash 53f9e285c86842ba4abedc4481ab0e75c3f0a59fd8bf1b1848c3e18ae617f1ec
Name:           perl-Catalyst-View-Component-SubInclude
Version:        0.10
Release:        44%{?dist}
Summary:        Use subincludes in your Catalyst views
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-View-Component-SubInclude
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-View-Component-SubInclude-%{version}.tar.gz
Patch0:         Catalyst-View-Component-SubInclude-0.10-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
Requires:       perl(Catalyst::Plugin::SubRequest)
Requires:       perl(Catalyst) >= 5.80014
Requires:       perl(Catalyst::Runtime) >= 5.80014
Requires:       perl(Catalyst::View::TT)
Requires:       perl(MooseX::Types)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Action::RenderView)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Plugin::SubRequest)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(Catalyst::View::TT)
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Catalyst::View::Component::SubInclude allows you to include content in your
templates (or, more generally, somewhere in your view's render processing)
which comes from another action in your application. It's implemented as a
Moose::Role, so using Moose in your view is required.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-View-Component-SubInclude-%{version}
%patch -P0 -p1

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
