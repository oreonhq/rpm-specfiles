%global source0_hash e6f51c4ff35a4097ba24ab9edeae04cca01cb93f5441559c1ba2003747d3dd7d

Name:           perl-Devel-Declare-Parser
Version:        0.021
Release:        7%{?dist}
Summary:        Higher level interface to Devel-Declare
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Declare-Parser
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Devel-Declare-Parser-%{version}.tar.gz
Patch0:         perl-Devel-Declare-Parser-fix-dependencies.patch
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(B::Compiling) >= 0.02
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.08
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Declare) >= 0.006
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple) >= 0.88
Requires:       perl(B::Compiling) >= 0.02
Requires:       perl(B::Hooks::EndOfScope) >= 0.08
Requires:       perl(Devel::Declare) >= 0.006

# Filter unversioned dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(B::Compiling\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(B::Hooks::EndOfScope\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Devel::Declare\\)

%description
Devel-Declare-Parser is a higher-level API sitting on top of
Devel::Declare. It is used by Devel::Declare::Exporter to simplify
exporting of Devel::Declare magic. Writing custom parsers usualy only
requires subclassing this module and overriding a couple methods.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-Declare-Parser-%{version}
%patch -P0 -p1
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%doc README
%{perl_vendorlib}/Devel/Declare*
%{_mandir}/man3/Devel::Declare::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
