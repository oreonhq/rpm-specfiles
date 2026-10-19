%global source0_hash e8b2d17c7f29b3e4f286cc3d3f5353df8e811615c42298eedad7cdbfec4aed7f
%bcond_without perl_Compress_Raw_Lzma_enables_optional_test
Name:		perl-Compress-Raw-Lzma
Version:	2.221
Release:        1%{?dist}
Summary:        Low-level interface to lzma compression library
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Compress-Raw-Lzma
Source0:        https://cpan.metacpan.org/modules/by-module/Compress/Compress-Raw-Lzma-%{version}.tar.gz
%if %{with perl_Compress_Raw_Lzma_enables_optional_test}
%endif
Requires:	perl(XSLoader)
%{?perl_default_filter}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CompTestUtils\\)
Provides:       perl(Compress::Raw::Lzma)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  xz
BuildRequires:  xz-devel
# /oreon:deps
%description
This module provides a Perl interface to the lzma compression library.
It is used by IO::Compress::Lzma.

%package tests
Summary:	Tests for %{name}
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Compress-Raw-Lzma-%{version}

# Remove bundled test modules
rm -rv t/Test/
perl -i -ne 'print $_ unless m{^t/Test/}' MANIFEST

# Help generators to recognize Perl scripts
for F in t/*.t; do
  perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
  chmod +x "$F"
done

%build

perl Makefile.PL \
  INSTALLDIRS=vendor \
  NO_PACKLIST=1 \
  NO_PERLLOCAL=1 \
  OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
rm %{buildroot}%{_libexecdir}/%{name}/t/meta*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
export TEST_SKIP_VERSION_CHECK=1
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export TEST_SKIP_VERSION_CHECK=1
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Compress-Raw-Lzma-tests -f %{oreon_filedir}/perl-Compress-Raw-Lzma-tests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.221-1
- Import
