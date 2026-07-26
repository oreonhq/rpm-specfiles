%global source0_hash faa7add9d771350a63e66bb6c9b91b130097c2399f6f85c2a9a0ea8e0ceb79d8

Name:           qtspell
Version:        1.0.2
Release:        4%{?dist}
Summary:        Spell checking for Qt text widgets

License:        GPL-3.0-or-later
URL:            https://github.com/manisandro/qtspell
Source0:        https://github.com/manisandro/qtspell/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  enchant2-devel
BuildRequires:  doxygen

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-enchant2
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-qt5-qttools
BuildRequires: mingw32-qt5-qttools-tools
BuildRequires: mingw32-qt6-qtbase
BuildRequires: mingw32-qt6-qttools

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-enchant2
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-qt5-qttools
BuildRequires: mingw64-qt5-qttools-tools
BuildRequires: mingw64-qt6-qtbase
BuildRequires: mingw64-qt6-qttools

Requires:      iso-codes

%description
QtSpell adds spell-checking functionality to Qt's text widgets, using the
enchant spell-checking library.

%package        qt5
Summary:        Spell checking for Qt5 text widgets

%description    qt5
QtSpell adds spell-checking functionality to Qt5's text widgets, using the
enchant spell-checking library.

%package        qt5-devel
Summary:        Development files for %{name}-qt5
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}

%description    qt5-devel
The %{name}-qt5-devel package contains libraries and header files for
developing applications that use %{name}-qt5.

%package        qt5-translations
Summary:        Translations for %{name}-qt5
BuildArch:      noarch
Requires:       %{name}-qt5 = %{version}-%{release}
Requires:       qt5-qttranslations

%description    qt5-translations
The %{name}-qt5-translations contains translations for %{name}-qt5.

%package        qt6
Summary:        Spell checking for Qt6 text widgets

%description    qt6
QtSpell adds spell-checking functionality to Qt6's text widgets, using the
enchant spell-checking library.

%package        qt6-devel
Summary:        Development files for %{name}-qt6
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}

%description    qt6-devel
The %{name}-qt6-devel package contains libraries and header files for
developing applications that use %{name}-qt6.

%package        qt6-translations
Summary:        Translations for %{name}-qt6
BuildArch:      noarch
Requires:       %{name}-qt6 = %{version}-%{release}
Requires:       qt6-qttranslations

%description    qt6-translations
The %{name}-qt6-translations contains translations for %{name}-qt6.

%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the documentation for developing applications
that use %{name}.

%package -n mingw32-%{name}-qt5
Summary:       MinGW Windows %{name}-Qt5 library
Requires:      mingw32-qt5-qttranslations
BuildArch:     noarch

%description -n mingw32-%{name}-qt5
MinGW Windows %{name}-Qt5 library.

%package -n mingw64-%{name}-qt5
Summary:       MinGW Windows %{name}-Qt5 library
Requires:      mingw64-qt5-qttranslations
BuildArch:     noarch

%description -n mingw64-%{name}-qt5
MinGW Windows %{name}-Qt5 library.

%package -n mingw32-%{name}-qt6
Summary:       MinGW Windows %{name}-Qt6 library
Requires:      mingw32-qt6-qttranslations
BuildArch:     noarch

%description -n mingw32-%{name}-qt6
MinGW Windows %{name}-Qt6 library.

%package -n mingw64-%{name}-qt6
Summary:       MinGW Windows %{name}-Qt6 library
Requires:      mingw64-qt6-qttranslations
BuildArch:     noarch

%description -n mingw64-%{name}-qt6
MinGW Windows %{name}-Qt6 library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%define _vpath_builddir %{_target_platform}-qt5
%cmake -DQT_VER=5
%cmake_build

%define _vpath_builddir %{_target_platform}-qt6
%cmake -DQT_VER=6
%cmake_build

%cmake_build --target doc

export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
%mingw_cmake -DQT_VER=5
%mingw_make_build

MINGW_BUILDDIR_SUFFIX=qt6 %mingw_cmake -DQT_VER=6
MINGW_BUILDDIR_SUFFIX=qt6 %mingw_make_build

%install
%define _vpath_builddir %{_target_platform}-qt5
%cmake_install

%define _vpath_builddir %{_target_platform}-qt6
%cmake_install

%mingw_make_install
MINGW_BUILDDIR_SUFFIX=qt6 %mingw_make_install

%mingw_debug_install_post

%files qt5
%license COPYING
%{_libdir}/libqtspell-qt5.so.*

%files qt5-devel
%{_includedir}/QtSpell-qt5/
%{_libdir}/libqtspell-qt5.so
%{_libdir}/pkgconfig/QtSpell-qt5.pc

%files qt5-translations
%{_qt5_translationdir}/QtSpell_*.qm

%files qt6
%license COPYING
%{_libdir}/libqtspell-qt6.so.*

%files qt6-devel
%{_includedir}/QtSpell-qt6/
%{_libdir}/libqtspell-qt6.so
%{_libdir}/pkgconfig/QtSpell-qt6.pc

%files qt6-translations
%{_qt6_translationdir}/QtSpell_*.qm

%files -n mingw32-%{name}-qt5
%license COPYING
%{mingw32_bindir}/libqtspell-qt5-1.dll
%{mingw32_libdir}/libqtspell-qt5.dll.a
%{mingw32_libdir}/pkgconfig/QtSpell-qt5.pc
%{mingw32_includedir}/QtSpell-qt5/
%{mingw32_datadir}/qt5/translations/QtSpell_*.qm

%files -n mingw64-%{name}-qt5
%license COPYING
%{mingw64_bindir}/libqtspell-qt5-1.dll
%{mingw64_libdir}/libqtspell-qt5.dll.a
%{mingw64_libdir}/pkgconfig/QtSpell-qt5.pc
%{mingw64_includedir}/QtSpell-qt5/
%{mingw64_datadir}/qt5/translations/QtSpell_*.qm

%files -n mingw32-%{name}-qt6
%license COPYING
%{mingw32_bindir}/libqtspell-qt6-1.dll
%{mingw32_libdir}/libqtspell-qt6.dll.a
%{mingw32_libdir}/pkgconfig/QtSpell-qt6.pc
%{mingw32_includedir}/QtSpell-qt6/
%{mingw32_datadir}/qt6/translations/QtSpell_*.qm

%files -n mingw64-%{name}-qt6
%license COPYING
%{mingw64_bindir}/libqtspell-qt6-1.dll
%{mingw64_libdir}/libqtspell-qt6.dll.a
%{mingw64_libdir}/pkgconfig/QtSpell-qt6.pc
%{mingw64_includedir}/QtSpell-qt6/
%{mingw64_datadir}/qt6/translations/QtSpell_*.qm

%files doc
%license COPYING
%doc %{__cmake_builddir}/doc/html

%changelog
%autochangelog
