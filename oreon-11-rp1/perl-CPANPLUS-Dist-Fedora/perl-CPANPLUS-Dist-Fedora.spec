%global source0_hash 6dc580d9844551d2ddf1592c9dc6aa59f350123e7c2113fc18ff96796e99d4a9

%global pkgname CPANPLUS-Dist-Fedora

# Do not perform tests that need the Internet
%bcond_with perl_CPAN_Dist_Fedora_enables_network

Name:           perl-CPANPLUS-Dist-Fedora
Version:        0.4.4
Release:        12%{?dist}
Summary:        CPANPLUS backend to build Fedora/RedHat RPMs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPANPLUS-Dist-Fedora
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(CPANPLUS::Dist::Base)
BuildRequires:  perl(CPANPLUS::Error)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::POM::View::Text)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Template)
%if %{with perl_CPAN_Dist_Fedora_enables_network}
BuildRequires:  gcc rpm rpm-build
%endif
# Tests:
BuildRequires:  perl(blib)
%if %{with perl_CPAN_Dist_Fedora_enables_network}
BuildRequires:  perl(CPANPLUS::Backend)
%endif
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
Requires:       gcc
Requires:       rpm
Requires:       rpm-build

# Filter modules bundled for tests
%if %{without perl_CPAN_Dist_Fedora_enables_network}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CPANPLUS::Backend\\)
%endif

%description
This is a distribution class to create Fedora packages from CPAN modules, 
and all its dependencies. This allows you to have the most recent copies of 
CPAN modules installed, using your package manager of choice, but without 
having to wait for central repositories to be updated.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_CPAN_Dist_Fedora_enables_network}
Requires:       perl(CPANPLUS::Backend)
%endif

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

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
%if %{with perl_CPAN_Dist_Fedora_enables_network}
export TEST_CPANPLUS_FEDORA=1
%else
unset TEST_CPANPLUS_FEDORA
%endif
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
%if %{with perl_CPAN_Dist_Fedora_enables_network}
export TEST_CPANPLUS_FEDORA=1
%else
unset TEST_CPANPLUS_FEDORA
%endif
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
