%global source2_hash cac60c2106750b6adb5c8e26b8bc569263244efdb93bc8047e0f8d95171eec40
%global source1_hash 243c6030d4c26ddbc47cbced4ace6bd7f5922323054b86b6a91333407bed356c
%global source0_hash aea244e1add9628b50ec042c54cf93803f4577f8f142678f09b91fd4c0b20f72
%bcond check 0
Name:           gplugin
Version:        0.44.2
Release:        1%{?dist}
Summary:        GObject based library that implements a reusable plugin system
License:        LGPL-2.0-or-later
URL:            https://keep.imfreedom.org/gplugin/gplugin
Source0:        https://downloads.sourceforge.net/pidgin/%{name}-%{version}.tar.xz
Source1:        https://downloads.sourceforge.net/pidgin/%{name}-%{version}.tar.xz.asc
Source2:        https://keybase.io/grim/pgp_keys.asc
Patch:          gplugin-0.43.1-gi-docgen-no-fatal-warnings.patch
%if %{with check}
%endif
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/gtester
BuildRequires:  /usr/bin/help2man
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  gnupg2
BuildRequires:  lua-lgi
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(python3-embed)
BuildRequires:  vala
# /oreon:deps
%description
GPlugin is a GObject based library that implements a reusable plugin system
which supports loading plugins in other languages via loaders.
It relies heavily on GObject Introspection to expose its API to the other
languages.

It has a very simple API which makes it very simple to use in your application.

%package        libs
Summary:        Library for %{name}
%description    libs
%{summary}.

%package        gtk4
Summary:        GTK4 applications for %{name}
BuildRequires:  pkgconfig(gtk4) >= 4
Requires:       %{name}-gtk4-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description    gtk4
%{summary}.

%package        gtk4-libs
Summary:        GTK4 libraries for %{name}
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description    gtk4-libs
%{summary}.

%package        loader-lua
Summary:        Lua loader for %{name}
BuildRequires:  pkgconfig(lua) >= 5.1.0
BuildRequires:  lua-lgi
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       lua-lgi
%description    loader-lua
%{summary}.

%package        loader-python
Summary:        Python loader for %{name}
BuildRequires:  pkgconfig(python3-embed)
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.0.0
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       pkgconfig(pygobject-3.0) >= 3.0.0
%description    loader-python
%{summary}.

%package        devel
Summary:        Development libraries and header files for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends: gi-docgen-fonts
%description    devel
%{summary}.

%package        gtk4-devel
Summary:        Development libraries and header files for %{name}-gtk4-libs
Requires:       %{name}-gtk4-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Recommends: gi-docgen-fonts
%description    gtk4-devel
%{summary}.

%package        vala
Summary:        Vala bindings for %{name}-libs
BuildRequires:  vala
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description    vala
%{summary}.

%package        gtk4-vala
Summary:        Vala bindings for %{name}-gtk4-libs
Requires:       %{name}-vala%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description    gtk4-vala
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# We install docs ourselves
sed -i -e '/install_data/,+1 d' meson.build
sed -i -e '/install_data/,+1 d' gplugin/share/valgrind/meson.build

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n gplugin-libs -f %{oreon_filedir}/gplugin-libs.list
%files -n gplugin-gtk4 -f %{oreon_filedir}/gplugin-gtk4.list
%files -n gplugin-gtk4-libs -f %{oreon_filedir}/gplugin-gtk4-libs.list
%files -n gplugin-loader-lua -f %{oreon_filedir}/gplugin-loader-lua.list
%files -n gplugin-loader-python -f %{oreon_filedir}/gplugin-loader-python.list
%files -n gplugin-devel -f %{oreon_filedir}/gplugin-devel.list
%files -n gplugin-gtk4-devel -f %{oreon_filedir}/gplugin-gtk4-devel.list
%files -n gplugin-vala -f %{oreon_filedir}/gplugin-vala.list
%files -n gplugin-gtk4-vala -f %{oreon_filedir}/gplugin-gtk4-vala.list

%changelog

%autochangelog
