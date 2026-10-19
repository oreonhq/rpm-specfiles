%global source0_hash 0869c81d19ab139c667d79567c14ddcb6cb5cbfc0108d04cade287eb29536706
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           grilo
Version:        0.3.19
Release:        1%{?dist}
Summary:        Content discovery framework
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/Grilo
Source0:        https://download.gnome.org/sources/%{name}/%{release_version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  libsoup3-devel
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  totem-pl-parser-devel
BuildRequires:  vala
# /oreon:deps
%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains the core library and elements.

%package devel
Summary:        Libraries/include files for Grilo framework
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains the core library and elements, as well as
general and API documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
    -Denable-gtk-doc=true
%meson_build
%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/grilo-%{release_version}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/grilo-%{release_version}/plugins/
%find_lang grilo
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n grilo-devel -f %{oreon_filedir}/grilo-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.19-1
- Prepare for Oreon 11 (RP1)
