%global source0_hash 72fb0f38450b71f80ca5331cff2b7b2024ffc9eb6178b6109bbd9638ccd4f771

%global srcname Unhide
Name:           unhide
Version:        20240510
Release:        3%{?dist}
Summary:        Tool to find hidden processes and TCP/UDP ports from rootkits

# GPL-3.0-or-later
#  unhide-20240510-build/Unhide-20240510/COPYING
#  unhide-20240510-build/Unhide-20240510/LEEME.txt
#  unhide-20240510-build/Unhide-20240510/LICENSE
#  unhide-20240510-build/Unhide-20240510/LISEZ-MOI.TXT
#  unhide-20240510-build/Unhide-20240510/NEWS
#  unhide-20240510-build/Unhide-20240510/README.txt
#  unhide-20240510-build/Unhide-20240510/TODO
#  unhide-20240510-build/Unhide-20240510/build_all.sh
#  unhide-20240510-build/Unhide-20240510/changelog
#  unhide-20240510-build/Unhide-20240510/make_tarball.sh
#  unhide-20240510-build/Unhide-20240510/man/es/unhide-tcp.8
#  unhide-20240510-build/Unhide-20240510/man/es/unhide.8
#  unhide-20240510-build/Unhide-20240510/man/fr/unhide-tcp.8
#  unhide-20240510-build/Unhide-20240510/man/fr/unhide.8
#  unhide-20240510-build/Unhide-20240510/man/unhide-tcp.8
#  unhide-20240510-build/Unhide-20240510/man/unhide.8
#  unhide-20240510-build/Unhide-20240510/ps
#  unhide-20240510-build/Unhide-20240510/sanity-tcp.sh
#  unhide-20240510-build/Unhide-20240510/sanity.sh
#  unhide-20240510-build/Unhide-20240510/ss
#  unhide-20240510-build/Unhide-20240510/ss-ref
#  unhide-20240510-build/Unhide-20240510/tar_list.txt
#  unhide-20240510-build/Unhide-20240510/unhide-linux-bruteforce.c
#  unhide-20240510-build/Unhide-20240510/unhide-linux-compound.c
#  unhide-20240510-build/Unhide-20240510/unhide-linux-procfs.c
#  unhide-20240510-build/Unhide-20240510/unhide-linux-syscall.c
#  unhide-20240510-build/Unhide-20240510/unhide-linux.c
#  unhide-20240510-build/Unhide-20240510/unhide-linux.h
#  unhide-20240510-build/Unhide-20240510/unhide-output.c
#  unhide-20240510-build/Unhide-20240510/unhide-output.h
#  unhide-20240510-build/Unhide-20240510/unhide-posix.c
#  unhide-20240510-build/Unhide-20240510/unhide-tcp-fast.c
#  unhide-20240510-build/Unhide-20240510/unhide-tcp.c
#  unhide-20240510-build/Unhide-20240510/unhide-tcp.h
#  unhide-20240510-build/Unhide-20240510/unhideGui.py
#  unhide-20240510-build/Unhide-20240510/unhide_rb.c
# MIT
#  unhide-20240510-build/Unhide-20240510/ToolTip.py
License:        GPL-3.0-or-later AND MIT
URL:            http://www.unhide-forensics.info/
Source0:        http://github.com/YJesus/%{srcname}/archive/v%{version}/%{srcname}-v%{version}.tar.gz

BuildRequires: gcc

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

%files
%doc changelog README.txt NEWS sanity.sh sanity-tcp.sh
%license COPYING LICENSE
%{_mandir}/man8/unhide*.8*
%{_mandir}/es/man8/unhide*.8*
%{_mandir}/fr/man8/unhide*.8*
%{_sbindir}/unhide
%{_sbindir}/unhide-tcp
%{_sbindir}/unhide_rb

%changelog
%autochangelog
