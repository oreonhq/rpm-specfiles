%global source0_hash f2ba62a52f32d18aea8a8ca73299bef0e52409332cfe514a9c475316f6d5351c

# Recognize terminal size
%bcond_without perl_Term_Table_enables_terminal
# Respect Unicode rules when breaking lines
%bcond_without perl_Term_Table_enables_unicode

Name:           perl-Term-Table
Version:        0.028
Release:        2%{?dist}
Summary:        Format a header and rows into a table
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Table
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Term-Table-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
# Optional run-time:
%if %{with perl_Term_Table_enables_terminal}
# Term::ReadKey 2.32 not used if Term::Size::Any is available
# Prefer Term::Size::Any over Term::ReadKey
BuildRequires:  perl(Term::Size::Any) >= 0.002
%endif
%if %{with perl_Term_Table_enables_unicode}
BuildRequires:  perl(Unicode::GCString) >= 2013.10
%endif
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::Tools::Tiny) >= 1.302097
BuildRequires:  perl(utf8)
%if %{with perl_Term_Table_enables_terminal}
Suggests:       perl(Term::ReadKey) >= 2.32
# Prefer Term::Size::Any over Term::ReadKey
Recommends:     perl(Term::Size::Any) >= 0.002
%endif
%if %{with perl_Term_Table_enables_unicode}
Recommends:     perl(Unicode::GCString) >= 2013.10
%endif

# Remove private test modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(main::HBase|main::HBase::Wrapped\\)$

%description
This Perl module is able to format rows of data into tables.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Term-Table-%{version}
# XXX Don't unbundle Term::Table::HashBase, the module is in Perl Core.
# Help generators to recognize Perl scripts
for F in t/*.t t/Table/*.t; do
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
cd %{_libexecdir}/%{name} && exec prove -r -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
unset TABLE_TERM_SIZE
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.028-2
- Prepare for Oreon 11 (RP1)
