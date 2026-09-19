%global source0_hash 45e09fb014bd28ab6181a383fbb74f2979a46b1d8ce8752389a7dc543f287c7c

Summary:	A WBFS manager for Linux using GTK+
Name:		wbfs-manager
Version:	0.1.12
Release:	32%{?dist}
License:	GPL-2.0-only
Url:		http://code.google.com/p/linux-wbfs-manager/
Source0:	http://linux-wbfs-manager.googlecode.com/files/linux-wbfs-manager-%{version}.tar.gz
Source1:	wbfs-gtk.desktop
Patch1:		wbfs-manager.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	libglade2-devel desktop-file-utils

%description
This is yet another graphic WBFS (Wii Backup File System) manager 
for Linux. It uses libwbfs from Kwiirk and caristat 
(available from the authors at 
http://github.com/kwiirk/wbfs/tree/master). 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n linux-%{name}
%patch -P1 -p1

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}/
cp -p wbfs_gtk %{buildroot}%{_bindir}/
desktop-file-install \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
%{SOURCE1}

%files
%{_bindir}/wbfs_gtk
%{_datadir}/applications/wbfs-gtk.desktop

%changelog
%autochangelog
