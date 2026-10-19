%global source0_hash 9c84a51be4cdb47bf88766ecab051fe092016472969e39f4acdba009885faabe
%bcond_with perl_XML_XPath_enables_load_test
%bcond_with perl_XML_XPath_enables_optional_test
Name:           perl-XML-XPath
Version:        1.49
Release:        1%{?dist}
Summary:        XPath parser and evaluator for Perl
License:        Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/XML-XPath
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/XML-XPath-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_XML_XPath_enables_load_test}
%endif
%if %{with perl_XML_XPath_enables_optional_test}
%endif
Requires:       perl(POSIX)
Requires:       perl(XML::Parser) >= 2.23
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(XML::Parser\\)$
%if %{without perl_XML_XPath_enables_optional_test}
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::LeakTrace\\)
%endif
%global __requires_exclude %{__requires_exclude}|^perl\\(-norequire\\)
Provides:       perl(XML::XPath)
Provides:       perl(XML::XPath::XMLParser)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a examples t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_XML_XPath_enables_load_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/00load.t
%endif
rm %{buildroot}%{_libexecdir}/%{name}/t/manifest.t
rm %{buildroot}%{_libexecdir}/%{name}/t/meta-*.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-XML-XPath-tests -f %{oreon_filedir}/perl-XML-XPath-tests.list

%changelog

%autochangelog
