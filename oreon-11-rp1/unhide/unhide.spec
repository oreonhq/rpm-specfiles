%global source0_hash 72fb0f38450b71f80ca5331cff2b7b2024ffc9eb6178b6109bbd9638ccd4f771
%global srcname Unhide
Name:           unhide
Version:        20240510
Release:        3%{?dist}
Summary:        Tool to find hidden processes and TCP/UDP ports from rootkits
License:        GPL-3.0-or-later AND MIT
URL:            http://www.unhide-forensics.info/
Source0:        http://github.com/YJesus/%{srcname}/archive/v%{version}/%{srcname}-v%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
# /oreon:deps
%description
Unhide is a forensic tool to find hidden processes and TCP/UDP ports by 
rootkits/LKMs or by another hiding technique.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
chmod -x sanity*.sh

%build

%{__cc} %{optflags} -lpthread unhide-linux*.c unhide-output.c -o unhide %{?__global_ldflags}
%{__cc} %{optflags} unhide-tcp.c unhide-tcp-fast.c unhide-output.c -o unhide-tcp %{?__global_ldflags}
%{__cc} %{optflags} unhide_rb.c -o unhide_rb %{?__global_ldflags}
%install
mkdir -p %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_mandir}/es/man8/
mkdir -p %{buildroot}%{_mandir}/fr/man8/
install -pm0755 unhide %{buildroot}%{_sbindir}/
install -pm0755 unhide-tcp %{buildroot}%{_sbindir}/
install -pm0755 unhide_rb %{buildroot}%{_sbindir}/
install -pm0644 man/unhide.8 %{buildroot}%{_mandir}/man8/
install -pm0644 man/unhide-tcp.8 %{buildroot}%{_mandir}/man8/
install -pm0644 man/es/unhide.8 %{buildroot}%{_mandir}/es/man8
install -pm0644 man/es/unhide-tcp.8 %{buildroot}%{_mandir}/es/man8/
install -pm0644 man/fr/unhide.8 %{buildroot}%{_mandir}/fr/man8/
install -pm0644 man/fr/unhide-tcp.8 %{buildroot}%{_mandir}/fr/man8/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
