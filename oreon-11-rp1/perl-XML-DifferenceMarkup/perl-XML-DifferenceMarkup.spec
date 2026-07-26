%global source0_hash 38639c5c707694e2174ef7cb33bbfeb05f2098709f9b380b3869fd1a6d38a914

Name:           perl-XML-DifferenceMarkup
Version:        1.05
Release:        41%{?dist}
Summary:        XML diff and merge
# ppport.h:     GPL-1.0-or-later OR Artistic-1.0-Perl
# README:       GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-DifferenceMarkup
Source0:        https://cpan.metacpan.org/authors/id/V/VB/VBAR/XML-DifferenceMarkup-%{version}.tar.gz
# Use system CLFAGS
Patch0:         XML-DifferenceMarkup-1.05-Do-not-override-CCFLAGS.patch
# Adapt to GCC 13, proposed to an upstream, CPAN RT#145911
Patch1:         perl-XML-DifferenceMarkup-configure-c99.patch
# Adapt to libxml2 2.12.0 and GCC 14, proposed to the upstream, CPAN RT#151218
Patch2:         XML-DifferenceMarkup-1.05-Adapt-to-libxml2-2.12.0-and-gcc-14.patch
BuildRequires:  coreutils
BuildRequires:  diffmark-devel
BuildRequires:  findutils
# Makefile.PL generates a temporary Makefile.PL distribution with an XS
# file that links to probe libxml2 (with gcc) and diffmark (with g++)
# libraries.
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(XML::LibXML) >= 1.70
BuildRequires:  perl(XSLoader)
# Tests only:
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
Requires:       perl(XML::LibXML) >= 1.70

%{?perl_default_filter}

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XML::LibXML\\)$

%description
This module implements an XML diff producing XML output. Both input and
output are DOM documents, as implemented by XML::LibXML.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(XML::LibXML) >= 1.70

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n XML-DifferenceMarkup-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t testdata %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%dir %{perl_vendorarch}/auto/XML
%dir %{perl_vendorarch}/auto/XML/DifferenceMarkup
%{perl_vendorarch}/auto/XML/DifferenceMarkup/DifferenceMarkup.so
%dir %{perl_vendorarch}/XML
%{perl_vendorarch}/XML/DifferenceMarkup.pm
%{_mandir}/man3/XML::DifferenceMarkup.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
