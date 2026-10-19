%global source0_hash f768bca4f0963f122eea8449d6359d30bf1c86c3ef08ac0e45cb0e238166a064
%bcond_without perl_Coro_Multicore_enables_coro
Name:           perl-Coro-Multicore
Version:        1.07
Release:        18%{?dist}
Summary:        Make Coro threads on multiple cores with specially supported modules
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (LicenseRef-Fedora-Public-Domain OR CC0-1.0)
URL:            https://metacpan.org/release/Coro-Multicore
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Coro-Multicore-%{version}.tar.gz
Patch0:         Coro-Multicore-0.02-Declare-POD-encoding.patch
Patch1:         Coro-Multicore-1.04-Fix-passing-context.patch
%if %{with perl_Coro_Multicore_enables_coro}
Requires:       perl(AnyEvent) >= 7
Requires:       perl(Carp)
Requires:       perl(Coro) >= 6.44
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((AnyEvent|Coro)\\)$
%else
%global debug_package %{nil}
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Canary::Stability)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Coro)
BuildRequires:  perl(Coro::AnyEvent)
BuildRequires:  perl(Coro::MakeMaker)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-podlators
# /oreon:deps
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
%global oreon_srcdir Coro-Multicore-%{version}
%oreon_prep
%build

%if %{with perl_Coro_Multicore_enables_coro}
export CORO_MULTICORE_CHECK=0 PERL_CANARY_STABILITY_NOPROMPT=1
perl Makefile.PL INSTALLDIRS=vendor \
    NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS" </dev/null
%{make_build}
%endif
pod2man perlmulticore.h >perlmulticore.h.3
%install
%if %{with perl_Coro_Multicore_enables_coro}
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%endif
install -d $RPM_BUILD_ROOT/%{_includedir}
install -m 0644 perlmulticore.h $RPM_BUILD_ROOT/%{_includedir}
install -d $RPM_BUILD_ROOT/%{_mandir}/man3
install -m 0644 perlmulticore.h.3 $RPM_BUILD_ROOT/%{_mandir}/man3
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
%if %{with perl_Coro_Multicore_enables_coro}
cp -a t $RPM_BUILD_ROOT%{_libexecdir}/%{name}
%endif
cat > $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test << 'EOF'
%if %{with perl_Coro_Multicore_enables_coro}
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%else
echo 'No upstream tests for perlmulticore-devel.'
%endif
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test
%oreon_autofiles perlmulticore-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with perl_Coro_Multicore_enables_coro}
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%endif
%if %{with perl_Coro_Multicore_enables_coro}
%files -f %{oreon_filedir}/main.list
%files -n perlmulticore-devel -f %{oreon_filedir}/perlmulticore-devel.list
%files -n perl-Coro-Multicore-tests -f %{oreon_filedir}/perl-Coro-Multicore-tests.list

%changelog

%autochangelog
%endif
