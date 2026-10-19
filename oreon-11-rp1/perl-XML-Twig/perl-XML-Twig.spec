%global source0_hash 0b744a9737a070f95c32154afd526bf5ebe76a59feb8bc1f5dbc6cdaa5e0e529
%bcond_with perl_XML_Twig_enables_optional_test
Name:           perl-XML-Twig
Version:        3.54
Release:        1%{?dist}
Summary:        Perl module for processing huge XML documents in tree mode
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Twig
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIROD/XML-Twig-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_XML_Twig_enables_optional_test}
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
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XML::Parser\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(tools\\)
Provides:       perl(XML::Twig)
Provides:       perl(XML::Twig::Elt)
Provides:       perl(XML::Twig::Elt)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  expat
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::XPathEngine)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
unset TEST_AUTHOR
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-XML-Twig-tests -f %{oreon_filedir}/perl-XML-Twig-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.54-3
- Prepare for Oreon 11 (RP1)
