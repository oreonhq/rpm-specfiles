%global source1_hash a54bf0696d74518534233292d6f362265c6bdfd6f1f392dfff62192a1e72672a
%global source0_hash 57f5457f72999d0bb1a139a37f2746ec1b5a02c094f2710a339d8bcea4236123
Summary:        GLib Ncurses Toolkit
Name:		libgnt
Version:	2.14.3
Release:        1%{?dist}
License:	GPL-2.0-or-later
URL:		https://keep.imfreedom.org/libgnt/libgnt/
Source0:        https://sourceforge.net/projects/pidgin/files/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:	https://sourceforge.net/projects/pidgin/files/%{name}-%{version}.tar.xz.asc
Source2:	libgnt-maintainers-keyring.asc
Patch0:		libgnt-2.14.1-gcc-14-fix.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  gobject-introspection
BuildRequires:  gtk-doc
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  ncurses-devel
BuildRequires:  ninja-build
BuildRequires:  python3-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libgnt-devel -f %{oreon_filedir}/libgnt-devel.list
%files -n libgnt-doc -f %{oreon_filedir}/libgnt-doc.list

%changelog

%autochangelog
