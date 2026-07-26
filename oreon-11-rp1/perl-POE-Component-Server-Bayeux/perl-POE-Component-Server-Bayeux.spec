%global source0_hash 2a421aed7509f9885830bff3ce4c2e6ea0325ea607baa819722b5a6c7b2e4793

Name:           perl-POE-Component-Server-Bayeux
Version:        0.04
Release:        44%{?dist}
Summary:        Bayeux/cometd server implementation in POE
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-Server-Bayeux
Source0:        https://cpan.metacpan.org/authors/id/E/EW/EWATERS/POE-Component-Server-Bayeux-%{version}.tar.gz
Patch1:         POE-Component-Server-Bayeux-0.04-switch.patch
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(CGI::Simple)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(JSON::Any)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(LWP)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(POE::Component::Client::HTTP)
BuildRequires:  perl(POE::Component::Server::HTTP) >= 0.09
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
# missed by the autoreq for various reasons
Requires:       perl(Class::Accessor)
Requires:       perl(JSON::XS)
Requires:       perl(POE::Component::Client::HTTP)
Requires:       perl(LWP)

%description
This module implements the Bayeux Protocol (1.0draft1) from the Dojo
Foundation. Also called cometd, Bayeux is a low-latency routing protocol
for JSON encoded events between clients and servers in a publish-
subscribe model.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POE-Component-Server-Bayeux-%{version}
%patch -P1 -p1 -b .switch

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README htdocs
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
