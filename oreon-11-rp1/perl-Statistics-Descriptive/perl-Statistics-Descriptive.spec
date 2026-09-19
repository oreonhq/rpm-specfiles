%global source0_hash 047b70a63fdcaa916168e0ff2d58e155e0ebbc68ed4ccbd73a7213dca3028f65

Name:           perl-Statistics-Descriptive
Version:        3.0801
Release:        8%{?dist}
Summary:        Perl module of basic descriptive statistical functions
# lib/Statistics/Descriptive.pm:            GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Statistics/Descriptive/Full.pm:       GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Statistics/Descriptive/Sparse.pm:     GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Statistics/Descriptive/Smoother*:     MIT
# t/lib/Utils.pm:                           MIT
# examples/statistical-analysis.pl:         MIT
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND MIT
URL:            https://metacpan.org/release/Statistics-Descriptive
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Statistics-Descriptive-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88

%{?perl_default_filter}
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Utils\\)

%description
This module provides basic functions used in descriptive statistics. It has
an object oriented design and supports two different types of data storage
and calculation objects: sparse and full. With the sparse method, none of
the data is stored and only a few statistical measures are available. Using
the full method, the entire data set is retained and additional functions
are available.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Statistics-Descriptive-%{version}

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
# Remove release test
rm %{buildroot}%{_libexecdir}/%{name}/t/boilerplate.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
./Build test

%files
%license LICENSE
%doc Changes examples README UserSurvey.txt
%{perl_vendorlib}/Statistics*
%{_mandir}/man3/Statistics::Descriptive*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
