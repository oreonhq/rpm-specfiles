%global source0_hash 1fad13f7dcb80897e55f16c919c185a1829ec1a328c613e06cc6330b3b6a169d
%bcond_without perl_XML_Hash_LX_enables_optional_test
%global cpan_version 0.07
Name:           perl-XML-Hash-LX
Version:        0.70.0
Release:        1%{?dist}
Summary:        Convert hash to XML and XML to hash using LibXML
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Hash-LX
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MONS/XML-Hash-LX-%{cpan_version}.tar.gz
BuildArch:      noarch
%if %{with perl_XML_Hash_LX_enables_optional_test}
%endif
Requires:       perl(Carp)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(lib::abs\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  glibc-gconv-extra
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Types::Serialiser)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib::abs)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is a companion for XML::LibXML. It operates with LibXML
objects, could return or accept LibXML objects, and may be used for
easy data transformations.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       glibc-gconv-extra
Requires:       perl-Test-Harness
Requires:       perl(lib::abs) >= 0.90
%if %{with perl_XML_Hash_LX_enables_optional_test}
Requires:       perl(Test::NoWarnings)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Hash-LX-%{cpan_version}
# Remove bundled modules
rm -rf ./inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
%if !%{with perl_XML_Hash_LX_enables_optional_test}
rm t/pod*
perl -i -ne 'print $_ unless m{^t/pod}' MANIFEST
%endif
# Fix shell bangs
for F in ex/* t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl}{$Config{startperl}}' "$F"
done
chmod +x t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_XML_Hash_LX_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod*
%endif
mkdir -p %{buildroot}%{_libexecdir}/%{name}/lib
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-XML-Hash-LX-tests -f %{oreon_filedir}/perl-XML-Hash-LX-tests.list

%changelog

%autochangelog
