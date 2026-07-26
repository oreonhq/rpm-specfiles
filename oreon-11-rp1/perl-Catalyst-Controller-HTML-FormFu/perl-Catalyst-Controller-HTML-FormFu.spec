%global source0_hash f13fb9b3b3b00b35f06abc31614461c8d7346fbe07fb569c71e8d586e5eb5ddc

Name:           perl-Catalyst-Controller-HTML-FormFu
Version:        2.04
Release:        24%{?dist}
Summary:        HTML::FormFu controller for Catalyst
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Catalyst-Controller-HTML-FormFu
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NIGELM/Catalyst-Controller-HTML-FormFu-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst::Action)
BuildRequires:  perl(Catalyst::Component::InstancePerContext)
BuildRequires:  perl(Catalyst::Controller)
# This is a plug-in for Catalyst::Runtime
BuildRequires:  perl(Catalyst::Runtime) >= 5.71001
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::FormFu) >= 2.06
BuildRequires:  perl(HTML::FormFu::Deploy)
BuildRequires:  perl(HTML::FormFu::MultiForm)
BuildRequires:  perl(HTML::FormFu::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Attribute::Chained) >= 1.0.1
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Regexp::Assemble)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
# Task::Weaken for Scalar::Util, see Makefile.PL
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Action::RenderView)
BuildRequires:  perl(Catalyst::Plugin::ConfigLoader) >= 0.23
BuildRequires:  perl(Catalyst::Plugin::Session)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:  perl(Catalyst::Plugin::Session::Store::File)
BuildRequires:  perl(Catalyst::View::TT)
# Config::General not used
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
# Template not used
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst)
# Test::WWW::Mechanize 1.16 for post_ok()
BuildRequires:  perl(Test::WWW::Mechanize) >= 1.16
Requires:       perl(Catalyst::Component::InstancePerContext)
Requires:       perl(Catalyst::Controller)
Requires:       perl(Catalyst::Runtime) >= 5.71001
Requires:       perl(HTML::FormFu) >= 2.06
Requires:       perl(MooseX::Attribute::Chained) >= 1.0.1
# Task::Weaken for Scalar::Util, see Makefile.PL
Requires:       perl(Task::Weaken)

%description
This base controller merges the functionality of HTML::FormFu with Catalyst.

# Filter unde-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((HTML::FormFu|MooseX::Attribute::Chained)\\)$

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Controller-HTML-FormFu-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
