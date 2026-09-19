%global source0_hash 6ccf97c824c7737572f535fd4a590bd3fe9ea5e12eaa6beffbef4b179b11b89d

Name:           perl-CatalystX-SimpleLogin
Version:        0.21
Release:        16%{?dist}
Summary:        Provide a simple Login controller which can be reused
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CatalystX-SimpleLogin
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABRAXXA/CatalystX-SimpleLogin-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst::Action::RenderView)
BuildRequires:  perl(Catalyst::Action::REST) >= 0.74
BuildRequires:  perl(Catalyst::ActionRole::ACL)
# not available in fedora and upstream is currently broken
# see https://rt.cpan.org/Public/Bug/Display.html?id=70417
# BuildRequires:  perl(Catalyst::Authentication::Credential::OpenID)
BuildRequires:  perl(Catalyst::Authentication::Store::DBIx::Class)
BuildRequires:  perl(Catalyst::Model::DBIC::Schema)
BuildRequires:  perl(Catalyst::Plugin::Authentication)
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.27
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Catalyst::Plugin::Session::Store::File)
BuildRequires:  perl(Catalyst::Runtime) >= 5.80013
BuildRequires:  perl(Catalyst::View::TT)
BuildRequires:  perl(CatalystX::Component::Traits) >= 0.13
BuildRequires:  perl(CatalystX::InjectComponent)
BuildRequires:  perl(Crypt::DH)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class::Optional::Dependencies)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTML::FormHandler) >= 0.28001
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON::Any) >= 1.22
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::AuthorRequires)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::MethodAttributes) >= 0.18
BuildRequires:  perl(MooseX::RelatedClassRoles) >= 0.004
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Common)
BuildRequires:  perl(MooseX::Types::JSON) >= 0.02
BuildRequires:  perl(MooseX::Types::Path::Class) >= 0.05
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(SQL::Translator)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(inc::Module::Install)
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

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
