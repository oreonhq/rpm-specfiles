%global source0_hash 5279eb0d136c533ff897f6934c3aad6f20504b997fb2606e52c5dbbd92758e73

# Support for mod_perl
%bcond_without perl_RPC_XML_enables_mod_perl
# Run optional tests
%bcond_without perl_RPC_XML_enables_optional_test

%global cpan_name RPC-XML

Name:       perl-%{cpan_name}
Version:    0.82
Release:    16%{?dist}
Summary:    Set of classes for core data, message and XML handling
# LGPL version and Artistic variant are clarified in README.license.
# etc/make_method:      Artistic-2.0 OR LGPL-2.1-only
# etc/rpc-method.dtd:   Artistic-2.0 OR LGPL-2.1-only
# lib/Apache/RPC/Server.pm: Artistic-2.0 OR LGPL-2.1-only
# lib/Apache/RPC/Status.pm: Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML.pm:   Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/Client.pm:    Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/Parser.pm:    Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/ParserFactory.pm: Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/Parser/XMLLibXML.pm:  Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/Parser/XMLParser.pm:  Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/Procedure.pm:     Artistic-2.0 OR LGPL-2.1-only
# lib/RPC/XML/Server.pm:    Artistic-2.0 OR LGPL-2.1-only
License:    Artistic-2.0 OR LGPL-2.1-only
URL:        https://metacpan.org/release/%{cpan_name}
Source0:    https://cpan.metacpan.org/authors/id/R/RJ/RJRAY/%{cpan_name}-%{version}.tar.gz
Source1:    README.license
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.56
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time without Apache stuff:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Daemon) >= 6.12
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Load) >= 0.36
# Keep Net::Server::MultiType optional, HTTP::Daemon is preferred
BuildRequires:  perl(Scalar::Util) >= 1.55
BuildRequires:  perl(subs)
BuildRequires:  perl(URI)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::LibXML) >= 1.85
BuildRequires:  perl(XML::Parser) >= 2.46
%if %{with perl_RPC_XML_enables_mod_perl}
# Run-time for Apache stuff:
BuildRequires:  perl(Apache)
BuildRequires:  perl(Apache::Constants)
BuildRequires:  perl(Apache::File)
BuildRequires:  perl(CGI)
# Socket not used at tests
%endif
# Recommended run-time:
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(DateTime) >= 1.54
BuildRequires:  perl(DateTime::Format::ISO8601) >= 0.15
# Tests:
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP) >= 6.51
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More) >= 1.302183
%if %{with perl_RPC_XML_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Net::Server)
%endif
Recommends:     perl(Compress::Zlib)
Requires:       perl(HTTP::Daemon) >= 6.12
Requires:       perl(MIME::Base64)
Requires:       perl(Module::Load) >= 0.36
Requires:       perl(Scalar::Util) >= 1.55
Requires:       perl(XML::Parser) >= 2.46
Requires:       perl(DateTime) >= 1.54
Requires:       perl(DateTime::Format::ISO8601) >= 0.15
Requires:       perl(XML::LibXML) >= 1.85

%{?perl_default_filter}
# Remove underspecified symbols
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((LWP|Module::Load|Scalar::Util|Test::More|XML::LibXML|XML::Parser)\\)\\s*$
# Hide private modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(BadParserClass\\)

%description
The RPC::XML package is an implementation of XML-RPC. The module provides
classes for sample client and server implementations, a server designed as an
Apache location-handler, and a suite of data-manipulation classes that are
used by them.

%if %{with perl_RPC_XML_enables_mod_perl}
%package -n perl-Apache-RPC
Summary:    Companion packages for RPC::XML tuned for mod_perl environments

%description -n perl-Apache-RPC
This package contains Apache::RPC::Server and Apache::RPC::Status, useful for
running RPC::XML under mod_perl.
%endif

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       coreutils
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with perl_RPC_XML_enables_mod_perl}
Requires:       perl-Apache-RPC = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires:       perl-Test-Harness
Requires:       perl(LWP) >= 6.51
Requires:       perl(Module::Load) >= 0.36
Requires:       perl(Test::More) >= 1.302183
%if %{with perl_RPC_XML_enables_optional_test}
Requires:       perl(Net::Server)
%endif
Requires:       perl(Scalar::Util) >= 1.55
Requires:       perl(XML::LibXML) >= 1.85

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{cpan_name}-%{version}
cp -p %{SOURCE1} .
%if !%{with perl_RPC_XML_enables_mod_perl}
rm -rf lib/Apache
perl -i -ln -e 'print unless qr{^lib/Apache/}' MANIFEST
%endif
# Normalize shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Tests, e.g. t/11_base64_fh.t write into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license README.license
%doc ChangeLog* README etc/*.dtd ex/ methods/
%{_mandir}/man3/RPC::XML.*
%{_mandir}/man3/RPC::XML::*
%{_mandir}/man1/make_method.*
%{_bindir}/make_method
%dir %{perl_vendorlib}/RPC
%{perl_vendorlib}/RPC/XML
%{perl_vendorlib}/RPC/XML.pm

%if %{with perl_RPC_XML_enables_mod_perl}
%files -n perl-Apache-RPC
%license README.license
%doc README.apache2
%{_mandir}/man3/Apache::RPC::*
%dir %{perl_vendorlib}/Apache
%{perl_vendorlib}/Apache/RPC
%endif

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
