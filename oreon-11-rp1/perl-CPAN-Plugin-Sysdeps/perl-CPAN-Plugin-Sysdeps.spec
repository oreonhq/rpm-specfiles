%global source0_hash 54d40fdcfb93e61bcd3e24fbf5b41700e68236e2a1d4e3f4d5ba883ce2a53e6b
Name:           perl-CPAN-Plugin-Sysdeps
Version:        0.80
Release:        1%{?dist}
Summary:        CPAN client plugin for installing system dependencies
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Plugin-Sysdeps
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/CPAN-Plugin-Sysdeps-%{version}.tar.gz
Patch0:         CPAN-Plugin-Sysdeps-0.66-Disable-probing-for-an-author-mode.patch
BuildArch:      noarch
Requires:       dnf5
Requires:       perl(Data::Dumper)
Recommends:     perl(Hash::Util)
Requires:       perl(IPC::Open3)
Requires:       perl(Symbol)
Requires:       rpm
Recommends:     fedora-release-common
Recommends:     sudo
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(TestUtil\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  fedora-release-common
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPAN::Distribution)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  rpm
# /oreon:deps
%description
CPAN::Plugin::Sysdeps is a plugin for CPAN Perl module to install non-CPAN
dependencies automatically. Currently, the list of required system
dependencies is maintained in a static data structure in
CPAN::Plugin::Sysdeps::Mapping.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset CPAN_PLUGIN_SYSDEPS_DEBUG PERL_CPAN_SYSDEPS_UV_UTIL_NATIVE
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset CPAN_PLUGIN_SYSDEPS_DEBUG PERL_CPAN_SYSDEPS_UV_UTIL_NATIVE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-CPAN-Plugin-Sysdeps-tests -f %{oreon_filedir}/perl-CPAN-Plugin-Sysdeps-tests.list

%changelog

%autochangelog
