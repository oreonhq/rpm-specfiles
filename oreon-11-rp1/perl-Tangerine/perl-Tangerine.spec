%global source0_hash ab132422200b214664dc55291d7f4164b077779020307c52cf2e93fce071dd40

Name:           perl-Tangerine
Version:        0.23
Release:        28%{?dist}
Summary:        Analyse perl files and report module-related information
License:        MIT
URL:            https://metacpan.org/release/Tangerine
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CONTYK/Tangerine-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(parent)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version) >= 0.77
# Tests only
BuildRequires:  perl(Test::More)
Requires:       perl(List::Util) >= 1.33

%description
Tangerine statically analyses perl files and reports various information
about provided, used (compile-time dependencies) and required (runtime
dependencies) modules.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tangerine-%{version}
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
rm -f %{buildroot}%{_libexecdir}/%{name}/t/author-pod-syntax.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README.md TODO
%{perl_vendorlib}/*
%{_mandir}/man*/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
