%global source0_hash bf4da40065deebb0544a1348614bb883f74ee9eacf3e0c46e89ce010c1a48d3e

Name:          perl-Verilog-Perl
Version:       3.482
Release:       7%{?dist}
Summary:       Verilog parsing routines
License:       LGPL-3.0-only OR Artistic-2.0
URL:           http://www.veripool.org/wiki/verilog-perl
Source0:       https://cpan.metacpan.org/authors/id/W/WS/WSNYDER/Verilog-Perl-%{version}.tar.gz

BuildRequires: bison
BuildRequires: coreutils
BuildRequires: gcc-c++
BuildRequires: gdbm-devel
BuildRequires: findutils
BuildRequires: flex
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(File::Copy)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(IO::File)
BuildRequires: perl(Pod::Usage) >= 1.34
BuildRequires: perl(strict)
BuildRequires: perl(vars)
# Run-time
BuildRequires: perl(base)
BuildRequires: perl(Cwd)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(FindBin)
BuildRequires: perl(lib)
BuildRequires: perl(Scalar::Util)
# Tests
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(POSIX)
BuildRequires: perl(Test)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(warnings)
# Optional tests
BuildRequires: perl(Devel::Leak)
BuildRequires: perl(Storable)
BuildRequires: perl(Test::Pod) >= 1.00

Provides:      perl-Verilog     = %{version}-%{release}
Obsoletes:     perl-Verilog     < 3.213-2

# Filtering Requires: and Provides
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((imp_test_pkg|mypackage)\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((imp_test_pkg|mypackage)\\)
%global __requires_exclude %{__requires_exclude}|^perl\\((.::t/test_utils.pl)\\)

%description
This package provides functions to support writing utilities
that use the Verilog language.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Devel::Leak)
Requires:       perl(Storable)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Verilog-Perl-%{version}

# Help file to recognise the Perl scripts
for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t verilog %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/00_pod.t
rm -f %{buildroot}%{_libexecdir}/%{name}/t/01_manifest.t
rm -f %{buildroot}%{_libexecdir}/%{name}/t/02_help.t
rm -f %{buildroot}%{_libexecdir}/%{name}/t/03_spaces.t
for i in vhier vpassert vppreproc vrename vsplitmodule; do
    ln -s %{_bindir}/$i %{buildroot}%{_libexecdir}/%{name}/
done
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I .
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# Free Electronic Lab : Package Self Test
make test

%files
%license COPYING
%doc Changes README verilog/
%dir %{perl_vendorarch}/Verilog/
%dir %{perl_vendorarch}/auto/Verilog/
%{_bindir}/*
%{perl_vendorarch}/Verilog/*
%{perl_vendorarch}/auto/Verilog/*
%{_mandir}/man?/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
