%global source0_hash 547f2f28073fc791c9d52fa5fd7d66d92c42c7d7fecba05ce1e4b55278ff8cd4

#debug info would be empty due to no binarys
%global debug_package %{nil}

Name: bless
Version: 0.6.3
Release: 19%{?dist}
Summary: High quality, full featured hex editor    

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later        
URL: https://github.com/afrantzis/bless/
Source0: https://github.com/afrantzis/bless/archive/v%{version}.tar.gz
Source1: bless.metainfo.xml
Patch1: bless-0.6.2-default-editmode-overwrite.patch
Patch2: bless-0.6.3-fix-reloading-file.patch

BuildRequires:  gcc
BuildRequires: mono-devel
BuildRequires: gtk-sharp2-devel     
BuildRequires: desktop-file-utils
BuildRequires: rarian-compat
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: gettext-devel
BuildRequires: nunit-devel
BuildRequires: docbook-style-xsl
BuildRequires: itstool
BuildRequires: libappstream-glib

Requires: mono-core
Requires: gtk-sharp2

Obsoletes: %{name}-doc < 0.6.3-11

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
Bless is a binary (hex) editor, a program that 
enables you to edit files as sequences of bytes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .editmodeoverwrite
%patch -P2 -p1 -b .fixreloadingfile
sed -i "s~html_xsl = 'http://docbook.sourceforge.net/release/xsl/current/html/chunk.xsl'~html_xsl = '/usr/share/sgml/docbook/xsl-stylesheets-1.79.2/xhtml/chunk.xsl'~" doc/user/meson.build

%build
%meson
%meson_build

%install
%meson_install

desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/bless.desktop

install -D -m0644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_metainfodir}/bless.metainfo.xml
appstream-util validate-relax --nonet ${RPM_BUILD_ROOT}%{_metainfodir}/bless.metainfo.xml

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/bless
%{_libdir}/bless/
%{_datadir}/bless/
%{_datadir}/icons/hicolor/48x48/apps/bless.png
%{_datadir}/applications/bless.desktop
%{_metainfodir}/bless.metainfo.xml

%changelog
%autochangelog
