%global source0_hash 1928e48033540e11ebf5506986dd101af78d2421d210f96599223b15d51714c6

%global cpan_version 6.57
Name:           perl-Coro
Version:        6.570
Release:        24%{?dist}
Summary:        The only real threads in perl
# Coro/libcoro:    GPL-2.0-or-later OR BSD-2-Clause
# Rest of package: GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (GPL-2.0-or-later OR BSD-2-Clause)
URL:            https://metacpan.org/release/Coro
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Coro-%{cpan_version}.tar.gz
Patch0:         %{name}-5.25-ucontext-default.patch
# Do not disable hardening
Patch1:         Coro-6.512-Disable-disabling-FORTIFY_SOURCE.patch
# https://rt.cpan.org/Public/Bug/Display.html?id=158609, https://bugzilla.redhat.com/show_bug.cgi?id=2379448
Patch2:         Coro-6.57-c23.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libecb-static
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Canary::Stability)
BuildRequires:  perl(Config)
BuildRequires:  perl(EV) >= 4
BuildRequires:  perl(EV::MakeMaker)
BuildRequires:  perl(Event) >= 1.08
BuildRequires:  perl(Event::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:  perl(strict)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(AnyEvent) >= 7
# AnyEvent::AIO >= 1 not used at tests
# AnyEvent::BDB >= 1 not used at tests
# AnyEvent::DNS not used at tests
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(AnyEvent::Util)
BuildRequires:  perl(base)
# BDB not used at tests
BuildRequires:  perl(Carp)
BuildRequires:  perl(common::sense)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Guard) >= 0.5
# IO::AIO >= 3.1 not used at tests
BuildRequires:  perl(IO::Socket::INET)
# Net::Config not used at tests
# Net::FTP not used at tests
# Net::HTTP not used at tests
# Net::NNTP not used at tests
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable) >= 2.15
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Export correct required versions
Requires:       perl(AnyEvent) >= 7
Requires:       perl(AnyEvent::AIO) >= 1
Requires:       perl(AnyEvent::BDB) >= 1
Requires:       perl(EV) >= 4
Requires:       perl(Event) >= 1.08
Requires:       perl(Guard) >= 0.5
Requires:       perl(Storable) >= 2.15
Requires:       perl(warnings)

%{?perl_default_filter}

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(AnyEvent\\)$
%global __requires_exclude %__requires_exclude|^perl\\(AnyEvent\\) >= 4.800001$
%global __requires_exclude %__requires_exclude|^perl\\(AnyEvent::AIO\\)$
%global __requires_exclude %__requires_exclude|^perl\\(AnyEvent::BDB\\)$
%global __requires_exclude %__requires_exclude|^perl\\(EV\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Event\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Guard\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Storable\\)$
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(Coro\\)$


Provides:       perl(Coro)
Provides:       perl(Coro) = %{version}
Provides:       perl(Coro::MakeMaker)
Provides:       perl(Coro::AnyEvent)
Provides:       perl(Coro::AIO)
Provides:       perl(Coro::BDB)
Provides:       perl(Coro::Channel)
Provides:       perl(Coro::Debug)
Provides:       perl(Coro::Handle)
Provides:       perl(Coro::LWP)
Provides:       perl(Coro::RWLock)
Provides:       perl(Coro::Select)
Provides:       perl(Coro::Semaphore)
Provides:       perl(Coro::SemaphoreSet)
Provides:       perl(Coro::Signal)
Provides:       perl(Coro::Socket)
Provides:       perl(Coro::Specific)
Provides:       perl(Coro::State)
Provides:       perl(Coro::Storable)
Provides:       perl(Coro::Timer)
Provides:       perl(Coro::Util)
%description
This module collection manages continuations in general, most often in the
form of cooperative threads (also called coros, or simply "coro" in the
documentation). They are similar to kernel threads but don't (in general) run
in parallel at the same time even on SMP machines. The specific flavor of
thread offered by this module also guarantees you that it will not switch
between threads unless necessary, at easily-identified points in your
program, so locking and parallel access are rarely an issue, making thread
programming much safer and easier than using other thread models.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Coro-%{cpan_version}

%ifnarch %{ix86} x86_64 %{arm}
# use ucontext backend on non-x86 (setjmp didn't work on s390(x))
%patch -P0 -p1 -b .ucontext-default
%endif
%patch -P1 -p1
%patch -P2 -p1

# Unbundle libecb
rm Coro/ecb.h
perl -i -lne 'print $_ unless m{\ACoro/ecb\.h\z}' MANIFEST
perl -i -pe 's/ecb\.h//' Coro/Makefile.PL

# Correct shebangs
for F in Coro/jit-*.pl; do
    perl -i -ne 'print $_ unless m{\A#!}' "$F"
    chmod -x "$F"
done
%fix_shbang_line eg/myhttpd

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
# Interactive configuration. Use default values.
perl Makefile.PL INSTALLDIRS=perl NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="$RPM_OPT_FLAGS" </dev/null
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%license COPYING
%doc Changes README README.linux-glibc
%doc doc/* eg
%{perl_archlib}/auto/Coro
%{perl_archlib}/Coro
%{perl_archlib}/Coro.pm
%{_mandir}/man3/Coro*.3pm*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
