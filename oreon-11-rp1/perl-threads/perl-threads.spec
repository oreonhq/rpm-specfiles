%global source0_hash 28394c98a2bcae6f20ffb8a3d965a1c194b764c650169e2050ee38dbaa10f110

%global base_version 2.21
Name:           perl-threads
Epoch:          1
Version:        2.43
Release:        521%{?dist}
Summary:        Perl interpreter-based threads
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/threads
Source0:        https://cpan.metacpan.org/authors/id/J/JD/JDHEDDEN/threads-2.21.tar.gz
# Unbundled from perl 5.40.0-RC1
Patch0:         threads-2.21-Upgrade-to-2.40.patch
# Unbundled from perl 5.42.0
Patch1:         threads-2.40-Upgrade-to-2.43.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::PPPort)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(overload)
BuildRequires:  perl(XSLoader)
# Tests only:
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  procps-ng
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(Thread::Semaphore)
BuildRequires:  perl(threads::shared)
Requires:       perl(Carp)

%{?perl_default_filter}

%description
Since Perl 5.8, thread programming has been available using a model called
interpreter threads which provides a new Perl interpreter for each thread,
and, by default, results in no data or state information being shared
between threads.

(Prior to Perl 5.8, 5005threads was available through the "Thread.pm" API.
This threading model has been deprecated, and was removed as of Perl 5.10.0.)

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# Optional tests:
Requires:       procps-ng
Requires:       perl(Thread::Queue)
Requires:       perl(Thread::Semaphore)
Requires:       perl(threads::shared)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n threads-%{base_version}
%patch -P0 -p1
%patch -P1 -p1
chmod -x examples/*

# Generate ppport.h
perl -MDevel::PPPort \
    -e "Devel::PPPort::WriteFile() or die 'Could not generate ppport.h: $!'"

# Help generators to recognize Perl scripts
for F in t/*.t; do
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
perl -i -ple "s{ '-Mblib' }{}" %{buildroot}%{_libexecdir}/%{name}/t/exit.t
perl -i -ple "s{ '-Mblib' }{}" %{buildroot}%{_libexecdir}/%{name}/t/thread.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
unset GIT_DIR PERL_BUILD_PACKAGING PERL_CORE PERL_RUNPERL_DEBUG \
    PERL5_ITHREADS_STACK_SIZE RUN_MAINTAINER_TESTS
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset GIT_DIR PERL_BUILD_PACKAGING PERL_CORE PERL_RUNPERL_DEBUG \
    PERL5_ITHREADS_STACK_SIZE RUN_MAINTAINER_TESTS
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes examples README
%{perl_vendorarch}/auto/threads*
%{perl_vendorarch}/threads*
%{_mandir}/man3/threads*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.43-521
- Prepare for Oreon 11 (RP1)
