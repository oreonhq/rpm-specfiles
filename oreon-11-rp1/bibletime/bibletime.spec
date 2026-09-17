%global source0_hash 71dbafdc8d29518aede79269d027d80b4192633e7a614c89ed76aeb0e0bd1dd4

Name:           bibletime
Version:        3.1.1
Release:        3%{?dist}
Summary:        An easy to use Bible study tool
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.bibletime.info/
Source0:        http://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

# These lack qtwebengine/qtwebkit
ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  gcc-c++
BuildRequires:  clucene-core-devel >= 2.0
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(QtGui) >= 4.5.0
BuildRequires:  sword-devel >= 1.8.1-15
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  po4a
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  make

# fop is java_arches exclusive
# However, this line is more inclusive of arches that do not have
# qtwebengine
#ExclusiveArch:  %{java_arches}
BuildRequires:  fop

%description
BibleTime is a free and easy to use cross-platform bible study tool. It
provides easy handling of digitalized texts (Bibles, commentaries and
lexicons) and powerful features to work with these texts (search in
texts, write own notes, save, print etc.). BibleTime is a frontend for
the SWORD Bible Framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install

# rename wrongly-named locale
mv %{buildroot}%{_docdir}/%{name}/handbook/html/{br,BR} || :
mv %{buildroot}%{_docdir}/%{name}/handbook/pdf/{br,BR} || :
mv %{buildroot}%{_docdir}/%{name}/howto/html/{br,BR} || :
mv %{buildroot}%{_docdir}/%{name}/howto/pdf/{br,BR} || :

# locale's
%find_lang %{name} || touch %{name}.lang
BT_DOC_DIR=%{_docdir}/%{name}/
for doctype in handbook howto ; do
	for fmt in html pdf; do
		for lang_dir in %{buildroot}/$BT_DOC_DIR/$doctype/$fmt/* ; do
			lang=$(basename $lang_dir)
			echo "%lang($lang) $BT_DOC_DIR/$doctype/$fmt/$lang/*" >> %{name}.lang
		done
	done
done

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/info.%{name}.BibleTime.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/info.%{name}.BibleTime.desktop
%dir %{_datadir}/%{name}
%dir %{_docdir}/%{name}/handbook/
%dir %{_docdir}/%{name}/howto/
%{_datadir}/%{name}/display-templates/
%{_datadir}/%{name}/icons/
%{_datadir}/%{name}/license/
%{_datadir}/%{name}/locale/
%{_datadir}/%{name}/pics/
%{_datadir}/metainfo/info.%{name}.BibleTime.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/info.%{name}.BibleTime.svg

%changelog
%autochangelog
