%global base_version 1.59

Name:           perl-threads-shared
Version:        1.70
Release:        521%{?dist}
Summary:        Perl extension for sharing data structures between threads
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/threads-shared
Source0:        https://cpan.metacpan.org/authors/id/J/JD/JDHEDDEN/threads-shared-%{base_version}.tar.gz
# Unbundled from perl 5.29.10
Patch0:         threads-shared-1.59-Upgrade-to-1.60.patch
# Fix a memory leak when assigning a shared reference to a shared string
# variable, in perl after 5.31.1
Patch1:         threads-shared-1.60-threads-shared-fix-leak.patch
# Unbundled from perl 5.32.0
Patch2:         threads-shared-1.59-Upgrade-to-1.61.patch
# Unbundled from perl 5.34.0
Patch3:         threads-shared-1.61-Upgrade-to-1.62.patch
# Unbundled from perl 5.35.11
Patch4:         threads-shared-1.62-Upgrade-to-1.64.patch
# Unbundled from perl 5.37.11
Patch5:         threads-shared-1.64-Upgrade-to-1.68.patch
# Unbundled from perl 5.40.0-RC1
Patch6:         threads-shared-1.68-Upgrade-to-1.69.patch
# Unbundled from perl 5.42.0
Patch7:         threads-shared-1.69-Upgrade-to-1.70.patch
# oreon url source checksums begin
%global source0_sha256 d1fc985e70e1e1dd53c2b9b07cf0d3bd526b4f404ef1c4a0033feaa167323fcf
%global source0_file threads-shared-1.59.tar.gz
# oreon url source checksums end
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
# Config_m not needed
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(threads) >= 1.73
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Time::HiRes)
# Win32 not needed
Requires:       perl(Carp)
Requires:       perl(threads) >= 1.73
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
By default, variables are private to each thread, and each newly created
thread gets a private copy of each existing variable. This module allows
you to share variables across different threads (and pseudo-forks on
Win32). It is used together with the threads module.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(POSIX)
Requires:       perl(Time::HiRes)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/threads-shared-1.59.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d1fc985e70e1e1dd53c2b9b07cf0d3bd526b4f404ef1c4a0033feaa167323fcf" || { echo "oreon: Source0 SHA256 mismatch for threads-shared-1.59.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n threads-shared-%{base_version}

# Generate ppport.h
perl -MDevel::PPPort \
    -e "Devel::PPPort::WriteFile() or die 'Could not generate ppport.h: $!'"

# Help generators to recognize Perl scripts
for F in t/*.t t/*pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
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
unset GIT_DIR PERL_BUILD_PACKAGING PERL_CORE PERL_RUNPERL_DEBUG \
    RUN_MAINTAINER_TESTS
make test

%files
%doc Changes examples README
%{perl_vendorarch}/auto/threads*
%{perl_vendorarch}/threads*
%{_mandir}/man3/threads::shared*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.70-521
- Prepare for Oreon 11 (RP1)
