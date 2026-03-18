# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_XML_Twig_enables_optional_test
%else
%bcond_with perl_XML_Twig_enables_optional_test
%endif

Name:           perl-XML-Twig
Version:        3.54
Release:        3%{?dist}
Summary:        Perl module for processing huge XML documents in tree mode
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Twig
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIROD/XML-Twig-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  expat >= 2.0.1
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
# Keep HTML::Entities::Numbered optional
# Keep HTML::Tidy optional
BuildRequires:  perl(HTML::TreeBuilder) >= 4.00
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Parser) >= 2.23
# Prefer XML::XPathEngine over XML::XPath
BuildRequires:  perl(XML::XPathEngine)
# Tests:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests:
%if %{with perl_XML_Twig_enables_optional_test}
BuildRequires:  perl(IO::String)
BuildRequires:  perl(LWP)
BuildRequires:  perl(HTML::Entities)
%if !( 0%{?rhel} >= 7 )
BuildRequires:  perl(Test::CPAN::Meta::JSON)
%endif
BuildRequires:  perl(Text::Iconv)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Unicode::Map8)
BuildRequires:  perl(Unicode::String)
BuildRequires:  perl(utf8)
BuildRequires:  perl(XML::Filter::BufferText)
BuildRequires:  perl(XML::Handler::YAWriter)
BuildRequires:  perl(XML::SAX::Writer) >= 0.39
BuildRequires:  perl(XML::Simple)
%endif
Requires:       perl(Encode)
Requires:       perl(HTML::TreeBuilder) >= 4.00
Requires:       perl(IO::Scalar)
Requires:       perl(Scalar::Util)
Requires:       perl(Text::Wrap)
Requires:       perl(XML::Parser) >= 2.23

%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(XML::XPathEngine::NodeSet\\)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(xml_split::state\\)
# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XML::Parser\\)$

# Filter modules bundled for tests
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(tools\\)

%description
This module provides a way to process XML documents. It is build on
top of XML::Parser.  XML::Twig offers a tree interface to the
document, while allowing you to output the parts of it that have been
completely processed.  It allows minimal resource (CPU and memory)
usage by building the tree only for the parts of the documents that
need actual processing, through the use of the twig_roots and
twig_print_outside_roots options.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(XML::XPathEngine)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n XML-Twig-%{version}
iconv -f iso88591 -t utf8 < Changes > Changes.utf8 && \
    mv -f Changes.utf8 Changes

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL -y INSTALLDIRS=perl NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod*
mkdir -p %{buildroot}%{_libexecdir}/%{name}/tools
for F in `ls tools`; do
    mkdir -p %{buildroot}%{_libexecdir}/%{name}/tools/$F
    ln -s %{_bindir}/$F %{buildroot}%{_libexecdir}/%{name}/tools/$F
done
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
unset TEST_AUTHOR
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README 
%dir %{perl_privlib}/XML
%{perl_privlib}/XML/Twig*
%exclude %{perl_privlib}/XML/speedup*
%{_bindir}/xml_*
%{_mandir}/man1/xml_*
%{_mandir}/man3/XML::Twig*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.54-3
- Prepare for Oreon 11 (RP1)
