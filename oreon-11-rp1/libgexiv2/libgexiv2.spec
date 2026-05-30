%global source0_hash none

Name:           libgexiv2
Version:        0.16.0
Release:        3%{?dist}
Summary:        Gexiv2 is a GObject-based wrapper around the Exiv2 library

# GNOME mirror path is sources/gexiv2/MAJOR.MINOR/ not full %%{version}
%global gexiv2_series %(echo %{version} | cut -d. -f1-2)

License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/gexiv2
Source0:        https://download.gnome.org/sources/gexiv2/%{version}/gexiv2-%{version}.tar.xz
Patch: 0001-gexiv2-fix-package-name-in-gir-file-to-have-0.16-suf.patch

BuildRequires:  pkgconfig(exiv2)
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base
BuildRequires:  gi-docgen

%description
libgexiv2 is a GObject-based wrapper around the Exiv2 library. 
It makes the basic features of Exiv2 available to GNOME applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     python3-gexiv2
Summary:        Python3 bindings for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       python3-gobject-base-noarch

%description -n python3-gexiv2
This package contains the python3 bindings for %{name}

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n gexiv2-%{version}

%build
%meson \
  -Dgtk_doc=true \
  -Dtests=true \
  %{nil}
%meson_build

%install
%meson_install

%check
# Test failures on s390x, filled as https://bugzilla.redhat.com/show_bug.cgi?id=2435118
%ifnarch s390x
%meson_test
%endif

%files
%license COPYING
%doc AUTHORS NEWS README.md THANKS
%{_libdir}/libgexiv2-0.16.so*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GExiv2-0.16.typelib

%files devel
%{_includedir}/gexiv2-0.16/gexiv2/
%{_libdir}/pkgconfig/gexiv2-0.16.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GExiv2-0.16.gir
%dir %{_datadir}/doc/
%{_datadir}/doc/gexiv2-0.16/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gexiv2-0.16.deps
%{_datadir}/vala/vapi/gexiv2-0.16.vapi

%files -n python3-gexiv2
%pycached %{python3_sitelib}/gi/overrides/GExiv2.py

%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.0-3
- Fix Source0 path use GNOME series dir %%{gexiv2_series} (0.16) not %%{version} (0.16.0)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16.0-2
- Prepare for Oreon 11 (RP1)
