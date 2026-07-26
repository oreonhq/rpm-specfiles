%global source0_hash 13d950b1ae4650c9710aeba85b59b05cdd5c697b698b04eb0d0be3f7f662a6aa

Name: slingshot
Version:  0.9
Release:  31%{?dist}
Summary: A Newtonian strategy game

License: GPL-2.0-or-later        
URL: https://github.com/ryanakca/slingshot
Source0: https://github.com/ryanakca/slingshot/archive/%{version}/slingshot-%{version}.tar.gz
Source1: slingshot.desktop
Source2: slingshot.appdata.xml
# Port to Python 3
Patch0: 243aef95dde390f97f1e0abbbdb646b3e5b97f7d.patch
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: gnu-free-sans-fonts
Requires: hicolor-icon-theme
Requires: python3-pygame

%description
Slingshot is a two dimensional, turn based simulation-strategy game 
set in the gravity fields of several planets. It is a highly 
addictive game, and never the same from round to round due to its 
randomly generated playing fields.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

rm -f src/slingshot/data/FreeSansBold.ttf

%build
%python3 setup.py build

%install
%python3 setup.py install --skip-build --root %{buildroot} --prefix %{_prefix}

rm -rf $RPM_BUILD_ROOT/slingshot
rm -rf $RPM_BUILD_ROOT/home
rm -rf $RPM_BUILD_ROOT/builddir

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mv src/slingshot/data/icon64x64.png src/slingshot/data/slingshot.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 src/slingshot/data/slingshot.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps

#install appdata
mkdir -p $RPM_BUILD_ROOT/%{_metainfodir}
install -p -m 664 %{SOURCE2} $RPM_BUILD_ROOT/%{_metainfodir}
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_metainfodir}/*.appdata.xml

#Link to font
ln -s %{_datadir}/fonts/gnu-free/FreeSansBold.ttf $RPM_BUILD_ROOT%{python3_sitelib}/%{name}/data/FreeSansBold.ttf

%files
%{_bindir}/slingshot
%{python3_sitelib}/%{name}-*.egg-info
%{python3_sitelib}/%{name}/
%doc README
%license LICENSE
%{_datadir}/applications/slingshot.desktop
%{_datadir}/icons/hicolor/64x64/apps/slingshot.png
%{_datadir}/pixmaps/slingshot.xpm
%{_metainfodir}/slingshot.appdata.xml

%changelog
%autochangelog
