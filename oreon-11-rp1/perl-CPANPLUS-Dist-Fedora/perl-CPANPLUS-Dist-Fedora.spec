%global source0_hash 6dc580d9844551d2ddf1592c9dc6aa59f350123e7c2113fc18ff96796e99d4a9
%global pkgname CPANPLUS-Dist-Fedora
%bcond_with perl_CPAN_Dist_Fedora_enables_network
Name:           perl-CPANPLUS-Dist-Fedora
Version:        0.4.4
Release:        12%{?dist}
Summary:        CPANPLUS backend to build Fedora/RedHat RPMs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPANPLUS-Dist-Fedora
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
Requires:       gcc
Requires:       rpm
Requires:       rpm-build
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(CPANPLUS::Dist::Base)
BuildRequires:  perl(CPANPLUS::Error)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::POM::View::Text)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a distribution class to create Fedora packages from CPAN modules, 
and all its dependencies. This allows you to have the most recent copies of 
CPAN modules installed, using your package manager of choice, but without 
having to wait for central repositories to be updated.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}

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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset TEST_CPANPLUS_FEDORA
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset TEST_CPANPLUS_FEDORA
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-CPANPLUS-Dist-Fedora-tests -f %{oreon_filedir}/perl-CPANPLUS-Dist-Fedora-tests.list

%changelog

%autochangelog
