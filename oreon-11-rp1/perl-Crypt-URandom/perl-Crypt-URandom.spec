%global source0_hash ef9f44141073c13573e85b148ff9a9089c45825b7d6608d832e4263899d3a2d4

# Perform optional tests
%bcond_without perl_Crypt_URandom_enables_optional_test

Name:           perl-Crypt-URandom
Version:        0.55
Release:        1%{?dist}
Summary:        Non-blocking randomness for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-URandom
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDICK/Crypt-URandom-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp) >= 1.26
BuildRequires:  perl(constant)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FileHandle)
# Win32 not used
# Win32::API not used
# Win32::API::Type not used
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Encode)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
%if %{with perl_Crypt_URandom_enables_optional_test}
# Optional tests:
# Devel::Cover not helpful
BuildRequires:  perl(Test::Pod) >= 1.14
%endif
Requires:       perl(Carp) >= 1.26
Requires:       perl(FileHandle)

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Carp\\)$

Provides:       perl(Crypt::URandom)
%description
This Module is intended to provide an interface to the strongest available
source of non-blocking randomness on the current platform.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       gcc
Requires:       perl-Test-Harness
Requires:       perl(Carp) >= 1.26

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Crypt-URandom-%{version}
%if !%{with perl_Crypt_URandom_enables_optional_test}
rm t/pod.t
perl -i -ne 'print $_ unless m{^t/pod.t}' MANIFEST
%endif
# Delete always skipped release tests
rm t/manifest.t
perl -i -ne 'print $_ unless m{^t/manifest.t}' MANIFEST
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
unset CRYPT_URANDOM_BUILD_DEBUG
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a check_random.inc t %{buildroot}%{_libexecdir}/%{name}
# t/boilerplate.t expects files in source archive locations.
rm %{buildroot}%{_libexecdir}/%{name}/t/boilerplate.t
%if %{with perl_Crypt_URandom_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
# check_random.inc and t/getrandom.t write into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
# t/core_read.t etc. needs URandom.pm in ./blib without URandom.so
mkdir -p "$DIR/blib/lib/Crypt"
cp %{perl_vendorarch}/Crypt/URandom.pm "$DIR/blib/lib/Crypt"
pushd "$DIR"
unset CRYPT_URANDOM_BUILD_DEBUG
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset CRYPT_URANDOM_BUILD_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
# README.md is identical to README.
%doc Changes README SECURITY.md
%dir %{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/auto/Crypt/URandom
%dir %{perl_vendorarch}/Crypt
%{perl_vendorarch}/Crypt/URandom.pm
%{_mandir}/man3/Crypt::URandom.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
