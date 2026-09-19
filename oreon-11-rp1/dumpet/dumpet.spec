%global source0_hash 2cc1fa3a1b06f885e4524d1be80bdacc5b6a55057d0577262f2f5186b49a4da3

Name:           dumpet
Version:        2.1
Release:        34%{?dist} 
Summary:        A tool to dump and debug bootable CD images
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://fedorahosted.org/dumpet/
BuildRequires:  gcc
BuildRequires:  popt-devel pkgconfig libxml2-devel git
BuildRequires: make

Source0:        https://fedorahosted.org/releases/d/u/dumpet/dumpet-%{version}.tar.bz2
Patch0001: 0001-Manually-tell-it-we-ve-got-64-bit-files-because-32-b.patch

%description
DumpET is a utility to aid in the debugging of bootable CD-ROM images.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
git init
git config user.email "%{name}-owner@fedoraproject.org"
git config user.name "Fedora Ninjas"
git add .
git commit -a -q -m "%{version} baseline."
git am %{patches} </dev/null

%build
make %{?_smp_mflags} CFLAGS="%{optflags} $(pkg-config --cflags libxml-2.0)"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
make DESTDIR=%{buildroot} install

%files
%doc README TODO COPYING
%attr(644,root,root) %{_mandir}/man1/dumpet.1*
%{_bindir}/dumpet

%changelog
%autochangelog
