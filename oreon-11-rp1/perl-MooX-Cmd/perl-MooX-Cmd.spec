%global source0_hash 943ff28daa80897327c7c5fec5a7100cfaac92daf0f9f97c38e3a77d00ae70f5

Name:           perl-MooX-Cmd
Version:        0.017
Release:        30%{?dist}
Summary:        Giving an easy Moo style way to make command organized CLI apps
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-Cmd
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/MooX-Cmd-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::MoreUtils) >= 0.406
BuildRequires:  perl(Module::Pluggable::Object) >= 4.8
BuildRequires:  perl(Module::Runtime)
# 0.009013 from Moo in META which is not used
BuildRequires:  perl(Moo::Role) >= 0.009013
BuildRequires:  perl(Package::Stash) >= 0.33
BuildRequires:  perl(Params::Util) >= 0.37
BuildRequires:  perl(parent)
BuildRequires:  perl(Regexp::Common) >= 2011121001
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Text::ParseWords)
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moo) >= 0.009013
# Optional tests:
%if !%{defined perl_bootstrap}
# Break build-cycle: perl-MooX-ConfigFromFile → perl-MooX-Cmd
# → perl-MooX-ConfigFromFile
BuildRequires:  perl(MooX::ConfigFromFile) >= 0.008
# Break build-cycle: perl-MooX-Options → perl-MooX-Cmd → perl-MooX-Options
BuildRequires:  perl(MooX::Options) >= 4.103
%endif
BuildRequires:  perl(Text::Abbrev)
Requires:       perl(List::MoreUtils) >= 0.406
Requires:       perl(Module::Pluggable::Object) >= 4.8
# 0.009013 from Moo in META which is not used
Requires:       perl(Moo::Role) >= 0.009013
Requires:       perl(Package::Stash) >= 0.33
Requires:       perl(Params::Util) >= 0.37
Requires:       perl(Regexp::Common) >= 2011121001
Requires:       perl(Test::More) >= 0.98

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(List::MoreUtils\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Pluggable::Object\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo::Role\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Package::Stash\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Util\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Regexp::Common\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::More\\)$

%description
Works together with MooX::Options for every command on its own, so options
are parsed for the specific context and used for the instantiation:

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooX-Cmd-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
