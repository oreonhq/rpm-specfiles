%global source0_hash none

# Do not invoke thread tests by default because the thread support is broken,
# bug #1224731, CPAN RT#91800
%bcond_with thread_test

Name:           perl-XML-LibXML
# NOTE: also update perl-XML-LibXSLT to a compatible version, see
# https://bugzilla.redhat.com/show_bug.cgi?id=469480
# it might not be needed anymore
# this module is maintained, the other is not
Version:        2.0213
Release:        1%{?dist}
Epoch:          1
Summary:        Perl interface to the libxml2 library
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MIT
URL:            https://metacpan.org/release/XML-LibXML
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/XML-LibXML-%{version}.tar.gz
# Fix parsing ampersand entities in SAX interface, CPAN RT#131498,
# posted to the upstream.
Patch0:        XML-LibXML-2.0202-Parse-an-ampersand-entity-in-SAX-interface.patch
# To reduce dependencies replace Alien::Libxml2 with pkg-config
Patch1:        XML-LibXML-2.0212-Use-pkgconfig-instead-of-Alien-Libxml2.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(libxml-2.0)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(XML::NamespaceSupport)
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::DocumentLocator)
BuildRequires:  perl(XML::SAX::Exception)
BuildRequires:  perl(XSLoader)
# Tests
# t/12html.t exhibits ISO-8859-2 charset
BuildRequires:  glibc-gconv-extra
BuildRequires:  perl(Errno)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(locale)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::ParserFactory)
# Optional tests
# Optional Test::Differences has a fall-back
%if ! ( 0%{?rhel} ) || (0%{?oreon} >= 11)
BuildRequires:  perl(Test::LeakTrace)
%endif
%if %{with thread_test}
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
%endif
BuildRequires:  perl(URI::file)
BuildRequires:  perl(utf8)
# Author test - Test::CPAN::Changes
# Author test - Test::Pod
# Author test - Test::Kwalitee
# Author test - Test::TrailingSpace
Requires:       perl(Data::Dumper)
# Run-require "perl-interpreter" because a triggerin script needs it.
Requires:           perl-interpreter
Requires(preun):    perl-interpreter
# threads and threads::shared are optional
Provides:       perl-XML-LibXML-Common = %{version}
Obsoletes:      perl-XML-LibXML-Common <= 0.13

%{?perl_default_filter}
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Collector\\)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(Counter)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(Stacker)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(TestHelpers)\s*$
%if 0%{?rhel} || (0%{?oreon} >= 11)
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::LeakTrace)\s*$
%endif

%description
This module implements a Perl interface to the GNOME libxml2 library
which provides interfaces for parsing and manipulating XML files. This
module allows Perl programmers to make use of the highly capable
validating XML parser and the high performance DOM implementation.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
# t/12html.t exhibits ISO-8859-2 charset
Requires:       glibc-gconv-extra
Requires:       perl-Test-Harness
%if %{with thread_test}
Requires:       perl(threads)
Requires:       perl(threads::shared)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n XML-LibXML-%{version}
chmod -x *.c
for i in Changes; do
  /usr/bin/iconv -f iso8859-1 -t utf-8 $i > $i.conv && /bin/mv -f $i.conv $i
done
perl -i -pe 's/\r\n/\n/' t/91unique_key.t

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL SKIP_SAX_INSTALL=1 INSTALLDIRS=vendor \
     OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a example t test %{buildroot}%{_libexecdir}/%{name}
for F in example/*.pl t/cpan-changes.t t/11memory.t t/pod.t \
        t/pod-files-presence.t t/release-kwalitee.t t/style-trailing-space.t; do
    rm -f %{buildroot}%{_libexecdir}/%{name}/"$F"
done
perl -i -pe 's{example/(testrun.xml)}{/tmp/$1}' %{buildroot}%{_libexecdir}/%{name}/t/03doc.t
cat > %{buildroot}%{_libexecdir}/%{name}/tests << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING RELEASE_TESTING
cd %{_libexecdir}/%{name} && THREAD_TEST=0%{?with_thread_test:1} exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/tests


%check
unset AUTHOR_TESTING RELEASE_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
THREAD_TEST=0%{?with_thread_test:1} make test

%triggerin -- perl-XML-SAX
for p in XML::LibXML::SAX::Parser XML::LibXML::SAX ; do
  %{_bindir}/perl -MXML::SAX -e "XML::SAX->add_parser(q($p))->save_parsers()" \
    2>/dev/null || :
done

%preun
if [ $1 -eq 0 ] ; then
  for p in XML::LibXML::SAX::Parser XML::LibXML::SAX ; do
    %{_bindir}/perl -MXML::SAX -e "XML::SAX->remove_parser(q($p))->save_parsers()" \
      2>/dev/null || :
  done
fi

%files
%license LICENSE
%doc AI_POLICY.md Changes HACKING.txt README.md
%{perl_vendorarch}/auto/XML
%dir %{perl_vendorarch}/XML
%{perl_vendorarch}/XML/LibXML*
%{_mandir}/man3/XML::LibXML*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:2.0213-1
- Import
