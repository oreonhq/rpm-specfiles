%global source0_hash 0bf3019811a62f0bf479dceb5449e8e2b854d59abed9e3dca7a3ca8b91e27122

Name:           perl-Math-FFT
Version:        1.36
Release:        19%{?dist}
Summary:        Perl module to calculate Fast Fourier Transforms
# arrays.c:         GPL-1.0-or-later OR Artistic-1.0-Perl (copied from
#                   <https://metacpan.org/dist/PGPLOT>)
# fft4g.c:          copied from <http://www.kurims.kyoto-u.ac.jp/~ooura/fft.html>
#                   LicenseRef-Fedora-UltraPermissive according to
#                   https://gitlab.com/fedora/legal/fedora-license-data/-/issues/604
# lib/Math/FFT.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-UltraPermissive
URL:            https://metacpan.org/release/Math-FFT
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Math-FFT-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::More) >= 0.88

# Remove under-specifiec dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# Hide private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(MathFftResults\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(MathFftResults\\)

%description
This module implements some algorithms for calculating Fast Fourier
Transforms for one-dimensional data sets of size 2^n. 

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.88

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-FFT-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorarch}/auto/Math
%{perl_vendorarch}/auto/Math/FFT
%dir %{perl_vendorarch}/Math
%{perl_vendorarch}/Math/FFT.pm
%{_mandir}/man3/Math::FFT.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
