%global source0_hash b23401c1226fee8dfe627f5ae0e90c55ac547010eca398110dc1631f41c9ec7d

Name:           perl-Net-IPv6Addr
Version:        1.02
Release:        14%{?dist}
Summary:        Perl module to check validity of IPv6 addresses

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-IPv6Addr
Source0:        https://cpan.metacpan.org/authors/id/B/BK/BKB/Net-IPv6Addr-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(utf8)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Math::BigInt) >= 1.999813
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
Requires:       perl(Math::BigInt) >= 1.999813

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Math::BigInt\\)\s*$

%description
Net::IPv6Addr checks strings for valid IPv6 addresses, as specified in
RFC1884. You throw possible addresses at it, it either accepts them or throws
an exception.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-IPv6Addr-%{version}
perl -MConfig -i -pe 's/\A#!.*perl/$Config{startperl}/' examples/*

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
# Needed for t/synopsis.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/examples
cp -a examples/synopsis.pl %{buildroot}%{_libexecdir}/%{name}/examples
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc examples Changes README
%{perl_vendorlib}/*
%{_mandir}/man?/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
