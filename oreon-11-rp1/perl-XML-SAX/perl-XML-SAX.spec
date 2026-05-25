Summary:        SAX parser access API for Perl
Name:           perl-XML-SAX
Version:        1.02
Release:        20%{?dist}

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-SAX
# Original source
# http://www.cpan.org/authors/id/G/GR/GRANTM/XML-SAX-%%{version}.tar.gz
Source0:        XML-SAX-%{version}-nopatents.tar.gz
# XML-SAX contains patented code that we cannot ship. Therefore we use
# this script to remove the patented code before shipping it.
# Download the upstream tarball and invoke this script while in the
# tarball's directory:
# ./generate-tarball.sh %%{version}
Source1: generate-tarball.sh

# Fix rt#20126
Patch0:         perl-XML-SAX-0.99-rt20126.patch

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::NamespaceSupport) >= 0.03
# XML::SAX::Base became independent package, BR just for test
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::Exception)
# Test
BuildRequires:  perl(base)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Test)

Requires:       perl(LWP::UserAgent)

# Remove bogus XML::SAX::PurePerl* dependencies and unversioned provides
%global __requires_exclude ^perl\\(XML::SAX::PurePerl
%global __provides_exclude ^perl\\(XML::SAX::PurePerl\\)$

%description
XML::SAX consists of several framework classes for using and building
Perl SAX2 XML parsers, filters, and drivers. It is designed around the
need to be able to "plug in" different SAX parsers to an application
without requiring programmer intervention. Those of you familiar with
the DBI will be right at home. Some of the designs come from the Java
JAXP specification (SAX part), only without the javaness.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n XML-SAX-%{version}
%patch -P0 -p1
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
echo N | perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}
touch %{buildroot}%{perl_vendorlib}/XML/SAX/ParserDetails.ini

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t testfiles %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99cleanup.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./

# Non-root user is not possible to work with system
# %{perl_vendorlib}/XML/SAX/ParserDetails.ini
if [ `id -u` -ne 0 ]; then
    rm t/01known.t t/20factory.t t/21saxini.t
    prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
else
    cp -p "%{perl_vendorlib}/XML/SAX/ParserDetails.ini" "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup"
    prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
    mv "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup" "%{perl_vendorlib}/XML/SAX/ParserDetails.ini"
fi

popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

# See http://rhn.redhat.com/errata/RHBA-2010-0008.html regarding these scriptlets
# perl-XML-LibXML-1.58-6 is in EL 5.8 and possibly later EL-5 releases
%post
if [ ! -f "%{perl_vendorlib}/XML/SAX/ParserDetails.ini" ] ; then
  perl -MXML::SAX -e \
    'XML::SAX->add_parser(q(XML::SAX::PurePerl))->save_parsers()' 2>/dev/null || :
else
  cp -p "%{perl_vendorlib}/XML/SAX/ParserDetails.ini" "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup"
fi

%triggerun -- perl-XML-LibXML < 1.58-8
if [ -f "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup" ] ; then
  mv "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup" "%{perl_vendorlib}/XML/SAX/ParserDetails.ini"
fi

%preun
# create backup of ParserDetails.ini, therefore user's configuration is used
if [ $1 -eq 0 ] ; then
  perl -MXML::SAX -e \
    'XML::SAX->remove_parser(q(XML::SAX::PurePerl))->save_parsers()' || :
fi
[ -f "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup" ] && \
rm -rf "%{perl_vendorlib}/XML/SAX/ParserDetails.ini.backup" || :

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/SAX.pm
%dir %{perl_vendorlib}/XML/SAX/
%{perl_vendorlib}/XML/SAX/*.pm
%doc %{perl_vendorlib}/XML/SAX/*.pod
%{perl_vendorlib}/XML/SAX/PurePerl/
%{_mandir}/man3/XML::*.3pm*
%ghost %{perl_vendorlib}/XML/SAX/ParserDetails.ini

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.02-20
- Import
