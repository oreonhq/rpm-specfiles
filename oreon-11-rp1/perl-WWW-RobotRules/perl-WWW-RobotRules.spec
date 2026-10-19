%global source0_hash 8522b532935a11bfa688c2e113bac66729df4851be50c2c26d4b06f45fade472
Name:           perl-WWW-RobotRules
Version:        6.03
Release:        1%{?dist}
Summary:        Database of robots.txt-derived permissions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-RobotRules
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/WWW-RobotRules-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(URI) >= 1.10
Conflicts:      perl-libwww-perl < 6
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(URI\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(WWW::RobotRules::InCore\\)
Provides:       perl(WWW::RobotRules)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(AnyDBM_File)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module parses /robots.txt files as specified in "A Standard for Robot
Exclusion", at <https://www.robotstxt.org/robotstxt.html>. Webmasters can
use the /robots.txt file to forbid conforming robots from accessing parts
of their web site.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n WWW-RobotRules-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -fr %{buildroot}%{_libexecdir}/%{name}/t/misc
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-WWW-RobotRules-tests -f %{oreon_filedir}/perl-WWW-RobotRules-tests.list

%changelog

%autochangelog
