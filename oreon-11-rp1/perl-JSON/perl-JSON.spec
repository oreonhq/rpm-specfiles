%global source0_hash df8b5143d9a7de99c47b55f1a170bd1f69f711935c186a6dc0ab56dd05758e35

Name:           perl-JSON
Summary:        Parse and convert to JSON (JavaScript Object Notation)
Version:        4.10
Release:        9%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/JSON
Source0:        https://cpan.metacpan.org/modules/by-module/JSON/JSON-%{version}.tar.gz



BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(lib)
BuildRequires:  perl(:VERSION) >= 5.5.30
# Module
BuildRequires:  perl(B)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# subs not used
# Tests
BuildRequires:  perl(charnames)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Optional tests
BuildRequires:  perl(JSON::XS) >= 4.00
BuildRequires:  perl(Types::Serialiser)
# Dependencies
Requires:       perl(B)
Requires:       perl(Encode)
Requires:       perl(Math::BigFloat)
Requires:       perl(Math::BigInt)
Suggests:       perl(Scalar::Util)
Requires:       perl(warnings)

%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(JSON::(Backend::PP|backportPP::Boolean|Boolean|PP|PP::IncrParser)\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(JSON::(backportPP|backportPP::Boolean)\\)

Provides:       perl(JSON)
Provides:       perl(JSON::Syck)
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n JSON-%{version}

# make rpmlint happy...
find .  -type f -exec chmod -c -x {} +
sed -i 's/\r//' README t/*
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
# t/20_unknown.t writes to CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/t "$DIR"
unset PERL_JSON_BACKEND PERL_JSON_DEBUG PERL_JSON_PP_USE_B
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
# Correct permissions
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.10-9
- Prepare for Oreon 11 (RP1)
