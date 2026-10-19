%global source0_hash 9f02d36decaf46b176a1bef74349232508bcc2b4b06d1662bbd1fd426c57d559
%global __provides_exclude_from ^%{_libdir}/calibre/calibre/plugins/.*\.so$
%global _python_bytecompile_extra 0
Name:           calibre
Version:        9.15.0
Release:        1%{?dist}
Summary:        E-book converter and library manager
License:        GPL-3.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-Fedora-Public-Domain AND BSD-3-clause AND Apache-2.0 AND PSF-2.0 AND ImageMagick
URL:            https://calibre-ebook.com/
Source0:        https://download.calibre-ebook.com/%{version}/%{name}-%{version}.tar.xz
Patch:          calibre-no-update.patch
Patch:          calibre-nodisplay.patch
ExclusiveArch:  %{qt6_qtwebengine_arches}
%{?pyqt6_requires}
Requires:       libwebp-tools
Requires:       poppler-utils
Requires:       python3-pyqt6
Requires:       qt6-qtwebengine
Requires:       python3-pyqt6-webengine
Requires:       qt6-qtsvg
Requires:       qt6-qtsensors
Requires:       qt6-qtimageformats
Requires:       qt6-qtwebview
Requires:       poppler-utils
Requires:       liberation-sans-fonts
Requires:       liberation-serif-fonts
Requires:       liberation-mono-fonts
Requires:       mathjax3
Requires:       optipng
Requires:       python3dist(odfpy)
Requires:       python3dist(lxml)
Requires:       python3dist(pillow)
Requires:       python3dist(mechanize)
Requires:       python3dist(python-dateutil)
Requires:       python3dist(beautifulsoup4)
Requires:       python3dist(soupsieve)
Requires:       python3dist(css-parser)
Requires:       python3dist(feedparser)
Requires:       python3dist(netifaces)
Requires:       python3dist(dnspython)
Requires:       python3dist(apsw)
Requires:       python3dist(psutil)
Requires:       python3dist(pygments)
Requires:       python3dist(msgpack)
Requires:       python3dist(regex)
Requires:       python3dist(html5-parser) >= 0.4.8
Requires:       python3dist(html2text)
Requires:       python3dist(markdown) >= 3.0
Requires:       python3dist(pychm)
Requires:       python3dist(pyqt6-sip)
%if %{undefined flatpak}
Requires:       udisks2
%endif
Requires:       /usr/bin/jpegtran
Requires:       jxrlib
Requires:       python3-jeepney
Requires:       qt6-qtmultimedia
Requires:       (qt6-qtspeech-flite or qt6-qtspeech-speechd)
Requires:       python3-xxhash
Recommends:     python3dist(zeroconf)
# oreon:deps
BuildRequires:  /usr/bin/jpegtran
BuildRequires:  bash-completion
BuildRequires:  chmlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  espeak-ng-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  fontconfig-devel
BuildRequires:  glib2-devel
BuildRequires:  hunspell-devel
BuildRequires:  hyphen-devel
BuildRequires:  jxrlib
BuildRequires:  libXrender-devel
BuildRequires:  libappstream-glib
BuildRequires:  libicu-devel
BuildRequires:  libinput-devel
BuildRequires:  libmtp-devel
BuildRequires:  libpng-devel
BuildRequires:  libstemmer-devel
BuildRequires:  libwebp-tools
BuildRequires:  libxkbcommon-devel
BuildRequires:  mathjax3
BuildRequires:  mesa-libEGL
BuildRequires:  onnxruntime-devel
BuildRequires:  openssl-devel
BuildRequires:  optipng
BuildRequires:  podofo0.10-devel
BuildRequires:  poppler-utils
BuildRequires:  pykakasi
BuildRequires:  python3-devel
BuildRequires:  python3-fonttools
BuildRequires:  python3-jeepney
BuildRequires:  python3-pyqt6
BuildRequires:  python3-pyqt6-devel
BuildRequires:  python3-pyqt6-webengine-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-speechd
BuildRequires:  python3-zstd
BuildRequires:  python3dist(apsw)
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(css-parser)
BuildRequires:  python3dist(feedparser)
BuildRequires:  python3dist(html2text)
BuildRequires:  python3dist(html5-parser)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(lxml-html-clean)
BuildRequires:  python3dist(markdown)
BuildRequires:  python3dist(mechanize)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(netifaces)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pychm)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(pyqt-builder)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(regex)
BuildRequires:  python3dist(sgmllib3k)
BuildRequires:  python3dist(sip)
BuildRequires:  python3dist(soupsieve)
BuildRequires:  python3dist(xxhash)
BuildRequires:  python3dist(zeroconf)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-static
BuildRequires:  qt6-qtimageformats
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtspeech-devel
BuildRequires:  qt6-qtspeech-flite
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  qt6-qtwebview-devel
BuildRequires:  sqlite-devel
BuildRequires:  uchardet-devel
BuildRequires:  web-assets-devel
BuildRequires:  xdg-utils
# /oreon:deps
%description
Calibre is meant to be a complete e-library solution. It includes library
management, format conversion, news feeds to ebook conversion as well as
e-book reader sync features.

Calibre is primarily a ebook cataloging program. It manages your ebook
collection for you. It is designed around the concept of the logical book,
i.e. a single entry in the database that may correspond to ebooks in several
formats. It also supports conversion to and from a dozen different ebook
formats.

Supported input formats are: MOBI, LIT, PRC, EPUB, CHM, ODT, HTML, CBR, CBZ,
RTF, TXT, PDF and LRS.

%prep

%autosetup -n calibre-%{version} -p1

# remove shebangs
sed -i -e '/^#!\//, 1d' src/calibre/*/*/*/*/*.py
sed -i -e '/^#!\//, 1d' src/calibre/*/*/*/*.py
sed -i -e '/^#!\//, 1d' src/calibre/*/*/*.py
sed -i -e '/^#![ ]*\//, 1d' src/calibre/*/*.py
sed -i -e '/^#!\//, 1d' src/calibre/*.py
sed -i -e '/^#!\//, 1d' src/css_selectors/*.py
sed -i -e '/^#!\//, 1d' src/polyglot/*.py
#sed -i -e '/^#!\//, 1d' src/templite/*.py
sed -i -e '/^#!\//, 1d' src/tinycss/*/*.py
sed -i -e '/^#!\//, 1d' src/tinycss/*.py
sed -i -e '/^#!\//, 1d' resources/default_tweaks.py

chmod -x src/calibre/*/*/*/*.py \
    src/calibre/*/*/*.py \
    src/calibre/*/*.py \
    src/calibre/*.py

# remove bundled MathJax
rm -rv resources/mathjax

%build

%python3 setup.py mathjax \
    --system-mathjax \
    --path-to-mathjax %{_jsdir}/mathjax@3/
%install
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{python3_sitearch}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
LIBPATH="%{_libdir}" \
CALIBRE_PY3_PORT=1 \
PODOFO_INC_DIR=%{_includedir}/podofo \
PODOFO_LIB_DIR=%{_libdir} \
PODOFO_LIB_NAME=%{_libdir}/libpodofo.so \
%python3 setup.py install \
    --root=%{buildroot}%{_prefix} \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --staging-root=%{buildroot}%{_prefix} \
    --staging-libdir=%{buildroot}%{_libdir} \
    --staging-sharedir=%{buildroot}%{_datadir}
sed -i -e '/^#!\//, 1d' %{buildroot}%{python3_sitearch}/init_calibre.py
%py_byte_compile %python3 %{buildroot}%{_datadir}/calibre
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp -p resources/images/library.png                \
   %{buildroot}%{_datadir}/pixmaps/calibre-gui.png
cp -p resources/images/viewer.png                 \
   %{buildroot}%{_datadir}/pixmaps/calibre-viewer.png
cp -p resources/images/tweak.png                 \
   %{buildroot}%{_datadir}/pixmaps/calibre-ebook-edit.png
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/calibre-ebook-edit.desktop \
    %{buildroot}%{_datadir}/applications/calibre-ebook-viewer.desktop \
    %{buildroot}%{_datadir}/applications/calibre-gui.desktop \
    %{buildroot}%{_datadir}/applications/calibre-lrfviewer.desktop
rm -r %{buildroot}%{_datadir}/icons/hicolor/128x128
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp -p resources/images/mimetypes/lrf.png \
      %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-sony-bbeb.png
cp -p resources/images/viewer.png \
      %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/calibre-viewer.png
rm -r %{buildroot}%{_libdir}/calibre/odf
rm %{buildroot}%{_datadir}/calibre/fonts/liberation/*
ln --symbolic --relative \
    %{buildroot}%{_usr}/share/fonts/liberation-mono/LiberationMono-BoldItalic.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationMono-BoldItalic.ttf
ln --symbolic --relative \
    %{buildroot}%{_usr}/share/fonts/liberation-mono/LiberationMono-Bold.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationMono-Bold.ttf
ln --symbolic --relative \
    %{buildroot}%{_usr}/share/fonts/liberation-mono/LiberationMono-Italic.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationMono-Italic.ttf
ln --symbolic --relative \
    %{buildroot}%{_usr}/share/fonts/liberation-mono/LiberationMono-Regular.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationMono-Regular.ttf
ln --symbolic --relative \
    %{buildroot}%{_usr}/share/fonts/liberation-sans/LiberationSans-BoldItalic.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSans-BoldItalic.ttf
ln --symbolic --relative \
    %{buildroot}%{_usr}/share/fonts/liberation-sans/LiberationSans-Bold.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSans-Bold.ttf
ln --symbolic --relative \
    %{buildroot}%{_usr}/share/fonts/liberation-sans/LiberationSans-Italic.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSans-Italic.ttf
ln --symbolic --relative \
    %{buildroot}%{_usr}/share/fonts/liberation-sans/LiberationSans-Regular.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSans-Regular.ttf
ln --symbolic --relative \
    %{buildroot}%{_usr}/share/fonts/liberation-serif/LiberationSerif-BoldItalic.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSerif-BoldItalic.ttf
ln --symbolic --relative \
    %{buildroot}%{_usr}/share/fonts/liberation-serif/LiberationSerif-Bold.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSerif-Bold.ttf
ln --symbolic --relative \
    %{buildroot}%{_usr}/share/fonts/liberation-serif/LiberationSerif-Italic.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSerif-Italic.ttf
ln --symbolic --relative \
    %{buildroot}%{_usr}/share/fonts/liberation-serif/LiberationSerif-Regular.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSerif-Regular.ttf
rm %{buildroot}/%{_datadir}/metainfo/calibre-ebook-edit.metainfo.xml
rm %{buildroot}/%{_datadir}/metainfo/calibre-ebook-viewer.metainfo.xml
%oreon_autofiles main

%check

TEST_ARGS=(
    --exclude-test-name unrar              # missing dependencies
    --exclude-test-name bonjour            # problems in mock
    --exclude-test-name 7z                 # missing dependencies
    --exclude-test-name test_searching     # python3 porting issue?
    --exclude-test-name test_zstd          # pyzstd not packaged yet
    --exclude-test-name test_zeroconf      # AttributeError: 'functools._lru_cache_wrapper' object has no attribute '__kwdefaults__'
    --exclude-test-name test_imaging       # WEBP Transparency support ok' not found
    --exclude-test-name test_recipe_browser_qt # Accept-Encoding not found
    --exclude-test-name test_websocket_basic
    --exclude-test-name test_ssl
    --exclude-test-name test_pycryptodome  # We do not ship the bundled pycryptodome
    --exclude-test-name test_piper         # piper is not yet packaged
    --exclude-test-name test_get
    --exclude-test-name test_qt
    --exclude-test-name test_recipe_browser_webengine
    --exclude-test-name test_tzdata
%ifarch ppc64le
    --exclude-test-name test_fts_pool
    --exclude-test-name test_fts_search
%endif
)
CALIBRE_PY3_PORT=1 \
%python3 setup.py test "${TEST_ARGS[@]}"
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/calibre-gui.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
