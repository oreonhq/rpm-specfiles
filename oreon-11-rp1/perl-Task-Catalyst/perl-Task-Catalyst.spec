%global source0_hash 9acd7b65fe09c4874aa72145ad341e66f0cac49c656e1a62f18206c615d9706d
Name:       perl-Task-Catalyst 
Version:    4.02
Release:        1%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        All you need to start with Catalyst
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Task-Catalyst-%{version}.tar.gz
URL:        https://metacpan.org/release/Task-Catalyst
BuildArch:  noarch
ExcludeArch:    %{ix86}
%global req_both() %{expand:\
Requires: %*\
} 
%req_both perl(Catalyst) >= 5.80000
%req_both perl(Catalyst::Devel) >= 1.26
%req_both perl(Catalyst::Manual) >= 5.8000
%req_both perl(Catalyst::Model::Adaptor)
%req_both perl(Catalyst::Model::DBIC::Schema)
%req_both perl(Catalyst::View::TT)
%req_both perl(Catalyst::View::Email)
%req_both perl(Catalyst::Controller::ActionRole)
%req_both perl(CatalystX::Component::Traits)
%req_both perl(CatalystX::SimpleLogin)
%req_both perl(Catalyst::Action::REST)
%req_both perl(Catalyst::Component::InstancePerContext)
%req_both perl(Catalyst::Plugin::Session)
%req_both perl(Catalyst::Plugin::Session::State::Cookie)
%req_both perl(Catalyst::Plugin::Session::Store::File)
%req_both perl(Catalyst::Plugin::Session::Store::DBIC)
%req_both perl(Catalyst::Plugin::Authentication)
%req_both perl(Catalyst::Authentication::Store::DBIx::Class)
%req_both perl(Catalyst::Authentication::Credential::HTTP)
%req_both perl(Catalyst::ActionRole::ACL)
%req_both perl(Catalyst::Plugin::Static::Simple)
%req_both perl(Catalyst::Plugin::Unicode::Encoding)
%req_both perl(Catalyst::Plugin::I18N)
%req_both perl(Catalyst::Plugin::ConfigLoader)
%req_both perl(Test::WWW::Mechanize::Catalyst)
%req_both perl(Catalyst::Plugin::StackTrace)
%req_both perl(CatalystX::REPL)
%req_both perl(CatalystX::LeakChecker)
%req_both perl(CatalystX::Profile)
%req_both perl(FCGI)
%req_both perl(FCGI::ProcManager)
%req_both perl(Starman)
%req_both perl(local::lib)
Requires:   %{_bindir}/catalyst.pl
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Action::REST)
BuildRequires:  perl(Catalyst::ActionRole::ACL)
BuildRequires:  perl(Catalyst::Authentication::Credential::HTTP)
BuildRequires:  perl(Catalyst::Authentication::Store::DBIx::Class)
BuildRequires:  perl(Catalyst::Component::InstancePerContext)
BuildRequires:  perl(Catalyst::Controller::ActionRole)
BuildRequires:  perl(Catalyst::Devel)
BuildRequires:  perl(Catalyst::Manual)
BuildRequires:  perl(Catalyst::Model::Adaptor)
BuildRequires:  perl(Catalyst::Model::DBIC::Schema)
BuildRequires:  perl(Catalyst::Plugin::Authentication)
BuildRequires:  perl(Catalyst::Plugin::ConfigLoader)
BuildRequires:  perl(Catalyst::Plugin::I18N)
BuildRequires:  perl(Catalyst::Plugin::Session)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Catalyst::Plugin::Session::Store::DBIC)
BuildRequires:  perl(Catalyst::Plugin::Session::Store::File)
BuildRequires:  perl(Catalyst::Plugin::StackTrace)
BuildRequires:  perl(Catalyst::Plugin::Static::Simple)
BuildRequires:  perl(Catalyst::Plugin::Unicode::Encoding)
BuildRequires:  perl(Catalyst::View::Email)
BuildRequires:  perl(Catalyst::View::TT)
BuildRequires:  perl(CatalystX::Component::Traits)
BuildRequires:  perl(CatalystX::LeakChecker)
BuildRequires:  perl(CatalystX::Profile)
BuildRequires:  perl(CatalystX::REPL)
BuildRequires:  perl(CatalystX::SimpleLogin)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FCGI)
BuildRequires:  perl(FCGI::ProcManager)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Starman)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(local::lib)
BuildRequires:  perl-generators
# /oreon:deps
%description
This package ensures everything you need to write serious Catalyst
applications is installed.  Install this if you're interested in 
developing Catalyst apps. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Task-Catalyst-%{version}

%build

PERL_AUTOINSTALL='--skipdeps' %{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

RELEASE_TESTING=1 TEST_POD=1 make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
