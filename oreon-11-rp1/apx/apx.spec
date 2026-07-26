%global source0_hash b61d481adbe6e0af241fd30dfdc455814358f011b908db6fc26b0a93ba3276e9

%global commit0 722c52e819e98ed8b88a26f9891d4b6b0983bcb7
%global date0   20160804

Name:           apx
Version:        0.1
Release:        48.%{date0}git%{?dist}
Summary:        QIX clone, cut into and claim the square area

# Automatically converted from old format: MIT - review is highly recommended.
License:        MIT
URL:            https://github.com/tstriker/%{name}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel python3-setuptools
BuildRequires:  fontpackages-devel
BuildRequires:  desktop-file-utils libappstream-glib

Requires:       python3

Requires:       hicolor-icon-theme

# need introspection for cairo
Requires:       python3-gobject
Requires:       python3-cairo

Requires:       %{name}-fonts = %{version}-%{release}

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
# Automatically converted from old format: CC-BY - review is highly recommended.
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
# avoid misplaced license file
find %{buildroot} -name '*LICENSE' -print -delete

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%license LICENSE
%doc AUTHORS README.md
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.sqlite
%{_datadir}/icons/hicolor/scalable/*.svg
%{python3_sitelib}/*
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/*.appdata.xml

%_font_pkg *.ttf
%license data/*_LICENSE

%changelog
%autochangelog
