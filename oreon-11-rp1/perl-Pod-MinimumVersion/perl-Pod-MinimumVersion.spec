%global source0_hash 0bd2812d9aacbd99bb71fa103a4bb129e955c138ba7598734207dc9fb67b5a6f

Name:           perl-Pod-MinimumVersion
Version:        50
Release:        44%{?dist}
Summary:        Perl version for POD directives used
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/Pod-MinimumVersion
Source0:        https://cpan.metacpan.org/authors/id/K/KR/KRYDE/Pod-MinimumVersion-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.4
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
# inc/my_pod2html not executed
# Run-time:
# Getopt::Long not used at tests
BuildRequires:  perl(IO::String) >= 1.02
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(Data::Dumper)
# Devel::FindRef not used
# Devel::StackTrace not used
BuildRequires:  perl(Exporter)
# Scalar::Util not used
BuildRequires:  perl(Test)
Requires:       perl(IO::String) >= 1.02
# This module has been divided from perl-Perl-Critic-Pulp
Conflicts:      perl-Perl-Critic-Pulp < 49

# Remove private modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MyTestHelpers\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(MyTestHelpers\\)$

Provides:       perl(Pod::MinimumVersion)
%description
Pod::MinimumVersion parses the POD in a Perl script, module, or document,
and reports what version of Perl is required to process the directives in
it with pod2man etc.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-MinimumVersion-%{version}
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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license COPYING
%doc Changes
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man3/*
%{_mandir}/man1/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
