%global source0_hash e5833b74e733baee19d1ef5e04b1263c1cff9c1746995ad72fc40918f440675e

Name:       perl-asa 
Version:    1.04
Release:    21%{?dist}
Summary:    Lets your class/object say it works like something else
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/asa
Source:     https://cpan.metacpan.org/authors/id/E/ET/ETHER/asa-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.5
BuildRequires:  perl(Carp)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful

%description
Perl 5 doesn't natively support Java-style interfaces, and it doesn't support
Perl 6 style roles either.

You can get both of these things in half a dozen different ways via various
CPAN modules, but they usually require that you buy into "their way" of
implementing your code.

This package overrides the isa() method, allowing your class to claim it's
a class it's not (that is, isn't in @ISA).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n asa-%{version}
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
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/asa.pm
%{_mandir}/man3/asa.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
