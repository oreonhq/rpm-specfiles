%global source0_hash a571b24181baaa76c96704e92acffc6934ff593e380dade274db4e43c140ad51
Name:           perl-Crypt-OpenSSL-Random
Version:        0.17
Release:        6%{?dist}
Summary:        OpenSSL/LibreSSL pseudo-random number generator access
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-OpenSSL-Random
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Crypt-OpenSSL-Random-%{version}.tar.gz
%{?perl_default_filter}
Provides:       perl(Crypt::OpenSSL::Random)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::OpenSSL::Guess)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Crypt::OpenSSL::Random provides the ability to seed and query the OpenSSL
and LibreSSL library's pseudo-random number generators.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Crypt-OpenSSL-Random-%{version}
# Remove author-only tests that are always skipped
for F in t/z_kwalitee.t t/z_manifest.t t/z_meta.t t/z_perl_minimum_version.t \
     t/z_pod-coverage.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\E'"$F"'\Q}' MANIFEST
done;

%build

unset AUTOMATED_TESTING
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/z_pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Crypt-OpenSSL-Random-tests -f %{oreon_filedir}/perl-Crypt-OpenSSL-Random-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.17-6
- Prepare for Oreon 11 (RP1)
