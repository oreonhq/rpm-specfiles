%global source0_hash 8bedc0660dde2e0e349196b982108dc4fa65c456bf442af5c30c956f05f9e3a1
Name:		fs_mark
Version:	3.3
Release:        1%{?dist}
Summary:        Benchmark synchronous/async file creation
License:	GPL-2.0-or-later
URL:		http://sourceforge.net/projects/fsmark/
Source0:        http://downloads.sourceforge.net/fsmark/%{name}.tgz
Patch0:		nostatic
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The fs_mark program is meant to give a low level bashing to file
systems. The write pattern that we concentrate on is heavily
synchronous IO across mutiple directories, drives, etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n fs_mark
%patch -P0 -p1 

%build

CFLAGS="$RPM_OPT_FLAGS" make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
install -D fs_mark $RPM_BUILD_ROOT/usr/bin/fs_mark
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
