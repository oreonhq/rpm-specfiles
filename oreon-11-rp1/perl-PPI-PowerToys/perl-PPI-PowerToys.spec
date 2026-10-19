%global source0_hash c4798d110ef8642331c5328ca66fc4250aaf2f00421957e3ceba8a728f78276e
Name:           perl-PPI-PowerToys
Version:        0.14
Release:        1%{?dist}
Summary:        Handy collection of small PPI-based utilities
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PPI-PowerToys
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/PPI-PowerToys-%{version}.tar.gz
Patch0:         PPI-PowerToys-0.14-Remove-using-of-MI-DSL.patch
BuildArch:      noarch
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\((File::Find::Rule|File::Find::Rule::Perl|File::Spec|Getopt::Long|IPC::Run3|PPI::Document|Probe::Perl|Test::More|Test::Script|version)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Find::Rule::Perl)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Probe::Perl)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(blib)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The PPI PowerToys are a small collection of utilities for working with Perl
files, modules and distributions.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(blib)
Requires:       perl(IPC::Run3) >= 0.034
Requires:       perl(Probe::Perl) >= 0.01
Requires:       perl(Test::More) >= 0.47
Requires:       perl(Test::Script) >= 1.03
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n PPI-PowerToys-%{version}
# Remove bundled libraries
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
# Remove tests which are always skipped
for T in t/97_meta.t t/98_pod.t t/99_pmv.t; do
    rm "$T"
    perl -i -ne 'print $_ unless m{^\Q'"$T"'\E}' MANIFEST
done
chmod +x t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a Makefile.PL t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
mkdir -p "$DIR"/lib/PPI "$DIR"/script "$DIR"/blib/lib/auto "$DIR"/blib/arch
ln -s %{perl_vendorlib}/PPI/PowerToys.pm "$DIR"/lib/PPI
ln -s %{_bindir}/ppi_copyright "$DIR"/script
ln -s %{_bindir}/ppi_version "$DIR"/script
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-PPI-PowerToys-tests -f %{oreon_filedir}/perl-PPI-PowerToys-tests.list

%changelog

%autochangelog
