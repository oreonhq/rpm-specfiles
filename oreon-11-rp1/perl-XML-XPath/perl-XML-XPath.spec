# Run optional tests
%if ! (0%{?rhel})
%bcond_without perl_XML_XPath_enables_load_test
%bcond_without perl_XML_XPath_enables_optional_test
%else
%bcond_with perl_XML_XPath_enables_load_test
%bcond_with perl_XML_XPath_enables_optional_test
%endif

Name:           perl-XML-XPath
Version:        1.48
Release:        11%{?dist}
Summary:        XPath parser and evaluator for Perl
# XML/XPath.pm, XML/XPath/PerlSAX.pm, REAME: GPL-1.0-or-later OR Artistic-1.0-Perl
# Others: Artistic-2.0
License:        Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/XML-XPath
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/XML-XPath-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(XML::Parser) >= 2.23
# Tests
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
%if %{with perl_XML_XPath_enables_load_test}
BuildRequires:  perl(Path::Tiny) >= 0.076
%endif
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
# Optional tests
%if %{with perl_XML_XPath_enables_optional_test}
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::LeakTrace)
%endif

Requires:       perl(POSIX)
Requires:       perl(XML::Parser) >= 2.23

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(XML::Parser\\)$

%if %{without perl_XML_XPath_enables_optional_test}
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::LeakTrace\\)
%endif

# perl-generators does not work properly for
#   "use parent qw/-norequire XML::XPath::Node/;"
%global __requires_exclude %{__requires_exclude}|^perl\\(-norequire\\)

%description
This module aims to comply exactly to the XPath specification at
http://www.w3.org/TR/xpath and yet allow extensions to be added in the
form of functions. Modules such as XSLT and XPointer may need to do
this as they support functionality beyond XPath.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n XML-XPath-%{version}

%if %{without perl_XML_XPath_enables_load_test}
rm -f t/00load.t
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
cat >> $RPM_BUILD_ROOT/%{_mandir}/man1/xpath.1 << EOF
.so man3/XML::XPath.3pm
EOF

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a examples t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_XML_XPath_enables_load_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/00load.t
%endif
rm %{buildroot}%{_libexecdir}/%{name}/t/manifest.t
rm %{buildroot}%{_libexecdir}/%{name}/t/meta-*.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README TODO
%{_bindir}/xpath
%{perl_vendorlib}/XML
%{_mandir}/man1/xpath*
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.48-11
- Prepare for Oreon 11 (RP1)
