%global source0_hash 74a2021259cb6cf7bbb9f4caa2677dca820fd93c8f1322336f48a48793155bdc

Name:           perl-Net-Netmask
Version:        2.0003
Release:        3%{?dist}
Summary:        Perl module for manipulating and looking up IP network blocks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Netmask
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMASLAK/Net-Netmask-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigInt) >= 1.999811
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(vars)
# Tests only
# Benchmark not used when runnig the tests through make check or prove
# Test::More 0.96 not used
# Test::Perl::Critic not used
# Test::Pod 1.41 not used
BuildRequires:  perl(Test::UseAllModules) >= 0.17
# Test::Version not used
BuildRequires:  perl(Test2::V0) >= 0.000111
BuildRequires:  perl(utf8)
# Optional tests
# Test::Vars not used
Requires:       perl(Math::BigInt) >= 1.999811

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Math::BigInt\\)$

%description
Net::Netmask parses and understands IPv4 and IPv6 CIDR blocks (see
<https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing> for more
information on CIDR blocks). There are also functions to insert a network
block into a table and then later look up network blocks by an IP address
using that table.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Netmask-%{version}

# Help file to recognise the Perl scripts
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
rm -rf %{buildroot}%{_libexecdir}/%{name}/t/release*
rm -rf %{buildroot}%{_libexecdir}/%{name}/t/author*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING RELEASE_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
