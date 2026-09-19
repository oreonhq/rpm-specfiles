%global source0_hash 8f0df8fb80e126bb967e829fb054f8739408d7c7fa558f6d6fa555618b3bedc1

Name:           perl-Catalyst-Model-XMLRPC
Version:        0.04
Release:        50%{?dist}
Summary:        XMLRPC model class for Catalyst
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Catalyst-Model-XMLRPC
Source0:        https://cpan.metacpan.org/authors/id/F/FM/FMERGES/Catalyst-Model-XMLRPC-%{version}.tar.gz
BuildArch:      noarch

Patch0:         config.patch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Devel)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(RPC::XML)
BuildRequires:  perl(Test::More)
# optional tests
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

# not automagically picked up...
Requires:       perl(Catalyst::Model)

%?perl_default_filter

%description
This model class uses RPC::XML::Client to invoke remote procedure calls
using XML-RPC.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Model-XMLRPC-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
# network tests will fail in the buildsys.
%{?_with_network_tests: XMLRPC_TEST_LIVE=1} TEST_POD=1 make test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
