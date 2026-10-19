%global source0_hash fc4a448bccb1a09b68865409b9e2aed171d28a2d5ac80f7be44f5fcca84ee0c1
%global nautilus_version 43~beta
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           nautilus-python
Version:        4.1.0
Release:        1%{?dist}
Summary:        Python bindings for Nautilus
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/NautilusPython
Source0:        https://download.gnome.org/sources/%{name}/4.1/%{name}-%{version}.tar.xz
Requires:       nautilus-extensions%{?_isa} >= %{nautilus_version}
Requires:       python3-gobject-base%{?_isa}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(libnautilus-extension-4)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel
# /oreon:deps
%description
Python bindings for Nautilus

%package devel
Summary:        Python bindings for Nautilus
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Python bindings for Nautilus

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/nautilus-python/extensions
rm -rfv $RPM_BUILD_ROOT%{_docdir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n nautilus-python-devel -f %{oreon_filedir}/nautilus-python-devel.list

%changelog

%autochangelog

