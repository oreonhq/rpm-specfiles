%global source0_hash 52730bcd1cf16bd4dae0de42531be9a4057535ec61ca38c0804eb8246ea6c41b

Summary: Ncurses based hexadecimal editor with a diff mode
Name: dhex
Version: 0.69
Release: 19%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.dettus.net/dhex/
Source: http://www.dettus.net/dhex/%{name}_%{version}.tar.gz
Patch: dhex-0.69-build-fix.patch
# Sent upstream
Patch: dhex-0.69-gcc-15-fix.patch
BuildRequires: gcc, ncurses-devel
BuildRequires: make

%description
DHEX is a more than just another hex editor: It includes a diff mode, which
can be used to easily and conveniently compare two binary files. Since it is
based on ncurses and is themeable, it can run on any number of systems and
scenarios. With its utilization of search logs, it is possible to track
changes in different iterations of files easily.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}_%{version}

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" %{?__global_ldflags: LDFLAGS="%{__global_ldflags}"}

%install
install -dD %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man{1,5}
make %{?_smp_mflags} DESTDIR=%{buildroot} BINDIR=%{_bindir} \
     MANDIR=%{_mandir} install

%files
%doc README.txt gpl.txt todo.txt

%{_bindir}/*
%{_mandir}/*/*

%changelog
%autochangelog
