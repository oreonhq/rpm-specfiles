%global source0_hash 08c4a2dc459607c7bef686c28491908d68290c0955a55dabaed100c33767fe6d
%global version_no_dot 27
Name:           c2esp
Version:        2.7
Release:        37%{?dist}
Summary:        CUPS driver for Kodak AiO printers
License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/cupsdriverkodak/
Source0:        https://downloads.sourceforge.net/cupsdriverkodak/c2esp-27.tar.gz
Patch01: c2esp-ftbfs-gcc7.patch
Patch02: c2esp-gcc10.patch
Patch03: c2esp-c99.patch
Patch04: c2esp-use-libcupsfilters.patch
Requires: cups-filesystem
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cups-devel
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  jbigkit-devel
BuildRequires:  libcupsfilters-devel
BuildRequires:  libppd-devel
BuildRequires:  make
BuildRequires:  python3-cups
# /oreon:deps
%description
CUPS filters and drivers for Kodak ESP and Hero all in one printers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n c2esp-%{version_no_dot} -S git

%build

autoreconf -vfi
%configure
make %{_smp_mflags} -C src/
%install
make -C src/ install DESTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.7-37
- Prepare for Oreon 11 (RP1)
