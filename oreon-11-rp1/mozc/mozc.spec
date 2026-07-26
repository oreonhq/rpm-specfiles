%global source0_hash 767cc05bb9325288f7288aed51d75291b8b25b464d8f4d8ffd44184aad95c70d

%global		pkg	mozc
%undefine	_hardened_build

%bcond_without	zinnia
%bcond_without	qt

Name:		mozc
Version:	2.29.5111.102
Release:	18%{?dist}
Summary:	A Japanese Input Method Editor (IME) designed for multi-platform

License:	BSD-3-Clause AND Apache-2.0 AND Unicode-DFS-2015 AND NAIST-2003
URL:		https://github.com/google/mozc
# data/unicode/: UCD
#  Copyright (c) 1991-2008 Unicode, Inc.
# data/test/stress_test/sentences.txt: Public Domain
#   See https://gitlab.com/fedora/legal/fedora-license-data/-/issues/178#note_1331790847
# data/dictionary_oss/: mecab-ipadic and BSD
#   See http://code.google.com/p/mozc/issues/detail?id=20
#   also data/installer/credits_en.html

##Source0:	http://mozc.googlecode.com/files/mozc-%%{version}.tar.bz2
# No upstream releases downloadable from the download services due to:
#   http://google-opensource.blogspot.jp/2013/05/a-change-to-google-code-download-service.html
#
# How to checkout the tree from the repository:
#   https://github.com/google/mozc/blob/master/docs/build_mozc_in_docker.md
#
# How to make a tarball after updating:
#   (cd src;
#    python build_mozc.py gyp --target_platform=Linux
#   )
#   major=$(grep MAJOR src/mozc_version.txt|sed -e 's/MAJOR=//g')
#   minor=$(grep MINOR src/mozc_version.txt|sed -e 's/MINOR=//g')
#   build=$(grep BUILD src/mozc_version.txt|sed -e 's/BUILD=//g')
#   rev=$(grep REVISION src/mozc_version.txt|sed -e 's/REVISION=//g')
#   version="$major.$minor.$build.$rev"
#   (cd src;
#    for f in $(find -type f -regex '.*.[ch]' -o -regex '.*.html' -o -regex '.*README*'); do chmod a-x $f; done
#    tar -a --exclude-vcs --exclude third_party/gyp* -cf ../mozc-$version.tar.bz2 *
#   )
#
Source0:	%{name}-%{version}.tar.xz
Source1:	mozc-init.el
# Public Domain
## https://gitlab.com/fedora/legal/fedora-license-data/-/issues/181#note_1339185494
Source2:	http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip
Source3:	http://www.post.japanpost.jp/zipcode/dl/jigyosyo/zip/jigyosyo.zip
Source4:	ibus-setup-mozc-jp.desktop
Source5:	ibus-mozc-launch-xwayland.desktop
Source6:	ibus-mozc-launch-xwayland.sh
Patch0:		mozc-build-ninja.patch
## to avoid undefined symbols with clang.
Patch1:		mozc-build-gcc.patch
Patch2:		mozc-build-verbosely.patch
Patch3:		mozc-build-id.patch
Patch4:		mozc-build-gcc-common.patch
Patch5:		mozc-use-system-abseil-cpp.patch
Patch6:		mozc-build-gyp.patch
Patch7:		mozc-build-new-abseil.patch
# Add #include directives for compatibility with abseil-cpp-20240116.
# Downstream-only because these are fixed upstream in a later release.
Patch8:         mozc-abseil-cpp-20240116-includes.patch
Patch9:		mozc-fix-2257171.patch

BuildRequires:	python gettext
BuildRequires:	libstdc++-devel zlib-devel libxcb-devel protobuf-devel protobuf-c glib2-devel gtk2-devel
BuildRequires:	abseil-cpp-devel
%if %{with qt}
BuildRequires:	qt5-qtbase-devel
%endif
%if %{with zinnia}
BuildRequires:	zinnia-devel
%endif
BuildRequires:	clang ninja-build
BuildRequires:	gyp >= 0.1-0.4.840svn
BuildRequires:	ibus-devel >= 1.5.4
BuildRequires:	emacs
%if 0%{?fedora} < 36
BuildRequires:	xemacs xemacs-packages-extra
%endif
BuildRequires:  desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:  %{py3_dist six}
BuildRequires:  binutils
# https://bugzilla.redhat.com/show_bug.cgi?id=1419949
ExcludeArch:	ppc ppc64 sparcv9 sparc64 s390x

%if %{with zinnia}
Recommends:	zinnia-tomoe-ja
%endif
Requires:	emacs-filesystem >= %{_emacs_version}
%if 0%{?fedora} < 36
Requires:	xemacs-filesystem >= %{_xemacs_version}
%endif
Provides:	emacs-mozc <= 2.17.2077.102-4, emacs-mozc-el <= 2.17.2077.102-4
Obsoletes:	emacs-mozc <= 2.17.2077.102-4, emacs-mozc-el <= 2.17.2077.102-4
Provides:	xemacs-mozc <= 2.17.2077.102-4, xemacs-mozc-el <= 2.17.2077.102-4
Obsoletes:	xemacs-mozc <= 2.17.2077.102-4, xemacs-mozc-el <= 2.17.2077.102-4
Provides:	emacs-common-mozc <= 2.17.2077.102-4
Obsoletes:	emacs-common-mozc <= 2.17.2077.102-4

%description
Mozc is a Japanese Input Method Editor (IME) designed for
multi-platform such as Chromium OS, Windows, Mac and Linux.

%package	-n ibus-mozc
Summary:	The mozc engine for IBus input platform
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	ibus%{?_isa} >= 1.5.4
Requires:	xrefresh

%description	-n ibus-mozc
Mozc is a Japanese Input Method Editor (IME) designed for
multi-platform such as Chromium OS, Windows, Mac and Linux.

This package contains the Input Method Engine for IBus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}-%{version} -a 2 -a 3
%autopatch -p1
(cd data/dictionary_oss;
PYTHONPATH="${PYTHONPATH}:../.." python ../../dictionary/gen_zip_code_seed.py --zip_code=../../KEN_ALL.CSV --jigyosyo=../../JIGYOSYO.CSV >> dictionary09.txt;
)
rm -rf third_party/abseil-cpp

%build
# replace compiler flags to build with the proper debugging information
t=`mktemp /tmp/mozc.gyp-XXXXXXXX`
opts=$(for i in $(echo $RPM_OPT_FLAGS); do #|sed -e 's/-fstack-clash-protection//g' -e 's/-fcf-protection//g'); do
	echo "i \\"
	echo "\"$i\","
done)
sed -ne "/'linux_cflags':/{p;n;p;:a;/[[:space:]]*\],/{\
$opts
p;b b};n;b a;};{p};:b" gyp/common.gypi > $t && mv $t gyp/common.gypi || exit 1
GYP_DEFINES="use_libprotobuf=1 use_system_abseil_cpp=1 %{?with_zinnia:use_libzinnia=1 zinnia_model_file=/usr/share/zinnia/model/tomoe/handwriting-ja.model} %{!?with_zinnia:use_libzinnia=0} ibus_mozc_path=%{_libexecdir}/ibus-engine-mozc ibus_mozc_icon_path=%{_datadir}/ibus-mozc/product_icon.png" python build_mozc.py gyp --gypdir=%{_bindir} --server_dir=%{_libexecdir}/mozc --target_platform=Linux %{!?with_qt:--noqt}
python build_mozc.py build -c Release unix/ibus/ibus.gyp:ibus_mozc unix/emacs/emacs.gyp:mozc_emacs_helper server/server.gyp:mozc_server gui/gui.gyp:mozc_tool renderer/renderer.gyp:mozc_renderer

%install
install -d $RPM_BUILD_ROOT%{_libexecdir}/mozc
install -d $RPM_BUILD_ROOT%{_libexecdir}/mozc/documents
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/ibus/component
install -d $RPM_BUILD_ROOT%{_datadir}/ibus-mozc
install -d $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}
install -d $RPM_BUILD_ROOT%{_emacs_sitestartdir}

install -p -m0755 out_linux/Release/mozc_server $RPM_BUILD_ROOT%{_libexecdir}/mozc
install -p -m0755 out_linux/Release/mozc_tool $RPM_BUILD_ROOT%{_libexecdir}/mozc
install -p -m0755 out_linux/Release/mozc_renderer $RPM_BUILD_ROOT%{_libexecdir}/mozc
install -p -m0644 data/installer/credits_en.html $RPM_BUILD_ROOT%{_libexecdir}/mozc/documents

# ibus-mozc
install -p -m0755 %{SOURCE6} $RPM_BUILD_ROOT%{_libexecdir}/mozc
install -p -m0755 out_linux/Release/ibus_mozc $RPM_BUILD_ROOT%{_libexecdir}/ibus-engine-mozc
install -p -m0644 out_linux/Release/gen/unix/ibus/mozc.xml $RPM_BUILD_ROOT%{_datadir}/ibus/component/
(cd data/images/unix;
install -p -m0644 ime_product_icon_opensource-32.png $RPM_BUILD_ROOT%{_datadir}/ibus-mozc/product_icon.png
for i in ui-*.png; do
	install -p -m0644 $i $RPM_BUILD_ROOT%{_datadir}/ibus-mozc/${i//ui-/}
done)
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE4}
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_sysconfdir}/xdg/autostart %{SOURCE5}

# emacs-common-mozc
install -p -m0755 out_linux/Release/mozc_emacs_helper $RPM_BUILD_ROOT%{_bindir}

# emacs-mozc*
install -p -m0644 unix/emacs/mozc.el $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}
install -p -m0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}

emacs -batch -f batch-byte-compile $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/mozc.el

%if 0%{?fedora} < 36
# xemacs-mozc*
install -d $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/%{pkg}
install -d $RPM_BUILD_ROOT%{_xemacs_sitestartdir}
install -p -m0644 unix/emacs/mozc.el $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/%{pkg}
install -p -m0644 %{SOURCE1} $RPM_BUILD_ROOT%{_xemacs_sitestartdir}

xemacs -batch -f batch-byte-compile $RPM_BUILD_ROOT%{_xemacs_sitelispdir}/%{pkg}/mozc.el
%endif

# Register as an AppStream component to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
install -d -m 0755 %{buildroot}%{_metainfodir}
cat > %{buildroot}%{_metainfodir}/mozc.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>mozc.xml</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Mozc</name>
  <summary>Japanese input method</summary>
  <description>
    <p>
      The Mozc input method is designed for entering Japanese text.
      It is multi-platform and is available on Chromium OS, Windows, Mac and Linux.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://github.com/google/mozc</url>
  <url type="bugtracker">https://github.com/google/mozc/issues</url>
  <url type="help"><!-- https://code.google.com/p/ibus/wiki/FAQ --></url>
  <languages>
    <lang percentage="100">ja</lang>
  </languages>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%dir %{_libexecdir}/mozc
%{_bindir}/mozc_emacs_helper
%{_libexecdir}/mozc/mozc_server
%{_libexecdir}/mozc/mozc_tool
%{_libexecdir}/mozc/documents
%dir %{_emacs_sitelispdir}/%{pkg}
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitestartdir}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.el
%if 0%{?fedora} < 36
%dir %{_xemacs_sitelispdir}/%{pkg}
%{_xemacs_sitelispdir}/%{pkg}/*.elc
%{_xemacs_sitestartdir}/*.el
%{_xemacs_sitelispdir}/%{pkg}/*.el
%endif

%files	-n ibus-mozc
%dir %{_datadir}/ibus-mozc
%{_libexecdir}/mozc/ibus-mozc-launch-xwayland.sh
%{_libexecdir}/ibus-engine-mozc
%{_libexecdir}/mozc/mozc_renderer
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/ibus-setup-mozc-jp.desktop
%{_datadir}/ibus/component/mozc.xml
%{_datadir}/ibus-mozc/*.png
%{_sysconfdir}/xdg/autostart/ibus-mozc-launch-xwayland.desktop

%changelog
%autochangelog
