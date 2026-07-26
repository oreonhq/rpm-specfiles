%global source0_hash 340a706817d2c1af8bde47c5b4e7f506c537f75f24425409d82c4a5fe3bffc0b

# Perform optional tests
%bcond_without perl_lib_abs_enable_optional_test

Name:           perl-lib-abs
Version:        0.95
Release:        20%{?dist}
Summary:        Module lib that makes relative path absolute to caller
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/lib-abs
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MONS/lib-abs-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd) >= 3.12
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Carp::Heavy)
# DynaLoader not used
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(XSLoader)
%if %{with perl_lib_abs_enable_optional_test}
# Optional tests:
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod) >= 1.22
%endif
Requires:       perl(Carp)

%description
The main reason of this library is to transform relative paths to absolute
at the BEGIN stage, and push transformed to @INC. Relative path basis is
not the current working directory, but the location of file, where the
statement is (caller file). When using common lib, relative paths stays
relative to current working directory.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(File::Spec)
Requires:       perl(XSLoader)
%if %{with perl_lib_abs_enable_optional_test}
Requires:       perl(Test::NoWarnings)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n lib-abs-%{version}
# Remove bunlded modules
rm -rf ./inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
%if !%{with perl_lib_abs_enable_optional_test}
rm t/pod.t
perl -i -ne 'print $_ unless m{^t/pod.t}' MANIFEST
%endif
# Remove /usr/bin/env from shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1 INSTALLDIRS=vendor
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_lib_abs_enable_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
set -e
# Needs to write to CWD, CPAN RT#91853
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
# Not parallel-safe, CPAN RT#91853
prove -I . -j 1
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# Not parallel-safe, CPAN RT#91853
export HARNESS_OPTIONS=j1
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
