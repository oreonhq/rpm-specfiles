%global source0_hash 54d40fdcfb93e61bcd3e24fbf5b41700e68236e2a1d4e3f4d5ba883ce2a53e6b

Name:           perl-CPAN-Plugin-Sysdeps
Version:        0.80
Release:        3%{?dist}
Summary:        CPAN client plugin for installing system dependencies
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Plugin-Sysdeps
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/CPAN-Plugin-Sysdeps-%{version}.tar.gz
# Prevent a build script from accidental execution in an author mode
Patch0:         CPAN-Plugin-Sysdeps-0.66-Disable-probing-for-an-author-mode.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
# dnf5 not used at tests
BuildRequires:  perl(constant)
# CPAN::Distribution not used at tests
BuildRequires:  perl(Data::Dumper)
# Getopt::Long not used at tests
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(warnings)
BuildRequires:  rpm
# Optional run-time:
BuildRequires:  perl(Hash::Util)
# The code prefers parsing /etc/os-release
%if 0%{?rhel}
BuildRequires:  redhat-release
%else
BuildRequires:  fedora-release-common
%endif
# sudo not used at tests
# Tests:
# CPAN::Distribution || CPAN
BuildRequires:  perl(CPAN::Distribution)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
Requires:       dnf5
Requires:       perl(Data::Dumper)
Recommends:     perl(Hash::Util)
Requires:       perl(IPC::Open3)
Requires:       perl(Symbol)
Requires:       rpm
%if 0%{?rhel}
Recommends:     redhat-release
%else
Recommends:     fedora-release-common
%endif
Recommends:     sudo

# Filter private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(TestUtil\\)

%description
CPAN::Plugin::Sysdeps is a plugin for CPAN Perl module to install non-CPAN
dependencies automatically. Currently, the list of required system
dependencies is maintained in a static data structure in
CPAN::Plugin::Sysdeps::Mapping.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# CPAN::Distribution || CPAN
Requires:       perl(CPAN::Distribution)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n CPAN-Plugin-Sysdeps-%{version}
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
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset CPAN_PLUGIN_SYSDEPS_DEBUG PERL_CPAN_SYSDEPS_UV_UTIL_NATIVE
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset CPAN_PLUGIN_SYSDEPS_DEBUG PERL_CPAN_SYSDEPS_UV_UTIL_NATIVE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README.md
%{_bindir}/cpan-sysdeps
%dir %{perl_vendorlib}/CPAN
%dir %{perl_vendorlib}/CPAN/Plugin
%{perl_vendorlib}/CPAN/Plugin/Sysdeps
%{perl_vendorlib}/CPAN/Plugin/Sysdeps.pm
%{_mandir}/man1/cpan-sysdeps.1*
%{_mandir}/man3/CPAN::Plugin::Sysdeps::*
%{_mandir}/man3/CPAN::Plugin::Sysdeps.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
