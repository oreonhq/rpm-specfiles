%global source0_hash 30ef32fac30f268a3d9062c44fd5ab7518499bf993b50ef8ee372d8787bcb9a8

Summary:            Perl extension for generating XML
Name:               perl-XML-Generator
Version:            1.13
Release:            8%{?dist}
License:            GPL-1.0-or-later OR Artistic-1.0-Perl
URL:                https://metacpan.org/release/XML-Generator
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/XML-Generator-%{version}.tar.gz
BuildArch:          noarch
BuildRequires:      coreutils
BuildRequires:      make
BuildRequires:      perl-generators
BuildRequires:      perl-interpreter
BuildRequires:      perl(Config)
BuildRequires:      perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:      perl(strict)
BuildRequires:      perl(warnings)
# Run-time:
BuildRequires:      perl(base)
BuildRequires:      perl(Carp)
BuildRequires:      perl(constant)
BuildRequires:      perl(overload)
BuildRequires:      perl(vars)
BuildRequires:      perl(XML::DOM)
# Tests:
BuildRequires:      perl(Test)
BuildRequires:      perl(Test::More)
BuildRequires:      perl(utf8)
# Optional tests:
BuildRequires:      perl(Tie::IxHash)
Requires:           perl(warnings)

%description
Perl module for generating XML documents

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Tie::IxHash)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n XML-Generator-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/author-pod-*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.13-8
- Prepare for Oreon 11 (RP1)
