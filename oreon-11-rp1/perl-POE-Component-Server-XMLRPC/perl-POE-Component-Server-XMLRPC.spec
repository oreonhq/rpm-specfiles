%global source0_hash 2b550938546c1dd02f96aac726b9966f61e6166bbcf22dad08f490c0ba01bbf8
Name:           perl-POE-Component-Server-XMLRPC
Version:        0.05
Release:        1%{?dist}
Summary:        Publish POE event handlers via XMLRPC over HTTP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Server-XMLRPC
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAHEX/POE-Component-Server-XMLRPC-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(POE) >= 0.22
Requires:       perl(POE::Component::Server::HTTP) >= 0.02
Requires:       perl(XMLRPC::Lite) >= 0.28
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(POE\\)$
%global __requires_exclude %__requires_exclude|^perl\\(POE::Component::Server::HTTP\\)$
%global __requires_exclude %__requires_exclude|^perl\\(XMLRPC::Lite\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POE)
BuildRequires:  perl(POE::Component::Server::HTTP)
BuildRequires:  perl(Test)
BuildRequires:  perl(XMLRPC::Lite)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
