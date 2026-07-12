%global source0_hash f768bca4f0963f122eea8449d6359d30bf1c86c3ef08ac0e45cb0e238166a064

# Enable Coro support via Perl XS Coro::Multicore module
%if 0%{?rhel}
%bcond_with perl_Coro_Multicore_enables_coro
%else
%bcond_without perl_Coro_Multicore_enables_coro
%endif

Name:           perl-Coro-Multicore
Version:        1.07
Release:        18%{?dist}
Summary:        Make Coro threads on multiple cores with specially supported modules
# COPYING:          GPL-1.0-or-later OR Artistic-1.0-Perl
# perlmulticore.h:  LicenseRef-Fedora-Public-Domain OR CC0-1.0
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (LicenseRef-Fedora-Public-Domain OR CC0-1.0)
URL:            https://metacpan.org/release/Coro-Multicore
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Coro-Multicore-%{version}.tar.gz
# Declare POD encoding, submitted to upstream,
# <http://lists.schmorp.de/pipermail/anyevent/2015q4/000780.html>
Patch0:         Coro-Multicore-0.02-Declare-POD-encoding.patch
# Fix build failure on Perl 5.26.1 with enabled treads, CPAN RT#124131,
# 1.05 provided a fix, but forgot to return a value from thread_proc().
# Keep the patch until upstream resolves it.
Patch1:         Coro-Multicore-1.04-Fix-passing-context.patch
BuildRequires:  coreutils
BuildRequires:  perl-podlators
%if %{with perl_Coro_Multicore_enables_coro}
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
BuildRequires:  perl(Canary::Stability)
BuildRequires:  perl(Coro::MakeMaker)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(AnyEvent) >= 7
BuildRequires:  perl(Carp)
BuildRequires:  perl(Coro) >= 6.44
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Coro::AnyEvent)
Requires:       perl(AnyEvent) >= 7
Requires:       perl(Carp)
Requires:       perl(Coro) >= 6.44

# Filter under-specified dependecies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((AnyEvent|Coro)\\)$
%else
%global debug_package %{nil}
%endif

%description
While Coro threads (unlike ithreads) provide real threads similar to
pthreads, python threads and so on, they do not run in parallel to each
other even on machines with multiple CPUs or multiple CPU cores.

This module lifts this restriction under two very specific but useful
conditions: firstly, the coro thread executes in XS code and does not
touch any perl data structures, and secondly, the XS code is specially
prepared to allow this.

# We package perlmulticore.h because it is bundled by perl-Compress-LZF-3.8.
# We deliver it from Coro-Multicore because perlmulticore.h's documentation
# points to Coro-Multicore CVS tree.
%package -n perlmulticore-devel
Summary:        Perl Multicore specification and implementation
License:        LicenseRef-Fedora-Public-Domain OR CC0-1.0
# Packaging guidelines require header-only packages:
# to be architecture-specific, to deliver headers in -devel package, to
# provide -static symbol for reverse build-requires.
Provides:       perlmulticore-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n perlmulticore-devel
This header file implements a simple mechanism for XS modules to allow
re-use of the perl interpreter for other threads while doing some lengthy
operation, such as cryptography, SQL queries, disk I/O and so on.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
%if %{with perl_Coro_Multicore_enables_coro}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Coro) >= 6.44
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n Coro-Multicore-%{version}

%build
%if %{with perl_Coro_Multicore_enables_coro}
export CORO_MULTICORE_CHECK=0 PERL_CANARY_STABILITY_NOPROMPT=1
perl Makefile.PL INSTALLDIRS=vendor \
    NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS" </dev/null
%{make_build}
%endif

# perlmulticore-devel:
pod2man perlmulticore.h >perlmulticore.h.3

%install
%if %{with perl_Coro_Multicore_enables_coro}
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%endif

# perlmulticore-devel:
install -d $RPM_BUILD_ROOT/%{_includedir}
install -m 0644 perlmulticore.h $RPM_BUILD_ROOT/%{_includedir}
install -d $RPM_BUILD_ROOT/%{_mandir}/man3
install -m 0644 perlmulticore.h.3 $RPM_BUILD_ROOT/%{_mandir}/man3

# Install tests
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
%if %{with perl_Coro_Multicore_enables_coro}
cp -a t $RPM_BUILD_ROOT%{_libexecdir}/%{name}
%endif
cat > $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
%if %{with perl_Coro_Multicore_enables_coro}
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%else
echo 'No upstream tests for perlmulticore-devel.'
%endif
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test

%check
%if %{with perl_Coro_Multicore_enables_coro}
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%endif

%if %{with perl_Coro_Multicore_enables_coro}
%files
%license COPYING
%doc Changes README
%dir %{perl_vendorarch}/auto/Coro
%{perl_vendorarch}/auto/Coro/Multicore
%dir %{perl_vendorarch}/Coro
%{perl_vendorarch}/Coro/Multicore.pm
%{_mandir}/man3/Coro::Multicore.3*
%endif

%files -n perlmulticore-devel
# COPYING file is about Perl module. Header files have a different license.
%{_includedir}/perlmulticore.h
%{_mandir}/man3/perlmulticore.h.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
