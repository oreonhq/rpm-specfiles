%global source0_hash 1e2419a5f21d26c324b28ae1c00e29e9175e8b596fff385a04c2172b36652226
%global debug_package %{nil}
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           gsettings-desktop-schemas
Version:        51.0
Release:        1%{?dist}
Summary:        A collection of GSettings schemas
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gsettings-desktop-schemas
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Source1:        org.gnome.desktop.interface.rhel.gschema.override
Requires: glib2 >= 2.31.0
Recommends: font(adwaitasans)
Recommends: font(adwaitamono)
# oreon:deps
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
# /oreon:deps
%description
gsettings-desktop-schemas contains a collection of GSettings schemas for
settings shared by various components of a desktop.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries
and header files for developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

glib-compile-schemas --dry-run --strict %{buildroot}%{_datadir}/glib-2.0/schemas
%files -f %{oreon_filedir}/main.list
%files -n gsettings-desktop-schemas-devel -f %{oreon_filedir}/gsettings-desktop-schemas-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
