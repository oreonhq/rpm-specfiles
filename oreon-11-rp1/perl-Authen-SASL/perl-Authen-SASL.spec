Name:           perl-Authen-SASL
Version:        2.2000
Release:        1%{?dist}
Summary:        SASL Authentication framework for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Authen-SASL
Source0:        https://cpan.metacpan.org/authors/id/E/EH/EHUELS/Authen-SASL-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 8cdf5a7f185448b614471675dae5b26f8c6e330b62264c3ff5d91172d6889b99
%global source0_file Authen-SASL-2.2000.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest::HMAC_MD5)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(GSSAPI)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
Requires:       perl(Tie::Handle)

%description
SASL is a generic mechanism for authentication used by several network
protocols. Authen::SASL provides an implementation framework that all
protocols should be able to share.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Carp)
Requires:       perl(Digest::MD5)
Requires:       perl(Digest::HMAC_MD5)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Authen-SASL-2.2000.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8cdf5a7f185448b614471675dae5b26f8c6e330b62264c3ff5d91172d6889b99" || { echo "oreon: Source0 SHA256 mismatch for Authen-SASL-2.2000.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n Authen-SASL-%{version}

# Fix permissions
chmod -c a-x eg/*

# Help generators to recognize Perl scripts
for F in `find t -name *.t -o -name *.pl`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/author-pod-syntax.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc api.txt Changes eg README
%{perl_vendorlib}/Authen
%{_mandir}/man3/Authen::SASL*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2000-1
- Prepare for Oreon 11 (RP1)
