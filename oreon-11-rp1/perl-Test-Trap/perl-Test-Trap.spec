%global source0_hash 54f99016562b5b1d72110100f1f2be437178cdf84376f495ffd0376f1d7ecb9a

Name:           perl-Test-Trap
Version:        0.3.5
Release:        9%{?dist}
Summary:        Trap exit codes, exceptions, output, etc
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Trap
Source0:        https://cpan.metacpan.org/authors/id/E/EB/EBHANSSEN/Test-Trap-v%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Refcount)
BuildRequires:  perl(Test::Tester) >= 0.107
# Optional tests
BuildRequires:  perl(IO::Scalar)
Requires:       perl(Test::More)

Provides:       perl(Test::Trap)
%description
Primarily (but not exclusively) for use in test scripts: A block eval on
steroids, configurable and extensible, but by default trapping (Perl)
STDOUT, STDERR, warnings, exceptions, would-be exit codes, and return
values from boxed blocks of test code.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Trap-v%{version}

# Help generators to recognize Perl scripts
for F in t/*.t t/*.pl t/*.PL; do
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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
