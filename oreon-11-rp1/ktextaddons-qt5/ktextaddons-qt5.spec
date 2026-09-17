%global source0_hash 64b80602e84b25e9164620af3f6341fa865b85e826ab8f5e02061ae24a277b20

Name:          ktextaddons-qt5
Version:       1.5.4
Release:       6%{?dist}
Summary:       Various text handling addons

License:       CC0-1.0 AND LGPL-2.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause

URL:           https://invent.kde.org/libraries/%{name}

Source0:       http://download.kde.org/stable/ktextaddons/ktextaddons-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules

BuildRequires: kf5-rpm-macros

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: cmake(Qt5TextToSpeech)
BuildRequires: cmake(Qt5UiPlugin)

BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5SyntaxHighlighting)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ktextaddons-%{version} -p1
# allow parallel installability with newer qt6-only ktextaddons
sed -i -e '/DTRANSLATION_DOMAIN/s/libtext[[:alpha:]]\+/&5/' text*/CMakeLists.txt
rename .po 5.po po/*/*.po

%build
%cmake_kf5 -DQT_MAJOR_VERSION=5
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/
%doc README.md
%{_kf5_libdir}/libKF5TextAddonsWidgets.so.1
%{_kf5_libdir}/libKF5TextAddonsWidgets.so.%{version}
%{_kf5_libdir}/libKF5TextAutoCorrectionCore.so.1
%{_kf5_libdir}/libKF5TextAutoCorrectionCore.so.%{version}
%{_kf5_libdir}/libKF5TextAutoCorrectionWidgets.so.1
%{_kf5_libdir}/libKF5TextAutoCorrectionWidgets.so.%{version}
%{_kf5_libdir}/libKF5TextCustomEditor.so.1
%{_kf5_libdir}/libKF5TextCustomEditor.so.%{version}
%{_kf5_libdir}/libKF5TextEmoticonsCore.so.1
%{_kf5_libdir}/libKF5TextEmoticonsCore.so.%{version}
%{_kf5_libdir}/libKF5TextEmoticonsWidgets.so.1
%{_kf5_libdir}/libKF5TextEmoticonsWidgets.so.%{version}
%{_kf5_libdir}/libKF5TextEditTextToSpeech.so.1
%{_kf5_libdir}/libKF5TextEditTextToSpeech.so.%{version}
%{_kf5_libdir}/libKF5TextGrammarCheck.so.1
%{_kf5_libdir}/libKF5TextGrammarCheck.so.%{version}
%{_kf5_libdir}/libKF5TextTranslator.so.1
%{_kf5_libdir}/libKF5TextTranslator.so.%{version}
%{_kf5_libdir}/libKF5TextUtils.so.1
%{_kf5_libdir}/libKF5TextUtils.so.%{version}
%{_kf5_plugindir}/translator/translator_bing.so
%{_kf5_plugindir}/translator/translator_deepl.so
%{_kf5_plugindir}/translator/translator_google.so
%{_kf5_plugindir}/translator/translator_libretranslate.so
%{_kf5_plugindir}/translator/translator_lingva.so
%{_kf5_plugindir}/translator/translator_yandex.so
%{_kf5_datadir}/qlogging-categories5/ktextaddons.categories
%{_kf5_datadir}/qlogging-categories5/ktextaddons.renamecategories

%files devel
%{_kf5_includedir}/TextAddonsWidgets/
%{_kf5_includedir}/TextAutoCorrectionCore/
%{_kf5_includedir}/TextAutoCorrectionWidgets/
%{_kf5_includedir}/TextCustomEditor/
%{_kf5_includedir}/TextEditTextToSpeech/
%{_kf5_includedir}/TextEmoticonsCore/
%{_kf5_includedir}/TextEmoticonsWidgets/
%{_kf5_includedir}/TextGrammarCheck/
%{_kf5_includedir}/TextTranslator/
%{_kf5_includedir}/TextUtils/
%{_kf5_libdir}/libKF5TextAddonsWidgets.so
%{_kf5_libdir}/libKF5TextAutoCorrectionCore.so
%{_kf5_libdir}/libKF5TextAutoCorrectionWidgets.so
%{_kf5_libdir}/libKF5TextCustomEditor.so
%{_kf5_libdir}/libKF5TextEditTextToSpeech.so
%{_kf5_libdir}/libKF5TextEmoticonsCore.so
%{_kf5_libdir}/libKF5TextEmoticonsWidgets.so
%{_kf5_libdir}/libKF5TextGrammarCheck.so
%{_kf5_libdir}/libKF5TextTranslator.so
%{_kf5_libdir}/libKF5TextUtils.so
%{_kf5_libdir}/cmake/KF5TextAddonsWidgets/
%{_kf5_libdir}/cmake/KF5TextAutoCorrectionCore/
%{_kf5_libdir}/cmake/KF5TextAutoCorrectionWidgets/
%{_kf5_libdir}/cmake/KF5TextCustomEditor/
%{_kf5_libdir}/cmake/KF5TextEmoticonsCore/
%{_kf5_libdir}/cmake/KF5TextEmoticonsWidgets/
%{_kf5_libdir}/cmake/KF5TextEditTextToSpeech/
%{_kf5_libdir}/cmake/KF5TextGrammarCheck/
%{_kf5_libdir}/cmake/KF5TextTranslator/
%{_kf5_libdir}/cmake/KF5TextUtils/
%{_kf5_qtplugindir}/designer/textcustomeditor.so
%{_kf5_qtplugindir}/designer/texttranslatorwidgets5.so

%changelog
%autochangelog
