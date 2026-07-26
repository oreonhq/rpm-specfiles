%global source0_hash a60f9bc363de5aac5128dfb61c9993d670d237e18a36c2cb05a73d7b2ff8096e

%global module_name ibus_cangjie
%global forgeurl https://github.com/Cangjians/ibus-cangjie
%global archiveext tar.xz

Name:             ibus-cangjie
Summary:          IBus engine to input Cangjie and Quick
Version:          2.5.0
Release:          %autorelease

%forgemeta

License:          GPL-3.0-or-later
URL:              https://cangjie.pages.freedesktop.org/projects/%{name}
Source0:          https://gitlab.freedesktop.org/cangjie/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:           0001-tests-no-coverage.patch

BuildArch:        noarch

BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    gettext
BuildRequires:    ibus-devel
BuildRequires:    python3-devel
BuildRequires:    meson

# For the unit tests
BuildRequires:    gobject-introspection
BuildRequires:    gtk3
BuildRequires:    gsound
BuildRequires:    libcangjie-data
BuildRequires:    python3-cangjie >= 1.5
BuildRequires:    python3-gobject

Requires:         gobject-introspection
Requires:         gtk3
Requires:         gsound
Requires:         python3-cangjie >= 1.5
Requires:         python3-gobject

%description
Common files needed by the IBus engines for users of the Cangjie and Quick
input methods.

%package engine-cangjie
Summary:          Cangjie input method for IBus
Requires:         %{name} = %{version}-%{release}

%description engine-cangjie
IBus engine for users of the Cangjie input method.

It is primarily intended to Hong Kong people who want to input Traditional
Chinese, as they are (by far) the majority of Cangjie users.

However, it should work for others as well (e.g to input Simplified Chinese).

%package engine-quick
Summary:          Quick (Simplified Cangjie) input method for IBus
Requires:         %{name} = %{version}-%{release}

%description engine-quick
IBus engine for users of the Quick (Simplified Cangjie) input method.

It is primarily intended to Hong Kong people who want to input Traditional
Chinese, as they are (by far) the majority of Quick users.

However, it should work for others as well (e.g to input Simplified Chinese).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%check
export CANGJIE_DB=/usr/share/libcangjie/cangjie.db
%meson_test --suite unittest

%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING
%{_bindir}/ibus-setup-cangjie
%{python3_sitelib}/%{module_name}
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.freedesktop.cangjie.ibus.Cangjie.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.cangjie.ibus.Quick.gschema.xml
%{_datadir}/icons/hicolor/*/intl/*
%{_libexecdir}/ibus-engine-cangjie

%files engine-cangjie
%{_datadir}/applications/ibus-setup-cangjie.desktop
%{_datadir}/applications/org.freedesktop.cangjie.ibus.cangjie-setup.desktop
%{_datadir}/metainfo/org.freedesktop.cangjie.ibus.Cangjie.metainfo.xml
%{_datadir}/ibus/component/org.freedesktop.cangjie.ibus.Cangjie.xml

# Old schema file, for schema migration in this release
%{_datadir}/glib-2.0/schemas/org.cangjians.ibus.cangjie.gschema.xml

%files engine-quick
%{_datadir}/applications/ibus-setup-quick.desktop
%{_datadir}/applications/org.freedesktop.cangjie.ibus.quick-setup.desktop
%{_datadir}/metainfo/org.freedesktop.cangjie.ibus.Quick.metainfo.xml
%{_datadir}/ibus/component/org.freedesktop.cangjie.ibus.Quick.xml

# Old schema file, for schema migration in this release
%{_datadir}/glib-2.0/schemas/org.cangjians.ibus.quick.gschema.xml

%changelog
%autochangelog
