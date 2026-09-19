%global source0_hash 65c7e58b7ccd9e14d12589741763001b2122715f9cd8e29e013cfa9c7cd75e0e

Name:           perl-HTTP-OAI
Version:        4.13
Release:        8%{?dist}
Summary:        API for OAI-PMH
License:        BSD-3-Clause
URL:            https://metacpan.org/release/HTTP-OAI
Source0:        https://cpan.metacpan.org/authors/id/H/HO/HOCHSTEN/HTTP-OAI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
# CGI not used, bin/oai_static_gateway.pl is never executed
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode) >= 2.12
BuildRequires:  perl(Exporter)
# Getopt::Long not used at tests
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(LWP::MemberMixin)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(overload)
# Pod::Usage not uset at tests
BuildRequires:  perl(POSIX)
# Term::ReadKey not used at tests
# Term::ReadLine not used at tests
BuildRequires:  perl(URI)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::LibXML) >= 1.60
BuildRequires:  perl(XML::LibXML::SAX)
BuildRequires:  perl(XML::LibXML::SAX::Builder)
BuildRequires:  perl(XML::LibXML::SAX::Parser)
BuildRequires:  perl(XML::LibXML::XPathContext)
BuildRequires:  perl(XML::NamespaceSupport)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::Base) >= 1.04
BuildRequires:  perl(XML::SAX::ParserFactory)
BuildRequires:  perl(XML::SAX::Writer)
# Tests:
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More) >= 0.99
Requires:       perl(Encode) >= 2.12
Requires:       perl(Term::ReadLine)
Requires:       perl(Term::ReadKey)
Requires:       perl(XML::LibXML) >= 1.60
Requires:       perl(XML::SAX::Base) >= 1.04

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Encode|Test::More|XML::LibXML|XML::SAX::Base)\\)$
# Hide prive modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(XML::SAX::Debug\\)

%description
These are Perl modules and tools implementing Open Archives Initiative
Protocol for Metadata Harvesting (OAI-PMH).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.99
Requires:       perl(XML::LibXML) >= 1.60
Requires:       perl(XML::SAX)
Requires:       perl(XML::SAX::Base) >= 1.04
Requires:       perl(XML::SAX::ParserFactory)
Requires:       perl(XML::SAX::Writer)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n HTTP-OAI-%{version}
# Remove always skipped author tests
rm t/author-pod-syntax.t
perl -i -ne 'print $_ unless m{^t/author-pod-syntax.t}' MANIFEST
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a examples t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset HTTP_OAI_AGENT HTTP_OAI_NETTESTS HTTP_OAI_SAX_TRACE HTTP_OAI_TRACE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc bin/oai_static_gateway.pl Changes README
%{_bindir}/oai_browser.pl
%{_bindir}/oai_pmh.pl
%dir %{perl_vendorlib}/HTTP
%{perl_vendorlib}/HTTP/OAI
%{perl_vendorlib}/HTTP/OAI.pm
%{_mandir}/man1/oai_browser.pl.*
%{_mandir}/man1/oai_pmh.pl.*
%{_mandir}/man3/HTTP::OAI.*
%{_mandir}/man3/HTTP::OAI::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
