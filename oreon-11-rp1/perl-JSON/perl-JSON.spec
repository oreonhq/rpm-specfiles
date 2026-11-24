# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 713bdbe724dbb915ed50265ffe47e079a511980cb2427aa19076788bb64c3182
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           perl-JSON
Summary:        Parse and convert to JSON (JavaScript Object Notation)
Version:        4.11
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/JSON
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/JSON-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(lib)
BuildRequires:  perl(:VERSION) >= 5.5.30
BuildRequires:  perl(B)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util) >= 1.08
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(charnames)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(JSON::XS) >= 4.00
BuildRequires:  perl(Types::Serialiser)
Requires:       perl(B)
Requires:       perl(Encode)
Requires:       perl(Math::BigFloat)
Requires:       perl(Math::BigInt)
Suggests:       perl(Scalar::Util)
Requires:       perl(warnings)

%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(JSON::(Backend::PP|backportPP::Boolean|Boolean|PP|PP::IncrParser)\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(JSON::(backportPP|backportPP::Boolean)\\)

%description
This module converts between JSON (JavaScript Object Notation) and Perl
data structure into each other. For JSON, see http://www.crockford.com/JSON/.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Tie::IxHash)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%oreon_sha256
%setup -q -n JSON-%{version}

find .  -type f -exec chmod -c -x {} +
sed -i 's/\r//' README t/*
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/t "$DIR"
unset PERL_JSON_BACKEND PERL_JSON_DEBUG PERL_JSON_PP_USE_B
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} -c %{buildroot}

%check
unset PERL_JSON_BACKEND PERL_JSON_DEBUG PERL_JSON_PP_USE_B
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
