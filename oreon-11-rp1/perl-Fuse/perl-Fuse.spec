%global source0_hash 13a2e923f247781acb79259f4e57ee62aa392e36a6df110fa56e1970010d1127
%bcond_with testsuite
Name:           perl-Fuse
Version:        0.16.1
Release:        1%{?dist}
Summary:        Write filesystems in Perl using FUSE
License:        LGPL-2.1-only AND ( GPL-2.0-or-later OR LGPL-2.1-or-later )
URL:            https://metacpan.org/release/Fuse
Source0:        https://cpan.metacpan.org/authors/id/D/DP/DPATES/Fuse-%{version}.tar.gz
%if %{with testsuite}
%endif
Recommends:     perl(threads)
Recommends:     perl(threads::shared)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse)
# /oreon:deps
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
%oreon_autofiles main

%check

%if %{with testsuite}
make test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
