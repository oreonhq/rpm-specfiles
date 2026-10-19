%global source0_hash ef9f44141073c13573e85b148ff9a9089c45825b7d6608d832e4263899d3a2d4
%bcond_without perl_Crypt_URandom_enables_optional_test
Name:           perl-Crypt-URandom
Version:        0.55
Release:        1%{?dist}
Summary:        Non-blocking randomness for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-URandom
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDICK/Crypt-URandom-%{version}.tar.gz
%if %{with perl_Crypt_URandom_enables_optional_test}
%endif
Requires:       perl(Carp) >= 1.26
Requires:       perl(FileHandle)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Carp\\)$
Provides:       perl(Crypt::URandom)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a check_random.inc t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/boilerplate.t
%if %{with perl_Crypt_URandom_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
mkdir -p "$DIR/blib/lib/Crypt"
cp %{perl_vendorarch}/Crypt/URandom.pm "$DIR/blib/lib/Crypt"
pushd "$DIR"
unset CRYPT_URANDOM_BUILD_DEBUG
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset CRYPT_URANDOM_BUILD_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Crypt-URandom-tests -f %{oreon_filedir}/perl-Crypt-URandom-tests.list

%changelog

%autochangelog
