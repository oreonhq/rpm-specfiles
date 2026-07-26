%global source0_hash 8f28213e4feee131c79d7ac6fd40f31df5b80244ba9f408477754af865fd85ed

Name:           veusz
Version:        4.2
Release:        2%{?dist}
Summary:        GUI scientific plotting package

License:        GPL-2.0-or-later AND (LGPL-2.1-only OR GPL-3.0-only) AND PSF-2.0 AND CC0-1.0
URL:            https://veusz.github.io/
Source0:        https://github.com/veusz/veusz/releases/download/veusz-%{version}/veusz-%{version}.tar.gz

BuildRequires:  gcc gcc-c++
BuildRequires:  python3 python3-devel python3-setuptools
BuildRequires:  python3-numpy
BuildRequires:  qt6-qtbase-devel qt6-qtsvg-devel
BuildRequires:  python3-pyqt6 python3-pyqt6-devel
BuildRequires:  python3-pyqt6-sip python3dist(sip)
BuildRequires:  python3-h5py
BuildRequires:  desktop-file-utils

Requires:       python3dist(pyqt6-sip) >= 13, python3dist(pyqt6-sip) < 14
Requires:       python3-pyqt6 python3-pyqt6-sip
Requires:       python3-numpy
Requires:       qt6-qtsvg
Requires:       /usr/bin/env
Recommends:     python3-h5py python3-astropy ghostscript qt6-qtimageformats

Provides:       python3-veusz

# we don't want to provide private python extension libs
# https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering
%global __provides_exclude_from ^%{python3_sitearch}/veusz/helpers/.*\\.so$

# install docs in version specific for old releases
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
Veusz is a 2D and 3D scientific plotting package, designed to create
publication-ready vector PDF and SVG output. It features GUI,
command-line, and scripting interfaces. Graphs are constructed from
widgets, allowing complex layouts to be designed. Veusz supports
plotting functions, data with error bars, keys, labels, stacked plots,
ternary plots, vector plots, contours, images, shapes and fitting
data. 3D point, surface, volume and function plots are also supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n veusz-%{version}

find -name \*~ | xargs rm -f

# remove shebangs from scripts which aren't installed
# (veusz allows these to be executed if app isn't installed properly)
sed -i '/^#!/d' veusz/veusz_main.py
sed -i '/^#!/d' veusz/veusz_listen.py

%build
%py3_build

%install
rm -rf %{buildroot}

# veusz-resource-dir: put data files in location given
%{python3} setup.py install --skip-build --root %{buildroot} \
    --veusz-resource-dir=%{buildroot}/%{_datadir}/veusz \
    --disable-install-examples

# tell veusz where its resource directory is in _datadir
ln -s %{_datadir}/veusz \
    %{buildroot}%{python3_sitearch}/veusz/resources

# tell it where to look for examples and COPYING
ln -s %{_pkgdocdir}/examples \
   %{buildroot}%{_datadir}/veusz

# install desktop file
desktop-file-install  \
    --dir %{buildroot}%{_datadir}/applications \
    support/veusz.desktop

# file to register .vsz mimetype
mkdir -p %{buildroot}%{_datadir}/mime/packages/
install -p support/veusz.xml -m 0644 %{buildroot}%{_datadir}/mime/packages/

# appdata file
mkdir -p %{buildroot}%{_datadir}/appdata/
install -p support/veusz.appdata.xml -m 0644 %{buildroot}%{_datadir}/appdata/

# symlink main veusz icon into pixmaps (for desktop file)
mkdir %{buildroot}%{_datadir}/pixmaps
ln -s ../veusz/icons/veusz_48.png %{buildroot}%{_datadir}/pixmaps/veusz.png

# also link in hicolor icons
for size in 16 32 48 64 128; do
    odir=%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
    mkdir -p $odir
    ln -s %{_datadir}/veusz/icons/veusz_${size}.png ${odir}/veusz.png
done
odir=%{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mkdir -p $odir
ln -s %{_datadir}/veusz/icons/veusz.svg $odir

# install man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -p Documents/man-page/veusz.1 -m 0644 \
    %{buildroot}%{_mandir}/man1

%check
# as the data directory hasn't got the same absolute path we have
# to define VEUSZ_RESOURCE_DIR
PYTHONPATH=%{buildroot}%{python3_sitearch} \
    VEUSZ_RESOURCE_DIR=%{buildroot}%{_datadir}/veusz \
    QT_QPA_PLATFORM=minimal \
    %{python3} tests/runselftest.py

%files
%doc README.md AUTHORS COPYING
%doc examples
%doc Documents/manual/html
%{_bindir}/veusz
%{_mandir}/man1/veusz.1.gz
%{_datadir}/applications/veusz.desktop
%{_datadir}/mime/packages/veusz.xml
%{_datadir}/appdata/veusz.appdata.xml
%{_datadir}/pixmaps/veusz.png
%{_datadir}/icons/hicolor/*/apps/veusz.*
%{_datadir}/veusz
%{python3_sitearch}/veusz-*.egg-info
%{python3_sitearch}/veusz

%changelog
%autochangelog
