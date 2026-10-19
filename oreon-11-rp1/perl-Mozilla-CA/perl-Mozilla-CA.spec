%global source0_hash 81f0bd9665eacbb6feef13b0fa16fbb30162c09292542b1206434e569196dd9b
Name:           perl-Mozilla-CA
Version:        20260813
Release:        1%{?dist}
Summary:        Mozilla's CA certificate bundle in PEM format
License:        MPL-2.0
URL:            https://metacpan.org/release/Mozilla-CA
Source0:        https://cpan.metacpan.org/authors/id/L/LW/LWP/Mozilla-CA-%{version}.tar.gz
Patch0:         Mozilla-CA-20250602-Redirect-to-ca-certificates-bundle.patch
BuildArch:      noarch
Requires:       ca-certificates
Provides:       perl(Mozilla::CA)
# oreon:deps
BuildRequires:  ca-certificates
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Mozilla-CA-tests -f %{oreon_filedir}/perl-Mozilla-CA-tests.list

%changelog

%autochangelog
