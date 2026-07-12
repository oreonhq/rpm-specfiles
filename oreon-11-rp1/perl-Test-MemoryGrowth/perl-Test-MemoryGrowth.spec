%global source0_hash 66ec08871b0288949cb2d0244a2bbdfe24d8f66d5839605fee74e54511e19d37

Name:           perl-Test-MemoryGrowth
Version:        0.05
Release:        4%{?dist}
Summary:        Assert that code does not cause growth in memory usage
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-MemoryGrowth
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-MemoryGrowth-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
# Devel::Gladiator is optional
# Devel::MAT::Dumper is optional
BuildRequires:  perl(Test::Builder::Module)
# Tests only
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Builder::Tester)
Recommends:     perl(Devel::Gladiator)

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

Provides:       perl(Test::MemoryGrowth)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%description
This module provides a function to check that a given block of code does
not result in the process consuming extra memory once it has finished.
Despite the name of this module it does not, in the strictest sense of the
word, test for a memory leak: that term is specifically applied to cases
where memory has been allocated but all record of it has been lost, so it
cannot possibly be reclaimed. While the method employed by this module can
detect such bugs, it can also detect cases where memory is still referenced
and reachable, but the usage has grown more than would be expected or
necessary.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-MemoryGrowth-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99pod.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
./Build test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/Test
%{perl_vendorlib}/Test/*
%{_mandir}/man3/Test::MemoryGrowth*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
