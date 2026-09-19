%global source0_hash 57f5457f72999d0bb1a139a37f2746ec1b5a02c094f2710a339d8bcea4236123

Summary:	GLib Ncurses Toolkit
Name:		libgnt
Version:	2.14.3
Release:	2%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://keep.imfreedom.org/libgnt/libgnt/
BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	ninja-build
BuildRequires:	gobject-introspection
BuildRequires:	gtk-doc
BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	python3-devel
BuildRequires:	gnupg2
Source0:	https://sourceforge.net/projects/pidgin/files/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:	https://sourceforge.net/projects/pidgin/files/%{name}-%{version}.tar.xz.asc
# https://issues.imfreedom.org/issue/LIBGNT-10
Source2:	libgnt-maintainers-keyring.asc
# https://keep.imfreedom.org/libgnt/libgnt/rev/2da723f790d6
Patch0:		libgnt-2.14.1-gcc-14-fix.patch

%description
GNT is an ncurses toolkit for creating text-mode graphical user interfaces
in a fast and easy way. It is based on GLib and ncurses.

%package devel
Summary:	Developmentfiles for libgnt
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libgnt.

%package doc
Summary:	Documentation for libgnt

%description doc
Documentation files for libgnt.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson -Dpython2=false
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_libdir}/libgnt.so.*
%{_libdir}/gnt

%files devel
%{_libdir}/libgnt.so
%{_libdir}/pkgconfig/gnt.pc
%{_includedir}/gnt

%files doc
%{_datadir}/gtk-doc

%changelog
%autochangelog
