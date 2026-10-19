%global source0_hash c1040d4928308b85b3576a418c5cbd6622f199208f80d4a153d1b829ee8508b8
Name:       ibus-table
Version:    1.17.16
Release:        1%{?dist}
Summary:        The Table engine for IBus platform
License:    LGPL-2.1-or-later
URL:        https://github.com/mike-fabian/ibus-table
Source0:        https://github.com/mike-fabian/ibus-table/releases/download/%{version}/%{name}-%{version}.tar.gz
Requires:       ibus > 1.3.0
%{?__python3:Requires: %{__python3}}
Recommends: python3-simpleaudio
Obsoletes:   ibus-table-additional < 1.2.0.20100111-5
BuildArch:  noarch
# oreon:deps
BuildRequires:  dbus-x11
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  ibus-devel
BuildRequires:  ibus-table-chinese-cangjie
BuildRequires:  ibus-table-chinese-stroke5
BuildRequires:  ibus-table-chinese-wubi-jidian
BuildRequires:  ibus-table-code
BuildRequires:  ibus-table-latin
BuildRequires:  ibus-table-translit
BuildRequires:  ibus-table-tv
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-base
# /oreon:deps
%description
The Table engine for IBus platform.

%package -n %{name}-devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}, pkgconfig
%description -n %{name}-devel
Development files for %{name}.

%package tests
Summary:        Tests for the %{name} package
Requires:       %{name} = %{version}-%{release}
%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

export PYTHON=%{__python3}
%configure --disable-static --disable-additional --enable-installed-tests
%make_build
%install
%__rm -rf $RPM_BUILD_ROOT
export PYTHON=%{__python3}
%make_install NO_INDEX=true pkgconfigdir=%{_datadir}/pkgconfig
%py_byte_compile %{python3} %{buildroot}/usr/share/ibus-table/engine
%py_byte_compile %{python3} %{buildroot}/usr/share/ibus-table/setup
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.metainfo.xml
desktop-file-validate \
    $RPM_BUILD_ROOT%{_datadir}/applications/ibus-setup-table.desktop
pushd engine
    python3 table.py -v
    python3 it_util.py -v
popd
mkdir -p /tmp/glib-2.0/schemas/
cp org.freedesktop.ibus.engine.table.gschema.xml \
   /tmp/glib-2.0/schemas/org.freedesktop.ibus.engine.table.gschema.xml
glib-compile-schemas /tmp/glib-2.0/schemas #&>/dev/null || :
export XDG_DATA_DIRS=/tmp
eval $(dbus-launch --sh-syntax)
dconf dump /
dconf write /org/freedesktop/ibus/engine/table/wubi-jidian/chinesemode 1
dconf write /org/freedesktop/ibus/engine/table/wubi-jidian/spacekeybehavior false
dconf dump /
make check && rc=0 || rc=1
cat tests/*.log
if [ $rc != 0 ] ; then
    exit $rc
fi
%files -f %{oreon_filedir}/main.list
%files -n ibus-table-devel -f %{oreon_filedir}/ibus-table-devel.list
%files -n ibus-table-tests -f %{oreon_filedir}/ibus-table-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17.16-1
- Prepare for Oreon 11 (RP1)
