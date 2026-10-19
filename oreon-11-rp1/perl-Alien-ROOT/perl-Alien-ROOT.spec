%global source0_hash a1fcc14631906c768864f91f0ef9a6b57c6599ef2ab524f2877db47e34e2ca50
Name:           perl-Alien-ROOT
Version:        5.34.36.1
Release:        37%{?dist}
Summary:        Utility package to install and locate CERN's ROOT library
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Alien-ROOT
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Alien-ROOT-v%{version}.tar.gz
Patch0:         Alien-ROOT-v5.34.36.1-Disable-build-time-check-for-Root.patch
BuildArch:      noarch
Requires:       perl(Config)
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(File::Spec)
Requires:       perl(IPC::Open3)
Requires:       root-core
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Fetch)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The original intention is to install and detect CERN's ROOT library. This
package always requires the ROOT library provided with your distribution.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Alien::ROOT)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Alien-ROOT-v%{version}
%patch -P0 -p1
# Remove bundled modules
find inc -depth -mindepth 1 -maxdepth 1 \! -name Alien -exec rm -rf -- {} +
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
find inc -type f >> MANIFEST
# Bypass inc::latest as it requires packlists
perl -i -pe "s/use inc::latest '([^']*)'/use \$1/" Build.PL

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Alien-ROOT-tests -f %{oreon_filedir}/perl-Alien-ROOT-tests.list

%changelog

%autochangelog
