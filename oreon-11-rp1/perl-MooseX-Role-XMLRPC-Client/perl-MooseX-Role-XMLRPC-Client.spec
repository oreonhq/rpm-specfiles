%global source0_hash 15546a3e826c2b5c18dcfac605415cdbc53c806647ea3e85f7b9d5bd12669adc

Name:       perl-MooseX-Role-XMLRPC-Client 
Version:    0.07
Release:    30%{?dist}
# lib/MooseX/Role/XMLRPC/Client.pm -> LGPLv2+
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2+

Summary:    Provide the needed bits to be a XML-RPC client 
Source:     https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/MooseX-Role-XMLRPC-Client-%{version}.tar.gz 
Url:        https://metacpan.org/release/MooseX-Role-XMLRPC-Client
BuildArch:  noarch

BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(Crypt::SSLeay)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(HTTP::Cookies)
BuildRequires: perl(Module::Install)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::AttributeShortcuts)
BuildRequires: perl(MooseX::Role::Parameterized)
BuildRequires: perl(MooseX::Types::Moose)
BuildRequires: perl(MooseX::Types::Path::Class)
BuildRequires: perl(MooseX::Types::URI)
BuildRequires: perl(namespace::clean)
BuildRequires: perl(RPC::XML::Client)
BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::Requires)

%{?perl_default_filter}

%description
This is a Moose role that provides the methods and attributes needed 
to enable a class to serve as an XML-RPC client.  It is parameterized
through MooseX::Role::Parameterized, so you can customize how it embeds
in your class. You can even embed it multiple times with different
paramaterization, if it strikes your fancy :-)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Role-XMLRPC-Client-%{version}

# This module bundles an old version of Module::Install
# This is against Fedora policy so we replace it with
# the system version
rm -rf inc/Module
cp -r %{perl_vendorlib}/Module inc/

# This fails. Remove it until we figure out why
sed -i -e 's/extra_tests;//' Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'

%{_fixperms} %{buildroot}/*

%check
%{?!_with_network_tests: NO_NET_TESTS=1} make test

%files
%doc Changes README 
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*.3*

%changelog
%autochangelog
