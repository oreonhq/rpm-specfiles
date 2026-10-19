%global source0_hash 2af21c5d61ac34ea26a5fabf15ba5a5841e648f7189db3e33b6f28b5489802ab
%bcond_with thread_test
Name:           perl-XML-LibXML
Version:        2.0213
Release:        1%{?dist}
Epoch:          1
Summary:        Perl interface to the libxml2 library
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MIT
URL:            https://metacpan.org/release/XML-LibXML
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/XML-LibXML-%{version}.tar.gz
Patch0:        XML-LibXML-2.0202-Parse-an-ampersand-entity-in-SAX-interface.patch
Patch1:        XML-LibXML-2.0212-Use-pkgconfig-instead-of-Alien-Libxml2.patch
%if ! ( 0%{?rhel} ) || (0%{?oreon} >= 11)
%endif
%if %{with thread_test}
%endif
Requires:       perl(Data::Dumper)
Requires:           perl-interpreter
Requires(preun):    perl-interpreter
Provides:       perl-XML-LibXML-Common = %{version}
Obsoletes:      perl-XML-LibXML-Common <= 0.13
%{?perl_default_filter}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Collector\\)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(Counter)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(Stacker)\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(TestHelpers)\s*$
%if 0%{?rhel} || (0%{?oreon} >= 11)
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::LeakTrace)\s*$
%endif
Provides:       perl(XML::LibXML)
Provides:       perl(XML::LibXML::Boolean)
Provides:       perl(XML::LibXML::Literal)
Provides:       perl(XML::LibXML::NodeList)
Provides:       perl(XML::LibXML::Number)
Provides:       perl(XML::LibXML::Reader)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  glibc-gconv-extra
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(XML::NamespaceSupport)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::DocumentLocator)
BuildRequires:  perl(XML::SAX::Exception)
BuildRequires:  perl(XML::SAX::ParserFactory)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(locale)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
%description
This module implements a Perl interface to the GNOME libxml2 library
which provides interfaces for parsing and manipulating XML files. This
module allows Perl programmers to make use of the highly capable
validating XML parser and the high performance DOM implementation.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a example t test %{buildroot}%{_libexecdir}/%{name}
for F in example/*.pl t/cpan-changes.t t/11memory.t t/pod.t \
        t/pod-files-presence.t t/release-kwalitee.t t/style-trailing-space.t; do
    rm -f %{buildroot}%{_libexecdir}/%{name}/"$F"
done
perl -i -pe 's{example/(testrun.xml)}{/tmp/$1}' %{buildroot}%{_libexecdir}/%{name}/t/03doc.t
cat > %{buildroot}%{_libexecdir}/%{name}/tests << 'EOF'
unset AUTHOR_TESTING RELEASE_TESTING
cd %{_libexecdir}/%{name} && THREAD_TEST=0%{?with_thread_test:1} exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/tests
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n perl-XML-LibXML-tests -f %{oreon_filedir}/perl-XML-LibXML-tests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:2.0213-1
- Import
