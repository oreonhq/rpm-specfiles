%global source0_hash dabc6330937a95fb2707dbd9f52e5a30fce04bd6b413d6ab92079226692346ba
%global debug_package %{nil}
Name:		unetbootin
Version:	702
Release:        12%{?dist}
Summary:        Create bootable Live USB drives for a variety of Linux distributions
License:	GPL-2.0-or-later
URL:		https://unetbootin.github.io/
Source0:        https://sourceforge.net/projects/%{name}/files/UNetbootin/%{version}/%{name}-source-%{version}.tar.gz
Patch0:     unetbootin-675-desktop.patch
ExclusiveArch:	%{ix86} x86_64
Requires:	p7zip-plugins
Requires:	syslinux
Requires:	syslinux-extlinux
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
UNetbootin allows you to create bootable Live USB drives for a variety of
Linux distributions from Windows or Linux, without requiring you to burn a CD.
You can either let it download one of the many distributions supported
out-of-the-box for you, or supply your own Linux .iso file if you've already
downloaded one or your preferred distribution isn't on the list.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c
%patch -P0 -p1
# Fix desktop file
sed -i '/^RESOURCES/d' unetbootin.pro

%build

lupdate-qt5 unetbootin.pro
lrelease-qt5 unetbootin.pro
%{?qmake_qt5}%{!?qmake_qt5:qmake-qt5}}
%make_build
%install
install -D -p -m 755 unetbootin %{buildroot}%{_bindir}/unetbootin
desktop-file-install --vendor="" --remove-category=Application --dir=%{buildroot}%{_datadir}/applications unetbootin.desktop
install -d %{buildroot}%{_datadir}/unetbootin
install -c -p -m 644 unetbootin_*.qm %{buildroot}%{_datadir}/unetbootin/
install -D -p -m 644 unetbootin_512.png %{buildroot}%{_datadir}/pixmaps/unetbootin.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
