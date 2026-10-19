%global source0_hash a60f9bc363de5aac5128dfb61c9993d670d237e18a36c2cb05a73d7b2ff8096e
%global module_name ibus_cangjie
%global forgeurl https://github.com/Cangjians/ibus-cangjie
%global archiveext tar.xz
Name:             ibus-cangjie
Summary:        IBus engine to input Cangjie and Quick
Version:          2.5.0
Release:        1%{?dist}
%forgemeta
License:          GPL-3.0-or-later
URL:              https://cangjie.pages.freedesktop.org/projects/%{name}
Source0:        https://gitlab.freedesktop.org/cangjie/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:           0001-tests-no-coverage.patch
BuildArch:        noarch
Requires:         gobject-introspection
Requires:         gtk3
Requires:         gsound
Requires:         python3-cangjie >= 1.5
Requires:         python3-gobject
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gobject-introspection
BuildRequires:  gsound
BuildRequires:  gtk3
BuildRequires:  ibus-devel
BuildRequires:  libcangjie-data
BuildRequires:  meson
BuildRequires:  python3-cangjie
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
# /oreon:deps
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
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export CANGJIE_DB=/usr/share/libcangjie/cangjie.db
%meson_test --suite unittest
%files -f %{oreon_filedir}/main.list
%files -n ibus-cangjie-engine-cangjie -f %{oreon_filedir}/ibus-cangjie-engine-cangjie.list
%files -n ibus-cangjie-engine-quick -f %{oreon_filedir}/ibus-cangjie-engine-quick.list

%changelog

%autochangelog
