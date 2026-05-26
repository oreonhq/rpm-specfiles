# Perform optional tests
%bcond_without perl_Compress_Raw_Lzma_enables_optional_test

Name:		perl-Compress-Raw-Lzma
Version:	2.221
Release:	1%{?dist}
Summary:	Low-level interface to lzma compression library
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Compress-Raw-Lzma
Source0:	https://cpan.metacpan.org/authors/id/P/PM/PMQS/Compress-Raw-Lzma-2.221.tar.gz
# oreon url source checksums begin
%global source0_sha256 e8b2d17c7f29b3e4f286cc3d3f5353df8e811615c42298eedad7cdbfec4aed7f
%global source0_file Compress-Raw-Lzma-2.221.tar.gz
# oreon url source checksums end

# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::Constant)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(lib)
BuildRequires:	xz-devel
# Module Runtime
BuildRequires:	perl(AutoLoader)
BuildRequires:	perl(bytes)
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(UNIVERSAL)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(File::Path)
BuildRequires:	perl(Test::More)
%if %{with perl_Compress_Raw_Lzma_enables_optional_test}
# Optional Tests
BuildRequires:	perl(Test::CPAN::Meta)
BuildRequires:	perl(Test::CPAN::Meta::JSON)
BuildRequires:	perl(Test::NoWarnings)
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	xz
%endif
# Dependencies
Requires:	perl(XSLoader)

# Don't "provide" private Perl libs
%{?perl_default_filter}
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CompTestUtils\\)

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Compress-Raw-Lzma-2.221.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e8b2d17c7f29b3e4f286cc3d3f5353df8e811615c42298eedad7cdbfec4aed7f" || { echo "oreon: Source0 SHA256 mismatch for Compress-Raw-Lzma-2.221.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
rm %{buildroot}%{_libexecdir}/%{name}/t/meta*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
export TEST_SKIP_VERSION_CHECK=1
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# See https://src.fedoraproject.org/rpms/perl-Compress-Raw-Lzma/pull-request/3
export TEST_SKIP_VERSION_CHECK=1
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README SECURITY.md
%{perl_vendorarch}/auto/Compress/
%{perl_vendorarch}/Compress/
%{_mandir}/man3/Compress::Raw::Lzma.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.221-1
- Import
