%global source0_hash fd8f143f4e162d36c8ae29c51b32d315415447829c81091e3bb86b326051c77c

Name:		fatrace
Version:	0.19.1
Release:	%autorelease
Summary:	Reports file access events from all running processes

License:	GPL-3.0-or-later
URL:		https://github.com/martinpitt/fatrace
Source0:        https://github.com/martinpitt/fatrace/archive/refs/tags/%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: make

%description
fatrace reports file access events from all running processes.

Its main purpose is to find processes which keep waking up the disk
unnecessarily and thus prevent some power saving.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
export PREFIX=%{_prefix}
make install DESTDIR=%{buildroot}
# move /sbin to /bin
mv %{buildroot}%{_prefix}/sbin %{buildroot}%{_bindir}

%files
%doc COPYING
%{_bindir}/fatrace
%{_bindir}/power-usage-report
%{_mandir}/man*/*

%changelog
%autochangelog
