%global source0_hash 2a0b95b22dbf20daf2fea51d9b71eaaf8d193b0a5be534ed2be10eb483fd428a

Name:           perl-Test-Synopsis-Expectation
Version:        0.12
Release:        7%{?dist}
Summary:        Test that SYNOPSIS code produces expected results
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Synopsis-Expectation
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MOZNION/Test-Synopsis-Expectation-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Simple::Methody)
BuildRequires:  perl(PPI::Tokenizer)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::More) >= 0.98
# Tests
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Builder::Tester)
Requires:       perl(Test::More) >= 0.98

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::More\\)$

%description
This module checks that a module's SYNOPSIS section is syntactically
correct, and will also check that it produces the expected results, based
on annotations you add in comments.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.98

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Synopsis-Expectation-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
unset RELEASE_TESTING
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
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
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test::Synopsis*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
