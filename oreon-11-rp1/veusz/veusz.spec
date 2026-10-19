%global source0_hash fadc46d4c4166d9695ab7db6a7865cb736a73f0fa07847fd8a5bb9906408dd09
Name:           veusz
Version:        4.2.1
Release:        1%{?dist}
Summary:        GUI scientific plotting package
License:        GPL-2.0-or-later AND (LGPL-2.1-only OR GPL-3.0-only) AND PSF-2.0 AND CC0-1.0
URL:            https://veusz.github.io/
Source0:        https://github.com/veusz/veusz/releases/download/veusz-%{version}/veusz-%{version}.tar.gz
Requires:       python3dist(pyqt6-sip) >= 13, python3dist(pyqt6-sip) < 14
Requires:       python3-pyqt6 python3-pyqt6-sip
Requires:       python3-numpy
Requires:       qt6-qtsvg
Requires:       /usr/bin/env
Recommends:     python3-h5py python3-astropy ghostscript qt6-qtimageformats
Provides:       python3-veusz
%global __provides_exclude_from ^%{python3_sitearch}/veusz/helpers/.*\\.so$
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-h5py
BuildRequires:  python3-numpy
BuildRequires:  python3-pyqt6
BuildRequires:  python3-pyqt6-devel
BuildRequires:  python3-pyqt6-sip
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(sip)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
# /oreon:deps
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
%{python3} setup.py install --skip-build --root %{buildroot} \
    --veusz-resource-dir=%{buildroot}/%{_datadir}/veusz \
    --disable-install-examples
ln -s %{_datadir}/veusz \
    %{buildroot}%{python3_sitearch}/veusz/resources
ln -s %{_pkgdocdir}/examples \
   %{buildroot}%{_datadir}/veusz
desktop-file-install  \
    --dir %{buildroot}%{_datadir}/applications \
    support/veusz.desktop
mkdir -p %{buildroot}%{_datadir}/mime/packages/
install -p support/veusz.xml -m 0644 %{buildroot}%{_datadir}/mime/packages/
mkdir -p %{buildroot}%{_datadir}/appdata/
install -p support/veusz.appdata.xml -m 0644 %{buildroot}%{_datadir}/appdata/
mkdir %{buildroot}%{_datadir}/pixmaps
ln -s ../veusz/icons/veusz_48.png %{buildroot}%{_datadir}/pixmaps/veusz.png
for size in 16 32 48 64 128; do
    odir=%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
    mkdir -p $odir
    ln -s %{_datadir}/veusz/icons/veusz_${size}.png ${odir}/veusz.png
done
odir=%{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mkdir -p $odir
ln -s %{_datadir}/veusz/icons/veusz.svg $odir
mkdir -p %{buildroot}%{_mandir}/man1
install -p Documents/man-page/veusz.1 -m 0644 \
    %{buildroot}%{_mandir}/man1
%oreon_autofiles main

%check

PYTHONPATH=%{buildroot}%{python3_sitearch} \
    VEUSZ_RESOURCE_DIR=%{buildroot}%{_datadir}/veusz \
    QT_QPA_PLATFORM=minimal \
    %{python3} tests/runselftest.py
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
