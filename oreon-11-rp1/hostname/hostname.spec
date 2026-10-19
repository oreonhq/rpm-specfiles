%global source1_hash edaef632cbb643e4e7a221717a6c441a4c1a7c918e6e4d56debc3d8739b233f6
%global source0_hash 5bb5d1be011158090157c9e7587ae5606c262a5020ecdc5caac6686b9910592e
Summary:        Utility to set/show the host name or domain name
Name: hostname
Version: 3.25
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://tracker.debian.org/pkg/hostname
Source0:        https://ftp.debian.org/debian/pool/main/h/hostname/hostname_%{version}.tar.xz
Source1: https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
Source2: nis-domainname
Source3: nis-domainname.service
Patch1: hostname-rh.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
This package provides commands which can be used to display the system's
DNS name, and to display or set its hostname or NIS domain name.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n hostname
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} .
%patch -P 1 -p1

%build

make CFLAGS="%{optflags} $CFLAGS -D_GNU_SOURCE" LDFLAGS="$RPM_LD_FLAGS"
%install
make DESTDIR=%{buildroot} install
install -m 0755 -d %{buildroot}%{_libexecdir}/%{name}
install -m 0755 -d %{buildroot}%{_prefix}/lib/systemd/system
install -m 0755 nis-domainname         %{buildroot}%{_libexecdir}/%{name}
install -m 0644 nis-domainname.service %{buildroot}%{_prefix}/lib/systemd/system
%oreon_autofiles main

%post

if [ $1 -eq 1 ]; then
  systemctl --no-reload preset nis-domainname.service &>/dev/null || :
fi
%preun

if [ $1 -eq 0 ]; then
  systemctl --no-reload disable --now nis-domainname.service &>/dev/null || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.25-1
- Prepare for Oreon 11 (RP1)
