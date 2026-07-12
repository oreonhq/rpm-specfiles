%global source0_hash adf1b9079b2b781755e5704877a1430a5f12997ea82205fd2966c9cc465a8522

Name:           perl-Digest-SHA3
Version:        1.05
Release:        12%{?dist}
Summary:        Perl extension for SHA-3
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Digest-SHA3
Source0:        https://cpan.metacpan.org/modules/by-module/Digest/Digest-SHA3-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(integer)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 0.08
Requires:       perl(Carp)
Requires:       perl(Digest::base)
Requires:       perl(XSLoader)

Provides:       perl(Digest::SHA3)
%description
Digest::SHA3 is written in C for speed. If your platform lacks a C
compiler, perhaps you can find the module in a binary form compatible with
your particular processor and operating system.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Digest-SHA3-%{version}
perl -MConfig -pi -e 's|^#!.*perl|$Config{startperl}|' examples/dups3
chmod -c -x examples/dups3

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod*.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README examples
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Digest*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%package -n sha3sum
Summary:        Compute and check SHA3 message digest
BuildArch:      noarch
Requires:       perl(Digest::SHA3)

%description -n sha3sum
This script will compute and check the SHA3 message digest of a file

%files -n sha3sum
%doc README
%{_mandir}/man1/*
%{_bindir}/*

%changelog
%autochangelog
