%global source0_hash 56ab67b1b6ede27aefb93cc1041443feac7f2e54cbabeed20b56fc97dd678825

Name:		topline
Version:	0.6
Release:	6%{?dist}
Summary:	Per-core/NUMA CPU and disk utilization plain-text grapher
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/kilobyte/topline
Source0:	https://github.com/kilobyte/topline/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	gcc

%description
This is a top-of-the-line logger of CPU usage patterns, designed for
machines with ca. 50-300 total hardware threads (fewer works but results
in a narrow graph, more requires a very wide terminal).  Every per-tick
sample is shown abusing Unicode characters to fit within a single line.

Disk usage is also shown in a similarly terse per-device way, as %%
utilization for reads and writes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make %{?_smp_mflags} CFLAGS="$CFLAGS" CPPFLAGS="$CPPFLAGS" LDFLAGS="$LDFLAGS"

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install topline %{buildroot}%{_bindir}
cp -p topline.1* %{buildroot}%{_mandir}/man1

%files
%{_bindir}/topline
%{_mandir}/man1/topline.1*
%license LICENSE
%doc README.md

%changelog
%autochangelog
