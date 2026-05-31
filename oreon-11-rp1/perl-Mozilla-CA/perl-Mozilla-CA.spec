%global source0_hash none

Name:           perl-Mozilla-CA
# You do not need to back-port a new version for updating a list of the
# certificates. They are taken from ca-certificates package instead
# per bug #738383.
Version:        20250602
Release:        3%{?dist}
Summary:        Mozilla's CA certificate bundle in PEM format
# README:                       MPL-2.0
## Unbundled
# mk-ca-bundle.pl:              MIT
# lib/Mozilla/CA/cacert.pem:    MPL-2.0
License:        MPL-2.0
URL:            https://metacpan.org/release/Mozilla-CA
Source0:        https://cpan.metacpan.org/authors/id/L/LW/LWP/Mozilla-CA-%{version}.tar.gz
# Use a CA bundle from ca-certificates package, bug #738383
Patch0:         Mozilla-CA-20250602-Redirect-to-ca-certificates-bundle.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  ca-certificates
BuildRequires:  perl(strict)
BuildRequires:  perl(File::Spec)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       ca-certificates

%description
Mozilla::CA provides a path to ca-certificates copy of Mozilla's bundle of
certificate authority certificates in a form that can be consumed by modules
and libraries based on OpenSSL.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Mozilla-CA-%{version}
%patch -P0 -p1
# Remove a bundled CA bundle for sure
rm lib/Mozilla/CA/cacert.pem
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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20250602-3
- Import
