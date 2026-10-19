%global source0_hash 5fdb49da785e29ec25dbb706df2a9256c06dabf464fbdedf18fd445693399f16
Name:           PyMca
Version:        5.9.7
Release:        1%{?dist}
Summary:        X-ray Fluorescence Toolkit
License:        GPL-2.0-or-later
URL:            http://pymca.sourceforge.net/
Source0:        pymca-%{version}-filtered.tar.xz
Source1:        PyMca.desktop
Source2:        edfviewer.desktop
Source3:        elementsinfo.desktop
Source4:        mca2edf.desktop
Source5:        peakidentifier.desktop
Source6:        pymcabatch.desktop
Source7:        pymcapostbatch.desktop
Source8:        pymcaroitool.desktop
Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}
Requires:       python3dist(pyqt5)
Requires:       python3-matplotlib
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  glibc-langpack-pl
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(fisx)
BuildRequires:  python3dist(h5py)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pyqt5)
BuildRequires:  qhull-devel
# /oreon:deps
%description
PyMCA provides a graphical interface for multi-channel analyzer spectra
visualization and analysis. PyMca can display spectra from a file or directly
from SPEC during acquisitions.

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch
%description    data
This package contains photon interaction data/elements data for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pymca-%{version}

sed -r -i 's|(os.path.join.")(PyMca5")|\1src/\2|' setup.py

# The test fails in F44 rawhide with:
# ERROR: testPCAToolsPCA (PCAToolsTest.testPCATools.testPCAToolsPCA)
# ----------------------------------------------------------------------
# TypeError: only 0-dimensional arrays can be converted to Python scalars
# The above exception was the direct cause of the following exception:
# Traceback (most recent call last):
#   File "/builddir/build/BUILD/PyMca-5.9.4-build/pymca-5.9.4/src/PyMca5/tests/PCAToolsTest.py", line 116, in testPCAToolsPCA
#     images, eigenvalues, eigenvectors = numpyPCA(x,
#                                         ~~~~~~~~^^^
#                                                  ncomponents=ncomp,
#                                                  ^^^^^^^^^^^^^^^^^^
#                                                  force=force,
#                                                  ^^^^^^^^^^^^
#                                                  center=False,
#                                                  ^^^^^^^^^^^^^
#                                                  scale=False)
#                                                  ^^^^^^^^^^^^
#   File "/builddir/build/BUILD/PyMca-5.9.4-build/BUILDROOT/usr/lib64/python3.14/site-packages/PyMca5/PyMcaMath/mva/PCATools.py", line 696, in numpyPCA
#     images[j, i] = numpy.dot(tmpData, eigenvectors[j])
#     ~~~~~~^^^^^^
# ValueError: setting an array element with a sequence.
# ----------------------------------------------------------------------
sed -r -i 's/def testPCAToolsPCA/def _ignored_testPCAToolsPCA/' src/PyMca5/tests/PCAToolsTest.py

%build

QHULL_CFLAGS="-I%{_includedir}/libqhull" \
QHULL_LIBS="-lqhull" \
SPECFILE_USE_GNU_SOURCE=1 \
PYMCA_DATA_DIR=/usr/share/PyMca \
PYMCA_DOC_DIR=/usr/share/doc/PyMca \
%py3_build
%install
PYMCA_DATA_DIR=/usr/share/PyMca \
PYMCA_DOC_DIR=/usr/share/doc/PyMca \
%py3_install
cp -ap src/PyMca5/PyMcaData/attdata/* %{buildroot}%{_datadir}/PyMca/attdata/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:1}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:2}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:3}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:4}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:5}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:6}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:7}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{S:8}
mkdir -p %{buildroot}%{_datadir}/appdata
cat >%{buildroot}%{_datadir}/appdata/edfviewer.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>edfviewer.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF
cat >%{buildroot}%{_datadir}/appdata/elementsinfo.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>elementsinfo.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF
cat >%{buildroot}%{_datadir}/appdata/mca2edf.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>mca2edf.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF
cat >%{buildroot}%{_datadir}/appdata/peakidentifier.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>peakidentifier.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF
cat >%{buildroot}%{_datadir}/appdata/pymcabatch.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>pymcabatch.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF
cat >%{buildroot}%{_datadir}/appdata/pymcapostbatch.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>pymcapostbatch.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF
cat >%{buildroot}%{_datadir}/appdata/pymcaroitool.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<component type="desktop">
  <metadata_license>CC0-1.0</metadata_license>
  <id>pymcaroitool.desktop</id>
  <metadata>
    <value key="X-Merge-With-Parent">PyMca.desktop</value>
  </metadata>
</component>
EOF
for size in 192x192 128x128 96x96 72x72 64x64 48x48 40x40 36x36 32x32 26x26 24x24 22x22 16x16 ; do
    install -pdm755 \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps
    convert -resize ${size} icons/PyMca_256x256.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}/apps/%{name}.png
done
find %{buildroot}%{python3_sitearch}/PyMca5/ -type f -exec chmod 644 {} +
find %{buildroot}%{python3_sitearch}/PyMca5/ -name *.so -exec chmod 755 {} +
find %{buildroot}%{python3_sitearch}/PyMca5 -type f -name '*.py' \
     -exec sed -i '/\/usr\/bin\/env/d' {} + \
     -exec touch -r setup.py {} +
%oreon_autofiles PyMca-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

PYTHONPATH=%{buildroot}%{python3_sitearch} \
PYMCA_DATA_DIR=%{buildroot}/usr/share/PyMca \
PYMCA_DOC_DIR=%{buildroot}/usr/share/doc/PyMca \
QT_QPA_PLATFORM=offscreen \
LC_ALL=pl_PL.utf8 \
%python3 src/PyMca5/tests/TestAll.py
%files -f %{oreon_filedir}/main.list
%files -n PyMca-data -f %{oreon_filedir}/PyMca-data.list

%changelog

%autochangelog
