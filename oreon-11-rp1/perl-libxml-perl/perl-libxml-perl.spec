Name:           perl-libxml-perl
Version:        0.08
Release:        56%{?dist}
Summary:        A collection of Perl modules for working with XML
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Public-Domain
URL:            https://metacpan.org/release/libxml-perl
Source0:        https://cpan.metacpan.org/authors/id/K/KM/KMACLEOD/libxml-perl-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 4571059b7b5d48b7ce52b01389e95d798bf5cf2020523c153ff27b498153c9cb
%global source0_file libxml-perl-0.08.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.5.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(strict)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::Parser) >= 2.19
# Tests:
Requires:       perl(XML::Parser) >= 2.19

# Filter out unversioned provides
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(Data::Grove\\)$
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XML::Parser\\)$

%description
libxml-perl is a collection of smaller Perl modules, scripts, and
documents for working with XML in Perl.  libxml-perl software works in
combination with XML::Parser, PerlSAX, XML::DOM, XML::Grove and
others.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libxml-perl-0.08.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4571059b7b5d48b7ce52b01389e95d798bf5cf2020523c153ff27b498153c9cb" || { echo "oreon: Source0 SHA256 mismatch for libxml-perl-0.08.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n libxml-perl-%{version}
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
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%doc ChangeLog Changes README
%{perl_vendorlib}/Data/
%{perl_vendorlib}/XML/
%{_mandir}/man3/Data*.3*
%{_mandir}/man3/XML*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.08-56
- Import
