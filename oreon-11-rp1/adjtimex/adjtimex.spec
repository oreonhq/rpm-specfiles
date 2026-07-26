%global source0_hash 04b9e8b66e77276ed07e78de89af37fd1aa12725923de853480827c4fafd176a

Summary: A utility for adjusting kernel time variables
Name: adjtimex
Version: 1.29
Release: 36%{?dist}
License: GPL-2.0-or-later
Source: http://ftp.debian.org/debian/pool/main/a/adjtimex/%{name}_%{version}.orig.tar.gz
Patch1: adjtimex-manopts.patch
Patch2: adjtimex-decl.patch
BuildRequires: gcc
BuildRequires: make

%description
Adjtimex provides raw access to kernel time variables. On standalone
or intermittently connected machines, root can use adjtimex to correct
for systematic drift. If your machine is connected to the Internet or
is equipped with a precision oscillator or radio clock, you should
instead manage the system clock with the xntpd program. Users can use
adjtimex to view kernel time variables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .manopts
%patch -P2 -p1 -b .decl

%build
%configure
make %{?_smp_mflags} VERSION=%{version}

%install
mkdir -p ${RPM_BUILD_ROOT}{%{_sbindir},%{_mandir}/man8}
install -m755 adjtimex ${RPM_BUILD_ROOT}%{_sbindir}/adjtimex
install -m644 adjtimex.8 ${RPM_BUILD_ROOT}%{_mandir}/man8/adjtimex.8

%files
%license COPYING
%doc README COPYRIGHT ChangeLog
%{_sbindir}/adjtimex
%{_mandir}/man8/adjtimex.8*

%changelog
%autochangelog
