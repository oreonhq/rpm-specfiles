%global source0_hash 9084f93eccd3b865d638ae8cb989bcb334edea6f550ba6874a282048284fcccc
%bcond pstoedit 1
%bcond marble 0
%bcond visio 1
%bcond wpd 1
%bcond okular 1
Name:    calligra 
Version: 26.08.1
Release:        1%{?dist}
Summary:        An integrated office suite
License: GPL-2.0-or-later AND GPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-3-Clause AND BSD-2-Clause
URL:     https://calligra.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch200: calligra-disable_products.patch
ExcludeArch: %{ix86}
%ifarch %{qt6_qtwebengine_arches}
%endif
%if %{with marble}
%endif
%if %{with wpd}
%if %{with visio}
%endif
%endif
Requires:  %{name}-words%{?_isa} = %{version}-%{release}
Requires:  %{name}-sheets%{?_isa} = %{version}-%{release}
Requires:  %{name}-stage%{?_isa} = %{version}-%{release}
Requires:  %{name}-karbon%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake(Imath)
BuildRequires:  cmake(KChart6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Okular6)
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libetonyek-0.1)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libodfgen-0.1)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libwpd-0.10)
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libwps-0.4)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pstoedit
BuildRequires:  zlib-devel
# /oreon:deps
%description
%{summary}.

%package data
Summary: Runtime support files for %{name}
%if %{undefined flatpak}
Requires: color-filesystem
%endif
%if 0%{?external_lilypond_fonts}
Requires: lilypond-emmentaler-fonts
%endif
Obsoletes: %{name}-core < 4
%if %{without okular}
Obsoletes: %{name}-okular-odpgenerator < %{version}-%{release}
Obsoletes: %{name}-okular-odtgenerator < %{version}-%{release}
%endif
BuildArch: noarch
%description data
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name}-data = %{version}-%{release}
%description libs
%{summary}.

%package l10n
Summary: Language files for calligra
Requires: %{name}-data = %{version}-%{release}
BuildArch: noarch
%description l10n
%{summary}.

%package  words
Summary:  An intuitive word processor application with desktop publishing features
Requires: %{name}-words-libs%{?_isa} = %{version}-%{release}
%description words
KWord is an intuitive word processor and desktop publisher application.
With it, you can create informative and attractive documents with
pleasure and ease.

%package  words-libs
Summary:  Runtime libraries for %{name}-words
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description words-libs
%{summary}.

%package  sheets 
Summary:  A fully-featured spreadsheet application
Requires: %{name}-sheets-libs%{?_isa} = %{version}-%{release}
%description sheets 
Tables is a fully-featured calculation and spreadsheet tool.  Use it to
quickly create and calculate various business-related spreadsheets, such
as income and expenditure, employee working hours…

%package  sheets-libs
Summary:  Runtime libraries for %{name}-sheets
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description sheets-libs
%{summary}.

%package  stage 
Summary:  A full-featured presentation program
Requires: %{name}-stage-libs%{?_isa} = %{version}-%{release}
%description stage 
Stage is a powerful and easy to use presentation application. You
can dazzle your audience with stunning slides containing images, videos,
animation and more.

%package  stage-libs
Summary:  Runtime libraries for %{name}-stage
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description stage-libs
%{summary}.

%package  karbon
Summary:  A vector drawing application
Requires: %{name}-karbon-libs%{?_isa} = %{version}-%{release}
%if %{with pstoedit}
BuildRequires: pstoedit
Requires: pstoedit
%endif
%description karbon
Karbon is a vector drawing application with an user interface that is
easy to use, highly customizable and extensible. That makes Karbon a
great application for users starting to explore the world of vector
graphics as well as for artists wanting to create breathtaking vector
art.

Whether you want to create clipart, logos, illustrations or photorealistic
vector images – look no further, Karbon is the tool for you!

%package  karbon-libs
Summary:  Runtime libraries for %{name}-karbon
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description karbon-libs
%{summary}.

%if %{with okular}
%package  okular-odpgenerator
Summary:  OpenDocument presenter support for okular
BuildRequires: cmake(Okular6)
Requires: %{name}-stage-libs%{?_isa} = %{version}-%{release}
Requires: okular-part
Supplements: (%{name}-stage and okular)
%description okular-odpgenerator
%{summary}.

%package  okular-odtgenerator
Summary:  OpenDocument text support for okular
BuildRequires: cmake(Okular6)
Requires: %{name}-words-libs%{?_isa} = %{version}-%{release}
Requires: okular-part
Supplements: (%{name}-words and okular)
%description okular-odtgenerator
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 \
  -Wno-dev
%cmake_build
%install
%cmake_install
%if 0%{?external_lilypond_fonts}
rm -fv %{buildroot}%{_kf6_datadir}/calligra_shape_music/fonts/Emmentaler-14.ttf
%endif
rm -frv %{buildroot}%{_kf6_datadir}/locale/x-test/
%find_lang %{name} --all-name --with-html
%oreon_autofiles calligra-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calligra-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calligra-l10n usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calligra-words usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calligra-words-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calligra-sheets usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calligra-sheets-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calligra-stage usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calligra-stage-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calligra-karbon usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calligra-karbon-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calligra-okular-odpgenerator usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles calligra-okular-odtgenerator usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

for appdata_file in %{buildroot}%{_kf6_metainfodir}/*.metainfo.xml ; do
appstream-util validate-relax --nonet ${appdata_file} ||:
done
for desktop_file in %{buildroot}%{_datadir}/applications/*.desktop ; do
desktop-file-validate ${desktop_file}  ||:
done
%files -f %{oreon_filedir}/main.list
%files -n calligra-data -f %{oreon_filedir}/calligra-data.list
%files -n calligra-libs -f %{oreon_filedir}/calligra-libs.list
%files -n calligra-l10n -f %{oreon_filedir}/calligra-l10n.list
%files -n calligra-words -f %{oreon_filedir}/calligra-words.list
%files -n calligra-words-libs -f %{oreon_filedir}/calligra-words-libs.list
%files -n calligra-sheets -f %{oreon_filedir}/calligra-sheets.list
%files -n calligra-sheets-libs -f %{oreon_filedir}/calligra-sheets-libs.list
%files -n calligra-stage -f %{oreon_filedir}/calligra-stage.list
%files -n calligra-stage-libs -f %{oreon_filedir}/calligra-stage-libs.list
%files -n calligra-karbon -f %{oreon_filedir}/calligra-karbon.list
%files -n calligra-karbon-libs -f %{oreon_filedir}/calligra-karbon-libs.list
%files -n calligra-okular-odpgenerator -f %{oreon_filedir}/calligra-okular-odpgenerator.list
%files -n calligra-okular-odtgenerator -f %{oreon_filedir}/calligra-okular-odtgenerator.list

%changelog

%autochangelog
