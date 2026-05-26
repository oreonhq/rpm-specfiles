# Run optional test
%if !%{defined perl_bootstrap}
%if ! (0%{?rhel}) || 0%{?oreon}
%bcond_without perl_B_Debug_enables_optional_test
%else
%bcond_with perl_B_Debug_enables_optional_test
%endif
%else
%global _without_perl_B_Debug_enables_optional_test 1
%global _with_perl_B_Debug_enables_optional_test 0
%endif

Name:           perl-B-Debug
Version:        1.26
Release:        444%{?dist}
Summary:        Walk Perl syntax tree, print debug information about op-codes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/B-Debug
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/B-Debug-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 8d6d3f5134f0ddd8dde68e6581f5b30b73b7db40fd28d076e4f6e5386f570d3a
%global source0_file B-Debug-1.26.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(B)
# B::Asmdata not used
BuildRequires:  perl(Config)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(strict)
# Optional run-time:
# B::Flags 0.04 not packaged
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
%if %{with perl_B_Debug_enables_optional_test}
# Optional test:
BuildRequires:  perl(Test::Pod) >= 1.00
%endif
Requires:       perl(deprecate)

%description
Walk Perl syntax tree and print debug information about op-codes. See
B::Concise and B::Terse for other details.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/B-Debug-1.26.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8d6d3f5134f0ddd8dde68e6581f5b30b73b7db40fd28d076e4f6e5386f570d3a" || { echo "oreon: Source0 SHA256 mismatch for B-Debug-1.26.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n B-Debug-%{version}
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
rm -f %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license Artistic Copying
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.26-444
- Import
