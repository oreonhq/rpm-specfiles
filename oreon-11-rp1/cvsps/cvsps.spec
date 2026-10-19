%global source0_hash 6906acb3636cdb4a4a9d608111aec22a85530037cb08a62ed5eb74ca0b218f81
%global prever  b1
Name:           cvsps
Version:        2.2
Release:        1%{?dist}
Summary:        Patchset tool for CVS
License:        GPL-1.0-or-later
URL:            https://sourceforge.net/projects/cvsps/
Source0:        https://downloads.sourceforge.net/project/%{name}/%{name}-%{version}%{prever}.tar.gz
Patch0:         %{name}-2.2b1-dynamic-logbuf.patch
Patch1:         %{name}-2.2b1-man.patch
Patch2:         %{name}-2.2b1-bufferoverflow.patch
Requires: cvs
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
CVSps is a program for generating 'patchset' information from a CVS
repository.  A patchset in this case is defined as a set of changes
made to a collection of files, and all committed at the same time
(using a single 'cvs commit' command).  This information is valuable
to seeing the big picture of the evolution of a cvs project.  While
cvs tracks revision information, it is often difficult to see what
changes were committed 'atomically' to the repository.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{prever}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build

CFLAGS="$RPM_OPT_FLAGS -DLINUX" make %{?_smp_mflags}
%install
make install prefix=$RPM_BUILD_ROOT%{_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

