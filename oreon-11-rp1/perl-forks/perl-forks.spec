%global source0_hash 61be24e44f4c6fea230e8354678beb5b7adcfefd909a47db8f0a251b0ab65993
Name:           perl-forks
Version:        0.36
Release:        1%{?dist}
Summary:        A drop-in replacement for Perl threads using fork()
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/forks
Source0:        https://cpan.metacpan.org/authors/id/R/RY/RYBSKEJ/forks-%{version}.tar.gz
Requires:       perl(IO::Socket) >= 1.18
Requires:       perl(List::MoreUtils) >= 0.15
Requires:       perl(Scalar::Util) >= 1.11
Requires:       perl(sigtrap)
Requires:       perl(Sys::SigAction) >= 0.11
Provides:       perl(forks::Devel::Symdump) = %{version}
Provides:       perl(forks::signals) = %{version}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((IO::Socket|List::MoreUtils|Scalar::Util|Sys::SigAction)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Acme::Damn)
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MM_Any)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::SigAction)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(sigtrap)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The forks.pm module is a drop-in replacement for threads.pm.  It has the
same syntax as the threads.pm module (it even takes over its name space) but
has some significant differences:

- you do _not_ need a special (threaded) version of Perl
- it is _much_ more economic with memory usage on OS's that support COW
- it is more efficient in the start-up of threads
- it is slightly less efficient in the stopping of threads
- it is less efficient in inter-thread communication

If for nothing else, it allows you to use the Perl threading model in
non-threaded Perl builds and in older versions of Perl (5.6.0 and
higher are supported).

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(if)
Requires:       perl(lib)
Requires:       perl(List::MoreUtils) >= 0.15
Requires:       perl(Sys::SigAction) >= 0.11
Requires:       perl(Thread::Queue)
Requires:       perl(threads)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n forks-%{version}
# Remove always skipped tests
rm t/forks99.t
perl -i -ne 'print $_ unless m{^t/forks99\.t}' MANIFEST
# Correct permissions
find . -type f -exec chmod a-x {} +
# Correct shebangs
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

unset FORKS_SIMULATE_USEITHREADS PERL_MM_USE_DEFAULT 
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find "$RPM_BUILD_ROOT" -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} "$RPM_BUILD_ROOT"/*
mkdir -p "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
cp -a t "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
cat > "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test << 'EOF'
unset PERL_CORE PERL5_ITHREADS_STACK_SIZE THREADS_DAEMON_MODEL \
    THREADS_IP_MASK THREADS_NATIVE_EMULATION THREADS_NICE \
    THREADS_NO_PRELOAD_SHARED THREADS_SIGCHLD_IGNORE THREADS_SOCKET_UNIX
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset PERL_CORE PERL5_ITHREADS_STACK_SIZE THREADS_DAEMON_MODEL \
    THREADS_IP_MASK THREADS_NATIVE_EMULATION THREADS_NICE \
    THREADS_NO_PRELOAD_SHARED THREADS_SIGCHLD_IGNORE THREADS_SOCKET_UNIX
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-forks-tests -f %{oreon_filedir}/perl-forks-tests.list

%changelog

%autochangelog
