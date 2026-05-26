# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 ee91f8f7db894ee7c6ee003daac10a99056c4948a674ef46acdbb63c81a4abeb
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Inherit additional methods from Digest::Base
%bcond_without perl_Digest_SHA_enables_digest_base
# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Digest_SHA_enables_optional_test
%else
%bcond_with perl_Digest_SHA_enables_optional_test
%endif

Name:           perl-Digest-SHA
Epoch:          1
Version:        6.04
Release:        522%{?dist}
Summary:        Perl extension for SHA-1/224/256/384/512
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Digest-SHA
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSHELOR/Digest-SHA-%{version}.tar.gz
# Since 5.80, upstream overrides CFLAGS because they think it improves
# performance. Revert it.
Patch0:         Digest-SHA-5.93-Reset-CFLAGS.patch
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
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
# Getopt::Long not used at tests
BuildRequires:  perl(integer)
BuildRequires:  perl(warnings)
# XSLoader or DynaLoader
BuildRequires:  perl(XSLoader)
# Optional run-time
%if %{with perl_Digest_SHA_enables_digest_base}
BuildRequires:  perl(Digest::base)
%endif
# Tests
BuildRequires:  perl(FileHandle)
%if %{with perl_Digest_SHA_enables_optional_test}
# Optional tests
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 0.08
%endif
%endif
Requires:       perl(Carp)
# Optional but recommended
%if %{with perl_Digest_SHA_enables_digest_base}
Requires:       perl(Digest::base)
%endif
# XSLoader or DynaLoader
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
Digest::SHA is a complete implementation of the NIST Secure Hash Standard. It
gives Perl programmers a convenient way to calculate SHA-1, SHA-224, SHA-256,
SHA-384, SHA-512, SHA-512/224, and SHA-512/256 message digests. The module can
handle all types of input, including partial-byte data.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%oreon_verify_sources
%setup -q -n Digest-SHA-%{version}
%patch -P0 -p1
chmod -x examples/*
perl -MExtUtils::MakeMaker -e 'ExtUtils::MM_Unix->fixin(q{examples/dups})'

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE='%{optflags}'
%{make_build}

%install
%{make_install}
find '%{buildroot}' -type f -name '*.bs' -empty -delete
%{_fixperms} -c '%{buildroot}'

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
rm %{buildroot}%{_libexecdir}/%{name}/t/podcover.t
# Create a temporary file in /tmp
perl -i -pe 's{"methods.tmp"}{"/tmp/methods.tmp"}' %{buildroot}%{_libexecdir}/%{name}/t/methods.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes examples/ README
%{_bindir}/shasum
%{perl_vendorarch}/auto/Digest/
%{perl_vendorarch}/Digest/
%{_mandir}/man1/shasum.1*
%{_mandir}/man3/Digest::SHA.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.04-522
- Prepare for Oreon 11 (RP1)
