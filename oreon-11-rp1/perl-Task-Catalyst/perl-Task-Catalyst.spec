%global source0_hash 9acd7b65fe09c4874aa72145ad341e66f0cac49c656e1a62f18206c615d9706d

Name:       perl-Task-Catalyst 
Version:    4.02
Release:    40%{?dist}
# lib/Task/Catalyst.pm -> GPL-1.0-or-later OR Artistic-1.0-Perl
License:    GPL-1.0-or-later OR Artistic-1.0-Perl

Summary:    All you need to start with Catalyst 
Source0:    https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Task-Catalyst-%{version}.tar.gz
URL:        https://metacpan.org/release/Task-Catalyst
BuildArch:  noarch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) => 6.42
# tests for Task::Catalyst itself
BuildRequires: perl(Test::More)
# tests for release-testing
BuildRequires: perl(Pod::Coverage::TrustPod)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)

# This macro allows us to easily define identical Requires and BR
%global req_both() %{expand:\
Requires: %*\
BuildRequires: %*\
} 

# Core Modules
%req_both perl(Catalyst) >= 5.80000
%req_both perl(Catalyst::Devel) >= 1.26
%req_both perl(Catalyst::Manual) >= 5.8000
# Recommended Models
%req_both perl(Catalyst::Model::Adaptor)
%req_both perl(Catalyst::Model::DBIC::Schema)
# Recommended Views
%req_both perl(Catalyst::View::TT)
%req_both perl(Catalyst::View::Email)
# Recommended Components
%req_both perl(Catalyst::Controller::ActionRole)
%req_both perl(CatalystX::Component::Traits)
%req_both perl(CatalystX::SimpleLogin)
%req_both perl(Catalyst::Action::REST)
%req_both perl(Catalyst::Component::InstancePerContext)
# Session Support
%req_both perl(Catalyst::Plugin::Session)
%req_both perl(Catalyst::Plugin::Session::State::Cookie)
%req_both perl(Catalyst::Plugin::Session::Store::File)
%req_both perl(Catalyst::Plugin::Session::Store::DBIC)
# Authentication and Authorization
%req_both perl(Catalyst::Plugin::Authentication)
%req_both perl(Catalyst::Authentication::Store::DBIx::Class)
%req_both perl(Catalyst::Authentication::Credential::HTTP)
%req_both perl(Catalyst::ActionRole::ACL)
# Recommended Plugins
%req_both perl(Catalyst::Plugin::Static::Simple)
%req_both perl(Catalyst::Plugin::Unicode::Encoding)
%req_both perl(Catalyst::Plugin::I18N)
%req_both perl(Catalyst::Plugin::ConfigLoader)
# Testing, Debugging and Profiling
%req_both perl(Test::WWW::Mechanize::Catalyst)
%req_both perl(Catalyst::Plugin::StackTrace)
%req_both perl(CatalystX::REPL)
%req_both perl(CatalystX::LeakChecker)
%req_both perl(CatalystX::Profile)
# Deployment
%req_both perl(FCGI)
%req_both perl(FCGI::ProcManager)
%req_both perl(Starman)
%req_both perl(local::lib)

# Make sure we pull it in, regardless of where it is
Requires:   %{_bindir}/catalyst.pl

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

%check
RELEASE_TESTING=1 TEST_POD=1 make test

%files
%doc Changes README 
%{perl_vendorlib}/Task*
%{_mandir}/man3/Task*.3*

%changelog
%autochangelog
