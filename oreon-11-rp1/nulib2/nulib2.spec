%global source0_hash 383127d6966edae09da550f4d7197e68eed101d239f2a23cee42dc086506af12

Name:		nulib2
Version:	3.1.0
Release:	21%{?dist}
Summary:	Disk and file archive program for NuFX (.SDK, .BXY) archives
License:	BSD-3-Clause
URL:		http://nulib.com/
Source0:	https://github.com/fadden/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: nulib2-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc
%description
NuLib2 is a command-line file archiver for Apple II archives. It can operate
on ShrinkIt and Binary II files (.shk, .sdk, .bxy, .bse, .bny, .bqy).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
cd nufxlib
%configure
# following make fails if smp_mflags used
make
cd ../nulib2
%configure
make %{?_smp_mflags}

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 nulib2/nulib2 %{buildroot}%{_bindir}
install -d -m0755 %{buildroot}%{_mandir}/man1
install -p -m0644 nulib2/nulib2.1 %{buildroot}%{_mandir}/man1

%files
%license nulib2/COPYING
%{_bindir}/nulib2
%{_mandir}/man1/nulib2.1*

%changelog
%autochangelog
