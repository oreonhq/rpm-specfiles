%global source0_hash 13a2e923f247781acb79259f4e57ee62aa392e36a6df110fa56e1970010d1127

# The tests don't work in mock, they can be run on local machine
%bcond_with testsuite

Name:           perl-Fuse
Version:        0.16.1
Release:        33%{?dist}
Summary:        Write filesystems in Perl using FUSE
# LGPL-2.1-only: Reference from metadata
# (GPL-2.0-or-later OR LGPL-2.1-or-later): same license as fuse as mention in README
License:        LGPL-2.1-only AND ( GPL-2.0-or-later OR LGPL-2.1-or-later )
URL:            https://metacpan.org/release/Fuse
Source0:        https://cpan.metacpan.org/authors/id/D/DP/DPATES/Fuse-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(POSIX)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse)
%if %{with testsuite}
# Run-time
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  fuse
BuildRequires:  perl(blib)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  util-linux
# Optional test
BuildRequires:  perl(Filesys::Statvfs)
BuildRequires:  perl(Lchown)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(Unix::Mknod)
%endif
Recommends:     perl(threads)
Recommends:     perl(threads::shared)

%description
This lets you implement filesystems in perl, through the FUSE (Filesystem
in USErspace) kernel/lib interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Fuse-%{version}
find -type f -exec chmod -c a-x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if %{with testsuite}
make test
%endif

%files
%doc AUTHORS examples Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Fuse*
%{_mandir}/man3/*

%changelog
%autochangelog
