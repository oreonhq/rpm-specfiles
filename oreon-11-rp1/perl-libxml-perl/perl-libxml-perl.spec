%global source0_hash 4571059b7b5d48b7ce52b01389e95d798bf5cf2020523c153ff27b498153c9cb
Name:           perl-libxml-perl
Version:        0.08
Release:        1%{?dist}
Summary:        A collection of Perl modules for working with XML
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Public-Domain
URL:            https://metacpan.org/release/libxml-perl
Source0:        https://cpan.metacpan.org/authors/id/K/KM/KMACLEOD/libxml-perl-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(XML::Parser) >= 2.19
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(Data::Grove\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(XML::Parser\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
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

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-libxml-perl-tests -f %{oreon_filedir}/perl-libxml-perl-tests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.08-56
- Import
