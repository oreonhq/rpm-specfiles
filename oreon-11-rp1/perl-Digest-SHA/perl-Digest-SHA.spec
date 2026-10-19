%global source0_hash ee91f8f7db894ee7c6ee003daac10a99056c4948a674ef46acdbb63c81a4abeb
%bcond_without perl_Digest_SHA_enables_digest_base
%bcond_with perl_Digest_SHA_enables_optional_test
Name:           perl-Digest-SHA
Epoch:          1
Version:        6.04
Release:        1%{?dist}
Summary:        Perl extension for SHA-1/224/256/384/512
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Digest-SHA
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSHELOR/Digest-SHA-%{version}.tar.gz
Patch0:         Digest-SHA-5.93-Reset-CFLAGS.patch
%if %{with perl_Digest_SHA_enables_digest_base}
%endif
%if %{with perl_Digest_SHA_enables_optional_test}
%if !%{defined perl_bootstrap}
%endif
%endif
Requires:       perl(Carp)
%if %{with perl_Digest_SHA_enables_digest_base}
Requires:       perl(Digest::base)
%endif
Requires:       perl(XSLoader)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
rm %{buildroot}%{_libexecdir}/%{name}/t/podcover.t
perl -i -pe 's{"methods.tmp"}{"/tmp/methods.tmp"}' %{buildroot}%{_libexecdir}/%{name}/t/methods.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Digest-SHA-tests -f %{oreon_filedir}/perl-Digest-SHA-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.04-522
- Prepare for Oreon 11 (RP1)
