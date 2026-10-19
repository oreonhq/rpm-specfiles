%global source0_hash ccdd172a2bc8a0c57fe8982cdc3cb3856da42ba78936c7837f43b30d4ad20bb5
Name:           bibletime
Version:        3.2.0
Release:        1%{?dist}
Summary:        An easy to use Bible study tool
License:        GPL-2.0-only
URL:            http://www.bibletime.info/
Source0:        http://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
ExclusiveArch:  %{qt6_qtwebengine_arches}
# oreon:deps
BuildRequires:  clucene-core-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  fop
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  po4a
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  sword-devel
# /oreon:deps
%description
BibleTime is a free and easy to use cross-platform bible study tool. It
provides easy handling of digitalized texts (Bibles, commentaries and
lexicons) and powerful features to work with these texts (search in
texts, write own notes, save, print etc.). BibleTime is a frontend for
the SWORD Bible Framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
mv %{buildroot}%{_docdir}/%{name}/handbook/html/{br,BR} || :
mv %{buildroot}%{_docdir}/%{name}/handbook/pdf/{br,BR} || :
mv %{buildroot}%{_docdir}/%{name}/howto/html/{br,BR} || :
mv %{buildroot}%{_docdir}/%{name}/howto/pdf/{br,BR} || :
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
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/info.%{name}.BibleTime.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
