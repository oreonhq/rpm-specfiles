%global source0_hash 38639c5c707694e2174ef7cb33bbfeb05f2098709f9b380b3869fd1a6d38a914
Name:           perl-XML-DifferenceMarkup
Version:        1.05
Release:        41%{?dist}
Summary:        XML diff and merge
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-DifferenceMarkup
Source0:        https://cpan.metacpan.org/authors/id/V/VB/VBAR/XML-DifferenceMarkup-%{version}.tar.gz
Patch0:         XML-DifferenceMarkup-1.05-Do-not-override-CCFLAGS.patch
Patch1:         perl-XML-DifferenceMarkup-configure-c99.patch
Patch2:         XML-DifferenceMarkup-1.05-Adapt-to-libxml2-2.12.0-and-gcc-14.patch
Requires:       perl(XML::LibXML) >= 1.70
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XML::LibXML\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  diffmark-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%global oreon_srcdir XML-DifferenceMarkup-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t testdata %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-XML-DifferenceMarkup-tests -f %{oreon_filedir}/perl-XML-DifferenceMarkup-tests.list

%changelog

%autochangelog
