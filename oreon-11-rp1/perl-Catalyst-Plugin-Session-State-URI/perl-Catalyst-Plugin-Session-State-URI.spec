%global source0_hash f63339b77bfb3be2c5f96f4d45b23b5988058f2c052ec9bcb513e26189298b10

Name:           perl-Catalyst-Plugin-Session-State-URI
Version:        0.15
Release:        46%{?dist}
Summary:        Saves session IDs by rewriting URIs delivered to the client
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Plugin-Session-State-URI
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Session-State-URI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Plugin::Session) >= 0.27
BuildRequires:  perl(Catalyst::Plugin::Session::State)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie) >= 0.03
BuildRequires:  perl(Catalyst::Request)
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::TokeParser::Simple)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::MockObject::Extends) >= 1.01
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Find)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(warnings)
BuildRequires:  sed
Requires:       perl(Catalyst::Plugin::Session::State)
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast)

%description
Catalyst::Plugin::Session::State::URI - Saves session IDs by rewriting URIs
delivered to the client, and extracting the session ID from requested URIs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Plugin-Session-State-URI-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
TEST_POD=1 make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
