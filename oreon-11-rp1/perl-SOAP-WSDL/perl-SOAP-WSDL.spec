%global source0_hash e2cc1e42eace8dbb384e509d04644191afcdd8df0fec144376cebafad3f15744
Summary:        Perl module for SOAP with WSDL support
Name:          perl-SOAP-WSDL
Version:       3.004
Release:        21%{?dist}
License:       GPL-1.0-or-later OR Artistic-1.0-Perl
URL:           https://metacpan.org/release/SOAP-WSDL
Source0:        https://cpan.metacpan.org/modules/by-module/SOAP/SOAP-WSDL-%{version}.tar.gz
Patch0:        %{name}-use-Test-XML.patch
BuildArch:     noarch
Requires:      perl(SOAP::Lite)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  git
BuildRequires:  make
BuildRequires:  perl(APR::Table)
BuildRequires:  perl(Apache2::Const)
BuildRequires:  perl(Apache2::Log)
BuildRequires:  perl(Apache2::RequestIO)
BuildRequires:  perl(Apache2::RequestRec)
BuildRequires:  perl(Apache2::RequestUtil)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Class::Std::Fast)
BuildRequires:  perl(Class::Std::Fast::Storable)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Plugin::CGI)
BuildRequires:  perl(Test::MockObject)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::Parser::Expat)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
SOAP::WSDL provides easy access to Web Services with WSDL descriptions.
The WSDL is parsed and stored in memory. Your data is serialized according
to the rules in the WSDL. The only transport mechanisms currently supported
are HTTP and HTTPS.

%package  Apache
Summary:  SOAP server with WSDL support for Apache2 web server
Requires: %{name} = %{version}-%{release}
%description Apache
The SOAP::WSDL-server package contains a SOAP compliant server capable of
sending messages via the Apache2 web server.

%package  examples
Summary:  Examples for the Perl SOAP::WSDL module
Requires: %{name} = %{version}-%{release}
%description examples
The package contains examples for SOAP::WSDL module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n SOAP-WSDL-%{version}
# fix example's permission
chmod a-x example/cgi-bin/*.pl

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_build pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
chmod 0755 %{buildroot}%{_bindir}/wsdl2perl.pl
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build test
%files -f %{oreon_filedir}/main.list
%files -n perl-SOAP-WSDL-Apache -f %{oreon_filedir}/perl-SOAP-WSDL-Apache.list
%files -n perl-SOAP-WSDL-examples -f %{oreon_filedir}/perl-SOAP-WSDL-examples.list

%changelog

%autochangelog
