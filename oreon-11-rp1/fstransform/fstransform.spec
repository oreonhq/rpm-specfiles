%global source0_hash 6fa5f27711ed7a00a0ccf1ffa0b9e2541e67c8e91451fc95e44c010de4443a6f
%bcond_with	man
Name:		fstransform
Version:	0.9.4
Release:        1%{?dist}
Summary:        Tool for in-place file-system conversion without backup
License:	GPL-3.0-or-later
URL:		https://github.com/cosmos72/%{name}
Source0:        https://github.com/cosmos72/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if %{with man}
%endif # with man
Requires:	coreutils
Requires:	util-linux
Requires:	which
# oreon:deps
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libcom_err-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
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
%{__mkdir} -p %{buildroot}%{_mandir}/man8
for f in %{buildroot}%{_sbindir}/* ; do
	n="$(echo ${f} | %{__sed} -e 's!^%{buildroot}%{_sbindir}/!!g')"
	%{_bindir}/help2man -N -s 8 --version-string='%{version}'	\
		--no-discard-stderr -o %{buildroot}%{_mandir}/man8/${n}.8 ${f}
done
%oreon_autofiles main
%endif # with man
%check

%make_build check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
