%global source0_hash 970fd13accd3d538e637db080ebbd9898020c8b5591837c8493a39edd737922d
%bcond_with perl_Module_Pluggable_enables_optional_test
Name:           perl-Module-Pluggable
Epoch:          2
Version:        6.4
Release:        1%{?dist}
Summary:        Automatically give your module the ability to have plugins
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Pluggable
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIMONW/Module-Pluggable-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Module_Pluggable_enables_optional_test}
%endif
Requires:       perl(File::Spec::Functions) >= 3.00
Requires:       perl(deprecate)
Recommends:     perl(Module::Runtime) >= 0.012
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec::Functions\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(No::Middle\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
Provides:       perl(Module::Pluggable)
Provides:       perl(Module::Pluggable::Object)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Module-Pluggable-tests -f %{oreon_filedir}/perl-Module-Pluggable-tests.list

%changelog

%autochangelog
