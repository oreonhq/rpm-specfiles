%global source0_hash f2ac2444a74e762783bbd36c486352f96340434d34ae7926d6ab234966540f49

Name:           perl-Linux-Pid
Version:        0.04
Release:        61%{?dist}
Summary:        Get the native PID and the PPID on Linux 
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Linux-Pid
Source0:        https://cpan.metacpan.org/modules/by-module/Linux/Linux-Pid-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
# Carp not used at tests
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Config)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
Requires:       perl(Carp)

%{?perl_default_filter}

Provides:       perl(Linux::Pid)
%description
Linux::Pid gets the native PID and the PPID on Linux. It's useful with
multithreaded programs. Linux's C library returns different values of
the PID and the PPID from different threads. This module forces Perl
to call the underlying C functions getpid() and getppid().


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Linux-Pid-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%files
%doc README Changes
%{perl_vendorarch}/auto/Linux
%{perl_vendorarch}/Linux
%{_mandir}/man3/Linux::Pid.3pm.gz


%changelog
%autochangelog
