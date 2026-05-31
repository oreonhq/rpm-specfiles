%global source0_hash f2b1987ecef9f6c9223e8fba2e8e48854333896650aabea81bdc30e0c9656b63

Name:           perl-Test-Inter
Version:        1.12
Release:        4%{?dist}
Summary:        Framework for more readable interactive test scripts
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Inter
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBECK/Test-Inter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
# Tests only:
BuildRequires:  perl(Config)
# File::Find::Rule not used
BuildRequires:  perl(Storable) >= 1.01
BuildRequires:  perl(Test::More)
# Test::Pod 1.00 not used
# Test::Pod::Coverage 1.00 not used
Requires:       perl(lib)

%description
This is another framework for writing test scripts. It is loosely inspired
by Test::More, and has most of it's functionality, but it is not a drop-in
replacement.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Inter-%{version}
chmod -x examples/*
# Help generators to recognize Perl scripts
for F in t/*.t; do
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
rm -f %{buildroot}%{_libexecdir}/%{name}/t/_*
# Directory for libraries used in tests
mkdir %{buildroot}%{_libexecdir}/%{name}/lib
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
unset RELEASE_TESTING TI_END TI_MODE TI_NOCLEAN TI_QUIET TI_START TI_TESTNUM \
    TI_WIDTH
make test

%files
%license LICENSE
%doc Changes README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.12-4
- Prepare for Oreon 11 (RP1)
