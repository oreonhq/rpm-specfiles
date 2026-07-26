%global source0_hash a9826f56483a27e2c63156590f328a3633e30375c10dfc89f6690e3929de0bc3

Name:           perl-Test-Bits
Version:        0.02
Release:        18%{?dist}
Summary:        Provides a bits_is() subroutine for testing binary data
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-Bits
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Test-Bits-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder::Module)
# Tests:
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Tester)

%description
This Perl module provides a single subroutine, bits_is(), for testing
binary data.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Bits-%{version}
# Remove tests which are skipped by default
rm t/author-* t/release-*
perl -i -ne 'print $_ unless m{\At\/(?:author|release)-}' MANIFEST
# Remove a redundant test. There is only Test::Bits module and that is loaded
# in t/bits_is.t.
rm t/00-compile.t
perl -i -ne 'print $_ unless m{\A\Qt/00-compile.t\E}' MANIFEST
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
%doc Changes README
%dir %{perl_vendorlib}/Test
%{perl_vendorlib}/Test/Bits.pm
%{_mandir}/man3/Test::Bits.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
