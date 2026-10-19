%global source0_hash ababeebbc34135a1fdd82e5d0fccd8464e0fa74f3b96e99d24efd7462a3ceb17
Name:           toolshed
Version:        20220204hga1b3c7faf452
Release:        6%{?dist}
Summary:        Cross-development toolkit for use with the Tandy Color Computer
License:        Public Domain
URL:            http://sourceforge.net/projects/toolshed/
Source0:        %{name}-%{version}-noroms.tar.gz
Source1: generate-tarball.sh
Patch0: toolshed-version-stringify.patch
Patch1: toolshed-OS9AttrToString-param.patch
# oreon:deps
BuildRequires:  discount
BuildRequires:  fuse-devel
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
ToolShed is a package of utilities to perform cross-development from
Windows, Linux or Mac OS X computers to the Tandy Color Computer and
Dragon microcomputers. Tools are included to read/write both OS-9 RBF
disk images and CoCo Disk BASIC disk images, create WAV and CAS files
and much more.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p1
%patch -P1 -p1

# Turn-off weird doc permissions...
chmod 0644 doc/*

%build

make %{?_smp_mflags} CFLAGS="%{optflags} \
	-fPIE -DSYSV -Dunix -DUNIX -DSYSV -O3 -I. -I../../../include -Wall \
	-DTOOLSHED_VERSION=2.2 -D_FILE_OFFSET_BITS=64 -Wno-unused-result -Werror" \
        -C build/unix
%install
mkdir -p %{buildroot}%{_bindir}
make %{?_smp_mflags} -C build/unix install INSTALLDIR=%{buildroot}%{_bindir} DOCDIR=%{buildroot}%{_docdir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
