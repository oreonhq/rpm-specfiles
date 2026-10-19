%global source0_hash 643825c245b262c548f1a7902c67877650e286d2155aac109a11481c689c5285
Name:           brewtarget
Version:        4.2.1
Release:        1%{?dist}
Summary:        An open source beer recipe creation tool 🍺
%global forgeurl https://github.com/Brewtarget/brewtarget
%forgemeta
License:    GPL-3.0-or-later AND BSD-2-Clause AND WTFPL AND (CC-BY-SA-3.0 OR LGPL-3.0-only) AND LGPL-2.1-only
URL:        %forgeurl
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:      0001-Modify-boost-requirements-for-Fedora.patch
Patch:      0002-Fix-name-of-lupdate-executable.patch
Patch:      0003-Use-system-installed-valijson.patch
Requires:       sqlite
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake(qt6core)
BuildRequires:  cmake(qt6linguisttools)
BuildRequires:  cmake(qt6multimedia)
BuildRequires:  cmake(qt6svg)
BuildRequires:  cmake(valijson)
BuildRequires:  cmake(xalanc)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pandoc
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xerces-c)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
# Crude way of disabling testLogRotation
sed -i -e '/testLogRotation/d' meson.build

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

cat > mesontest.sh << EOF
mkdir %{_builddir}/%{name}-%{version}/brewtarget-test
export TMPDIR="%{_builddir}/%{name}-%{version}/brewtarget-test"
%meson_test --verbose --timeout-multiplier 2
EOF
chmod a+x ./mesontest.sh
xvfb-run ./mesontest.sh
desktop-file-validate %buildroot%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
