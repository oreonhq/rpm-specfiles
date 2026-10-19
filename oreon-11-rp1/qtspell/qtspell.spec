%global source0_hash faa7add9d771350a63e66bb6c9b91b130097c2399f6f85c2a9a0ea8e0ceb79d8
Name:           qtspell
Version:        1.0.2
Release:        4%{?dist}
Summary:        Spell checking for Qt text widgets
License:        GPL-3.0-or-later
URL:            https://github.com/manisandro/qtspell
Source0:        https://github.com/manisandro/qtspell/archive/%{version}/%{name}-%{version}.tar.gz
Requires:      iso-codes
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  enchant2-devel
BuildRequires:  gcc-c++
BuildRequires:  mingw32-enchant2
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qttools
BuildRequires:  mingw32-qt5-qttools-tools
BuildRequires:  mingw32-qt6-qtbase
BuildRequires:  mingw32-qt6-qttools
BuildRequires:  mingw64-enchant2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qttools
BuildRequires:  mingw64-qt5-qttools-tools
BuildRequires:  mingw64-qt6-qtbase
BuildRequires:  mingw64-qt6-qttools
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
# /oreon:deps
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
%oreon_prep
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qtspell-qt5 -f %{oreon_filedir}/qtspell-qt5.list
%files -n qtspell-qt5-devel -f %{oreon_filedir}/qtspell-qt5-devel.list
%files -n qtspell-qt5-translations -f %{oreon_filedir}/qtspell-qt5-translations.list
%files -n qtspell-qt6 -f %{oreon_filedir}/qtspell-qt6.list
%files -n qtspell-qt6-devel -f %{oreon_filedir}/qtspell-qt6-devel.list
%files -n qtspell-qt6-translations -f %{oreon_filedir}/qtspell-qt6-translations.list
%files -n qtspell-doc -f %{oreon_filedir}/qtspell-doc.list
%files -n mingw32-qtspell-qt5 -f %{oreon_filedir}/mingw32-qtspell-qt5.list
%files -n mingw64-qtspell-qt5 -f %{oreon_filedir}/mingw64-qtspell-qt5.list
%files -n mingw32-qtspell-qt6 -f %{oreon_filedir}/mingw32-qtspell-qt6.list
%files -n mingw64-qtspell-qt6 -f %{oreon_filedir}/mingw64-qtspell-qt6.list

%changelog

%autochangelog
