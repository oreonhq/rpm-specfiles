%global source0_hash 6ccf97c824c7737572f535fd4a590bd3fe9ea5e12eaa6beffbef4b179b11b89d
Name:           perl-CatalystX-SimpleLogin
Version:        0.21
Release:        1%{?dist}
Summary:        Provide a simple Login controller which can be reused
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CatalystX-SimpleLogin
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABRAXXA/CatalystX-SimpleLogin-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Catalyst::Action::REST) >= 0.74
Requires:       perl(Catalyst::Plugin::Authentication)
Requires:       perl(Catalyst::Plugin::Session) >= 0.27
Requires:       perl(Catalyst::Runtime) >= 5.80013
Requires:       perl(Catalyst::View::TT)
Requires:       perl(CatalystX::Component::Traits) >= 0.13
Requires:       perl(HTML::FormHandler) >= 0.28001
Requires:       perl(MooseX::MethodAttributes) >= 0.18
Requires:       perl(MooseX::RelatedClassRoles) >= 0.004
Requires:       perl(MooseX::Types)
Requires:       perl(MooseX::Types::Common)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Catalyst::Action::REST)
BuildRequires:  perl(Catalyst::Action::RenderView)
BuildRequires:  perl(Catalyst::ActionRole::ACL)
BuildRequires:  perl(Catalyst::Authentication::Store::DBIx::Class)
BuildRequires:  perl(Catalyst::Model::DBIC::Schema)
BuildRequires:  perl(Catalyst::Plugin::Authentication)
BuildRequires:  perl(Catalyst::Plugin::Session)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Catalyst::Plugin::Session::Store::File)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(Catalyst::View::TT)
BuildRequires:  perl(CatalystX::Component::Traits)
BuildRequires:  perl(CatalystX::InjectComponent)
BuildRequires:  perl(Crypt::DH)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class::Optional::Dependencies)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTML::FormHandler)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON::Any)
BuildRequires:  perl(Module::Install::AuthorRequires)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::MethodAttributes)
BuildRequires:  perl(MooseX::RelatedClassRoles)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Common)
BuildRequires:  perl(MooseX::Types::JSON)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(SQL::Translator)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl-generators
# /oreon:deps
%description
CatalystX::SimpleLogin is an application class which provides a simple login
and logout page with the addition of only one line of code and one template to
your application.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CatalystX-SimpleLogin-%{version}
# Remove bundled libs
rm -rf inc/*

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
