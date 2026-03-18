#!/bin/bash -x

QT_BRANCH=5.15
QT_VERSION=5.15.1
make_build="$(rpm --eval %make_build)"

# Clone full qt tree
git clone -b $QT_BRANCH git://code.qt.io/qt/qt5.git

# Install fedora deps for qt5-qtbase, qt5-qttools
sudo dnf builddep qt5-qtbase qt5-qttools -y

# Configure using fedora configure basic options
cd qt5 || return
git submodule foreach "git checkout $QT_BRANCH"
git submodule foreach "git fetch"
git submodule foreach "git pull"

# Init the base source
./init-repository

# hard-code docdir for now, rpm --eval %{_qt5_docdir} yields unexpanded %{_docdir}/qt5 , wtf -- rex
./configure -confirm-license -opensource -prefix $(rpm --eval "%{_qt5_prefix}") \
    -archdatadir $(rpm --eval "%{_qt5_archdatadir}") -bindir $(rpm --eval "%{_qt5_bindir}") \
    -libdir $(rpm --eval "%{_qt5_libdir}") -libexecdir $(rpm --eval "%{_qt5_libexecdir}") \
    -datadir $(rpm --eval "%{_qt5_datadir}") -docdir /usr/share/doc/qt5 \
    -examplesdir $(rpm --eval "%{_qt5_examplesdir}") -headerdir $(rpm --eval "%{_qt5_headerdir}") \
    -importdir $(rpm --eval "%{_qt5_importdir}") -plugindir $(rpm --eval "%{_qt5_plugindir}") \
    -sysconfdir $(rpm --eval "%{_qt5_sysconfdir}") -translationdir $(rpm --eval "%{_qt5_translationdir}") \
    -platform linux-g++ -release -shared -accessibility -dbus-runtime -fontconfig -glib -gtk \
    -icu -journald -nomake examples -nomake tests -no-rpath -no-separate-debug-info -no-strip \
    -system-libjpeg -system-libpng -system-zlib -no-directfb -skip qtmacextras -skip qtandroidextras \
    -skip qtactiveqt -skip qtwinextras -skip qtqa

$make_build qmake_all

$make_build -C qtbase || exit
$make_build -C qtbase/src/tools/bootstrap
$make_build -C qtbase/src/tools/rcc
$make_build sub-qmldevtools -C qtdeclarative/src/
$make_build sub-qdoc sub-qtattributionsscanner -C qttools/src/
$make_build sub-qhelpgenerator -C qttools/src/assistant/

echo "INFO: make docs"
$make_build -j1 docs  || echo "ERROR: make docs" ; exit 1

# Install docs on tmp directory
DEST=${PWD}/install
rm -rf $DEST/ && mkdir -p ${DEST}
$make_build install_docs INSTALL_ROOT=$DEST -k

XZ_OPT="-T 2"
tar -C $DEST -cJf ../qt-doc-opensource-src-${QT_VERSION}.tar.xz .
