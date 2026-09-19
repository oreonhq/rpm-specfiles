%global source0_hash 2b550938546c1dd02f96aac726b9966f61e6166bbcf22dad08f490c0ba01bbf8

Name:           perl-POE-Component-Server-XMLRPC
Version:        0.05
Release:        52%{?dist}
Summary:        Publish POE event handlers via XMLRPC over HTTP
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Server-XMLRPC
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAHEX/POE-Component-Server-XMLRPC-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(POE) >= 0.22
BuildRequires:  perl(POE::Component::Server::HTTP) >= 0.02
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XMLRPC::Lite) >= 0.28
# Tests only
BuildRequires:  perl(Test)
Requires:       perl(POE) >= 0.22
Requires:       perl(POE::Component::Server::HTTP) >= 0.02
Requires:       perl(XMLRPC::Lite) >= 0.28

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(POE\\)$
%global __requires_exclude %__requires_exclude|^perl\\(POE::Component::Server::HTTP\\)$
%global __requires_exclude %__requires_exclude|^perl\\(XMLRPC::Lite\\)$

%description
POE::Component::Server::XMLRPC is a bolt-on component that can publish a
event handlers via XMLRPC over HTTP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Server-XMLRPC-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
# CHANGES file is empty
%doc README examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
