%global source0_hash 3d26c20df42628981cbfcfa5b1ca028c6ceadb344c1dcf97a25ad6a88b73d7c5

# noarch, but to avoid debug* files interfering with manifest test:
%global debug_package %{nil}

%if 0%{?fedora} && 0%{?fedora} < 37
# Similarly for .package_note* files (#2059504)
%undefine _package_note_file
%endif

Name:           perl-Test-DistManifest
Version:        1.014
Release:        34%{?dist}
Summary:        Author test that validates a package MANIFEST
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-DistManifest
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-DistManifest-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(Module::Manifest) >= 0.07
BuildRequires:  perl(Test::Builder)
# Tests only:
BuildRequires:  perl(if)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
# Test::Warnings not used without $ENV{AUTHOR_TESTING}
# Dependencies:

# Remove private modules
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

Provides:       perl(Test::DistManifest)
%description
This Perl module provides a simple method of testing that a MANIFEST matches
the distribution.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-DistManifest-%{version}
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
PERL_MM_FALLBACK_SILENCE_WARNING=1 perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/00*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README examples/
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::DistManifest.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
