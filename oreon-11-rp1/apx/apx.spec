%global source0_hash b61d481adbe6e0af241fd30dfdc455814358f011b908db6fc26b0a93ba3276e9
%global commit0 722c52e819e98ed8b88a26f9891d4b6b0983bcb7
%global date0   20160804
Name:           apx
Version:        0.1
Release:        1%{?dist}
Summary:        QIX clone, cut into and claim the square area
License:        MIT
URL:            https://github.com/tstriker/%{name}
Source0:        https://github.com/tstriker/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
BuildArch:      noarch
Requires:       python3
Requires:       hicolor-icon-theme
Requires:       python3-gobject
Requires:       python3-cairo
Requires:       %{name}-fonts = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
APX is a QIX clone with minor differences in game-play from the original.
Read about the original: http://en.wikipedia.org/wiki/Qix

Use arrow keys to move around the perimeter of square, hold down Space or Shift
to cut into the area. Connect back to perimeter to claim the area.

Your objective is to claim 75 percent or more to proceed to the next level.

Claiming with Shift key will be slower but give you double the points.

For every claimed full percent over 75 percent you get extra 1000 points.

%package fonts
Summary:       Fonts for the game %{name}
License:       LicenseRef-Callaway-CC-BY
URL:           http://www.04.jp.org/
BuildArch:     noarch
Requires:      fontpackages-filesystem
%description fonts
Fonts for the game %{name}.
Redistribution from: http://www.04.jp.org

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n%{name}-%{commit0}
sed -i s,Games,Game, data/*.desktop
# add right shebang
sed -i '1d;2i#!%{__python3}' bin/%{name}
find %{name} -name \*.py |xargs sed -i '/^#!\//, 1d'
# do not try to install the font again and again
sed -i /utils.install_font.*/d bin/%{name}
sed -i -r 's,(fonts/)04b03,\1%{name},' setup.py

%build

sed -i '/"install":/d' setup.py
%py3_build
%install
%py3_install
find %{buildroot} -name '*LICENSE' -print -delete
%oreon_autofiles apx-fonts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n apx-fonts -f %{oreon_filedir}/apx-fonts.list

%changelog

%autochangelog
