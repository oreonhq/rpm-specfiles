# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 044404d4fdb52485bf143e2661eb4b59de955d4805231befad1bb41bfb715a6f
%global source1_hash d360e039412451e0596d4cf0ae9a072d15f94ba0beb4c0740c3ca5340de6f5b2
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary:        SAX parser access API for Perl
Name:           perl-XML-SAX
Version:        1.02
Release:        1%{?dist}

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-SAX
Source0:        XML-SAX-%{version}-nopatents.tar.gz
Source1: generate-tarball.sh

Patch0:         perl-XML-SAX-0.99-rt20126.patch

BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
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
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::Exception)
BuildRequires:  perl(base)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Test)

Requires:       perl(LWP::UserAgent)

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
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%setup -q -n XML-SAX-%{version}
%patch -P0 -p1
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

mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t testfiles %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99cleanup.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./

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
%autochangelog
