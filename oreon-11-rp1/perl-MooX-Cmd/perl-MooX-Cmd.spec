%global source0_hash 943ff28daa80897327c7c5fec5a7100cfaac92daf0f9f97c38e3a77d00ae70f5
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           perl-MooX-Cmd
Version:        0.017
Release:        1%{?dist}
Summary:        Giving an easy Moo style way to make command organized CLI apps
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-Cmd
Source0:        https://cpan.metacpan.org/authors/id/G/GE/GETTY/MooX-Cmd-%{version}.tar.gz
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%endif
Requires:       perl(List::MoreUtils) >= 0.406
Requires:       perl(Module::Pluggable::Object) >= 4.8
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
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::ConfigFromFile)
BuildRequires:  perl(MooX::Options)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Abbrev)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
