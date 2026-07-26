%global source0_hash 9f51ad44d457104e26fe08c3e27b99e4c231ffe18b0ec76be8d63e62d176129f

Name:           chewing-editor
Version:        0.1.2
Release:        3%{?dist}
Summary:        Cross platform chewing user phrase editor
Summary(zh_TW): 跨平台酷音詞庫編輯器

# chewing-editor GPL-2.0-or-later
# gmock BSD-3-Clause
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://github.com/chewing/chewing-editor
Source0:        %{url}/releases/download/%{version}/chewing-editor-%{version}-Source.tar.gz
Source1:        %{url}/releases/download/%{version}/chewing-editor-%{version}-Source.tar.gz.asc
Source2:        https://chewing.im/.well-known/openpgpkey/hu/y84sdmnksfqswe7fxf5mzjg53tbdz8f5?l=release#/libchewing.pgp

BuildRequires:  cmake gcc-c++
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(chewing) >= 0.4.0
BuildRequires:  pkgconfig(gtest) >= 1.7.0
BuildRequires:  help2man
BuildRequires:  desktop-file-utils
BuildRequires:  gnupg2
Requires:       hicolor-icon-theme

%description
chewing-editor is a cross platform chewing user phrase editor. It provides a
easy way to manage user phrase. With it, user can customize their user phrase
to increase input performance.

%description -l zh_TW
chewing-editor 是一個跨平台的詞庫編輯器。它提供了簡單管理使用者詞庫的界面，
有了它，使用者可以自訂自己的詞庫來提高輸入效率。

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{name}-%{version}-Source

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/chewing-editor.desktop

%files
%license COPYING
%doc README.md
%{_bindir}/chewing-editor
%{_datadir}/applications/chewing-editor.desktop
%{_datadir}/icons/hicolor/scalable/apps/chewing-editor.svg
%{_datadir}/icons/hicolor/256x256/apps/chewing-editor.png
%{_mandir}/man1/chewing-editor.1.gz

%changelog
%autochangelog
