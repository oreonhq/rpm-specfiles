%global source0_hash ac18aa1ccb926c8acbf8093084547bf11feae90c19541eef21116bab81973108

Name:     ntfs-3g-system-compression
Summary:  NTFS-3G plugin for reading "system compressed" files
Version:  1.1
Release:  2%{?dist}
License:  GPL-2.0-or-later
URL:      https://github.com/ebiggers/ntfs-3g-system-compression
Source:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libntfs-3g) >= 2017.3.23
Supplements:    ntfs-3g

%description
System compression, also known as "Compact OS", is a Windows feature that
allows rarely modified files to be compressed using the XPRESS or LZX
compression formats. It is not built directly into NTFS but rather is
implemented using reparse points. This feature appeared in Windows 10 and it
appears that many Windows 10 systems have been using it by default.

This RPM contains a plugin which enables the NTFS-3G FUSE driver to
transparently read from system-compressed files. Currently, only reading is
supported. Compressing an existing file may be done by using the "compact"
utility on Windows.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
autoreconf -i
%configure

%build
%make_build

%install
%make_install
rm -rf %{buildroot}%{_libdir}/ntfs-3g/*.la

%files
%doc README.md
%license COPYING
%dir %{_libdir}/ntfs-3g/
%{_libdir}/ntfs-3g/ntfs-plugin-80000017.so

%changelog
%autochangelog
