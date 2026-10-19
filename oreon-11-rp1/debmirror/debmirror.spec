%global source0_hash b45481099db4d81b514dd4a946f2cfba446168e2c896c5e0da09752ebfa93994
Name:       debmirror
Version:    2.49.git
Release:        1%{?dist}
Summary:        Debian partial mirror script, with ftp and package pool support
License:    GPL-2.0-or-later
URL:        https://tracker.debian.org/pkg/debmirror
BuildArch:  noarch
Source0:        https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
Patch0:     %{name}-no-root.patch
Requires:   bzip2
Requires:   coreutils
Requires:   ed
Requires:   findutils
Requires:   gnupg
Requires:   gzip
Requires:   patch
Requires:   rsync
# oreon:deps
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
# /oreon:deps
%description
This program downloads and maintains a partial local Debian mirror.
It can mirror any combination of architectures, distributions and sections.
Files are transferred by ftp, http, hftp or rsync, and package pools are fully
supported. It also does locking and updates trace files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir work
%oreon_prep
%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 examples/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf
install -d %{buildroot}%{_mandir}/man1
pod2man %{name} %{buildroot}%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
