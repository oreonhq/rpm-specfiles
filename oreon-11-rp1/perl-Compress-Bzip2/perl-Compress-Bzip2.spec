%global source0_hash 859f835c3f5c998810d8b2a6f9e282ff99d6cb66ccfa55cae7e66dafb035116e
%bcond_with perl_Compress_Bzip2_enables_optional_test
Name:           perl-Compress-Bzip2
Version:        2.28
Release:        1%{?dist}
Summary:        Interface to Bzip2 compression library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Compress-Bzip2
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Compress-Bzip2-%{version}.tar.gz
%if !%{defined perl_bootstrap} && %{with perl_Compress_Bzip2_enables_optional_test}
%endif
Requires:       perl(constant) >= 1.04
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(constant\\)$
Provides:       perl(Compress::Bzip2)
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Compress::Bzip2 module provides a Perl interface to the Bzip2 compression
library. A relevant subset of the functionality provided by Bzip2 is available
in Compress::Bzip2. Compress::Bzip2 is not well integrated into PerlIO, use
the preferred IO::Compress::Bzip2 instead.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       bash
Requires:       bzip2
Requires:       coreutils
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Compress-Bzip2-%{version}
# Remove bundled bzip2 library
find bzlib-src -mindepth 1 -type f \! -name 'sample*' -delete
perl -i -ne 'print $_ unless m{^bzlib-src/}' MANIFEST
find bzlib-src -type f >>MANIFEST
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="$RPM_OPT_FLAGS"
%make_build
%install
%make_install
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
rm -f %{buildroot}/%{_libexecdir}/%{name}/t/900*
rm -f %{buildroot}/%{_libexecdir}/%{name}/t/090-memory-usage.pl
mkdir -p %{buildroot}/%{_libexecdir}/%{name}/bzlib-src
for F in sample0.bz2 sample0.ref sample1.bz2 sample1.ref sample2.bz2 sample2.ref sample3.bz2 sample3.ref; do
    cp "bzlib-src/$F" %{buildroot}/%{_libexecdir}/%{name}/bzlib-src/
done
cp -a config.in %{buildroot}/%{_libexecdir}/%{name}/
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Compress-Bzip2-tests -f %{oreon_filedir}/perl-Compress-Bzip2-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.28-25
- Prepare for Oreon 11 (RP1)
