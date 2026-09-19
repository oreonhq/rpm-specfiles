%global source0_hash 6fa5f27711ed7a00a0ccf1ffa0b9e2541e67c8e91451fc95e44c010de4443a6f

# help2man is too old on rhel <= 6 to support some switches.
%if 0%{?fedora} || 0%{?rhel} >= 7
%bcond_without	man
%else
%bcond_with	man
%endif

Name:		fstransform
Version:	0.9.4
Release:	18%{?dist}
Summary:	Tool for in-place file-system conversion without backup

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/cosmos72/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	e2fsprogs-devel
BuildRequires:	gcc-c++
BuildRequires:	libcom_err-devel
BuildRequires:	zlib-devel

%if %{with man}
BuildRequires:	help2man
%endif # with man
BuildRequires: make

Requires:	coreutils
Requires:	util-linux
Requires:	which

%description
fstransform is a tool to change a file-system from one format
to another, for example from jfs/xfs/reiser to ext2/ext3/ext4,
in-place and without the need for backup.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

# Make sure Autotools files have proper timestamps.
/bin/touch aclocal.m4 configure Makefile.am Makefile.in

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%if %{with man}
# Create man-pages.
%{__mkdir} -p %{buildroot}%{_mandir}/man8
for f in %{buildroot}%{_sbindir}/* ; do
	n="$(echo ${f} | %{__sed} -e 's!^%{buildroot}%{_sbindir}/!!g')"
	%{_bindir}/help2man -N -s 8 --version-string='%{version}'	\
		--no-discard-stderr -o %{buildroot}%{_mandir}/man8/${n}.8 ${f}
done
%endif # with man

%check
%make_build check

%files
%doc doc/*
%doc ChangeLog
%doc README
%doc TODO
%license AUTHORS
%license COPYING
%if %{with man}
%{_mandir}/man8/fsattr.8*
%{_mandir}/man8/fsmount_kernel.8*
%{_mandir}/man8/fsmove.8*
%{_mandir}/man8/fsremap.8*
%{_mandir}/man8/%{name}.8*
%endif # with man
%{_sbindir}/fsattr
%{_sbindir}/fsmount_kernel
%{_sbindir}/fsmove
%{_sbindir}/fsremap
%{_sbindir}/%{name}

%changelog
%autochangelog
