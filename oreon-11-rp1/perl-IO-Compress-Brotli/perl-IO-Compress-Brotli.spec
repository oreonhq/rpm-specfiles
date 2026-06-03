%global source0_hash none

%global cpan_version 0.022
Name:           perl-IO-Compress-Brotli
Version:        %{cpan_version}000
Release:        5%{?dist}
Summary:        Perl bindings for Brotli compression
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Compress-Brotli/
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/IO-Compress-Brotli-%{cpan_version}.tar.gz
Patch0:        https://src.fedoraproject.org/rpms/perl-IO-Compress-Brotli/raw/rawhide/f/IO-Compress-Brotli-0.019-Use-pkgconfig-instead-of-bundled-libbrotli.patch

# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig)
# Run-time
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Test::More)
# Used in the installed script `bro-perl` - added by perl-generators
# BuildRequires:  perl(Getopt::Long)
# BuildRequires:  perl(Time::HiRes)

%description
IO::Compress::Brotli is a module that compresses Brotli buffers and
streams. Despite its name, it is not a subclass of IO::Compress::Base
and does not implement its interface. This will be rectified in a
future release.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Test::Harness)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IO-Compress-Brotli-%{cpan_version}
%patch -P0 -p1

# Remove bundled source
for F in `find brotli -type f | grep -v testdata`; do 
    rm -rf $F
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/brotli/tests
cp -a brotli/tests/testdata %{buildroot}%{_libexecdir}/%{name}/brotli/tests/
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/IO*
%{_mandir}/man3/*
%{_bindir}/bro-perl

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.019000-5
- Import
