%global source0_hash 5202b89be915cd24ebdc3021c7159b587050c4dc3eb9de2eb599d098b16e54df

Name:       debmirror
Version:    2.47
Release:    %autorelease
Summary:    Debian partial mirror script, with ftp and package pool support
License:    GPL-2.0-or-later
URL:        https://tracker.debian.org/pkg/debmirror
BuildArch:  noarch

Source:     https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
Patch0:     %{name}-no-root.patch

BuildRequires: perl
BuildRequires: perl-generators
BuildRequires: perl-podlators

Requires:   bzip2
Requires:   coreutils
Requires:   ed
Requires:   findutils
Requires:   gnupg
Requires:   gzip
Requires:   patch
Requires:   rsync

%description
This program downloads and maintains a partial local Debian mirror.
It can mirror any combination of architectures, distributions and sections.
Files are transferred by ftp, http, hftp or rsync, and package pools are fully
supported. It also does locking and updates trace files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n work

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 examples/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf

# generate a man page
install -d %{buildroot}%{_mandir}/man1
pod2man %{name} %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license GPL debian/copyright
%doc debian/changelog debian/NEWS doc/design.txt
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
%autochangelog
