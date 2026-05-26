# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Module_Pluggable_enables_optional_test
%else
%bcond_with perl_Module_Pluggable_enables_optional_test
%endif

Name:           perl-Module-Pluggable
Epoch:          2
Version:        6.3
Release:        4%{?dist}
Summary:        Automatically give your module the ability to have plugins
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Pluggable
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIMONW/Module-Pluggable-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 58512bb9c654746d0937770b98b559b30872d85ac24073485e5830890dd1b2a0
%global source0_file Module-Pluggable-6.3.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions) >= 3.00
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(if)
BuildRequires:  perl(vars)
BuildRequires:  perl(Scalar::Util)
# Recommended run-time:
BuildRequires:  perl(Module::Runtime) >= 0.012
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.62
# IncTest is a locally overloaded module in t/lib/Text/Abbrev.pm
%if %{with perl_Module_Pluggable_enables_optional_test}
# Optional tests:
BuildRequires:  perl(App::FatPacker) >= 0.10.0
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Copy)
%endif
Requires:       perl(File::Spec::Functions) >= 3.00
Requires:       perl(deprecate)
# Recommended run-time:
Recommends:     perl(Module::Runtime) >= 0.012

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec::Functions\\)$
# Remove private modules
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(No::Middle\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

%description
This package provides a simple but, hopefully, extensible way of having
'plugins' for your module. Essentially all it does is export a method into
your name space that looks through a search path for .pm files and turn those
into class names. Optionally it instantiates those classes for you.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(File::Spec::Functions) >= 3.00

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Module-Pluggable-6.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "58512bb9c654746d0937770b98b559b30872d85ac24073485e5830890dd1b2a0" || { echo "oreon: Source0 SHA256 mismatch for Module-Pluggable-6.3.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Module-Pluggable-%{version}
find -type f -exec chmod -x {} +
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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.3-4
- Prepare for Oreon 11 (RP1)
