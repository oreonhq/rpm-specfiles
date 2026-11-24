# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8522b532935a11bfa688c2e113bac66729df4851be50c2c26d4b06f45fade472
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond perl_WWW_RobotRules_enables_DB_File %{undefined rhel}

Name:           perl-WWW-RobotRules
Version:        6.03
Release:        1%{?dist}
Summary:        Database of robots.txt-derived permissions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-RobotRules
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/WWW-RobotRules-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(AnyDBM_File)
BuildRequires:  perl(Carp)
%if %{with perl_WWW_RobotRules_enables_DB_File}
BuildRequires:  perl(DB_File)
%endif
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(URI) >= 1.10
BuildRequires:  perl(vars)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
Requires:       perl(URI) >= 1.10
Conflicts:      perl-libwww-perl < 6
%if %{with perl_WWW_RobotRules_enables_DB_File}
Suggests:       perl(WWW::RobotRules::DB_File)
%endif

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(URI\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(WWW::RobotRules::InCore\\)

%description
This module parses /robots.txt files as specified in "A Standard for Robot
Exclusion", at <https://www.robotstxt.org/robotstxt.html>. Webmasters can
use the /robots.txt file to forbid conforming robots from accessing parts
of their web site.

%if %{with perl_WWW_RobotRules_enables_DB_File}
%package DB_File
Summary:        Parse robots.txt files using a disk cache
Conflicts:      perl-WWW-RobotRules < 6.03-2

%description DB_File
This is a subclass of WWW::RobotRules that uses the DB_File package to
implement disk caching of robots.txt.
%endif

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%oreon_sha256
%setup -q -n WWW-RobotRules-%{version}
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

%check
make test

%files
%doc Changes
%license LICENSE
%exclude %{perl_vendorlib}/WWW/RobotRules/DB_File.pm
%{perl_vendorlib}/*
%exclude %{_mandir}/man3/WWW::RobotRules::DB_File.3*
%{_mandir}/man3/*

%if %{with perl_WWW_RobotRules_enables_DB_File}
%files DB_File
%license LICENSE
%{perl_vendorlib}/WWW/RobotRules/DB_File.pm
%{_mandir}/man3/WWW::RobotRules::DB_File.3*
%endif

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
