%global source0_hash 6966c286b71239304c5038b419ae67dd2492c235c024186e7dd581fef1dad29f
%global bigname QXmlEdit
Name:           qxmledit
Version:        0.9.18
Release:        1%{?dist}
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-3.0-only AND Zlib
Summary:        Simple XML Editor and XSD Viewer
Url:            http://qxmledit.org/
Source0:        https://github.com/lbellonda/qxmledit/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       libqxmledit%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Scxml)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(glu)
BuildRequires:  qt5-linguist
# /oreon:deps
%description
QXmlEdit is a simple XML editor based on qt libraries. Its main features are
unusual data visualization modes, nice XML manipulation and presentation and it
is multi platform. It can split very big XML files into fragments, and compare
XML files. It is one of the few graphical Open Source XSD viewers.

%package        doc
Summary:        Simple XML Editor documentatio
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
QXmlQXmlEdit is a simple XML editor based on qt libraries.
This package includes QXmlEdit documentation.

%package -n     libqxmledit
Summary:        XML Editor Shared Libraries
%description -n libqxmledit
QXmlQXmlEdit is a simple XML editor based on qt libraries.
This package includes QXmlEdit shared libraries.

%package -n     libqxmledit-devel
Summary:        XML Editor Development Files
Requires:       libqxmledit%{?_isa} = %{version}-%{release}
%description -n libqxmledit-devel
QXmlEdit is a simple XML editor based on qt libraries.
This package includes QXmlEdit development files.

%prep

%autosetup
# tmp fix (https://github.com/lbellonda/qxmledit/issues/74)
desktop-file-edit --add-mime-type=application/xml install_scripts/environment/desktop/%{bigname}.desktop

%build

lrelease-qt5 {src/QXmlEdit.pro,src/QXmlEditWidget.pro,src/sessions/QXmlEditSessions.pro}
%{qmake_qt5} \
    QXMLEDIT_INST_DIR=%{_bindir} \
    QXMLEDIT_INST_LIB_DIR=%{_libdir} \
    QXMLEDIT_INST_DATA_DIR=%{_datadir}/%{name} \
    QXMLEDIT_INST_TRANSLATIONS_DIR=%{_datadir}/%{name}/translations \
    QXMLEDIT_INST_INCLUDE_DIR=%{_includedir}/%{name} \
    QXMLEDIT_INST_ICON_DIR=%{_datadir}/pixmaps \
    QXMLEDIT_INST_DOC_DIR=%{_datadir}/doc/%{name} \
    QXMLEDIT_INST_DESKTOPINFO_DIR=%{_datadir}/applications \
    QXMLEDIT_INST_METAINFO_DIR=%{_metainfodir} \
    QXMLEDIT_INST_USE_C11=y
%{make_build}
%install
%{make_install} INSTALL_ROOT=%{buildroot}
install -Dm 0644 install_scripts/environment/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%find_lang QXmlEdit --with-qt --without-mo
%find_lang QXmlEditSessions --with-qt --without-mo
%find_lang QXmlEditWidget --with-qt --without-mo
%find_lang SCXML --with-qt --without-mo
%oreon_autofiles libqxmledit usr/*/lib*.so.*
%oreon_autofiles libqxmledit-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{bigname}.desktop
%files -f %{oreon_filedir}/main.list
%files -n qxmledit-doc -f %{oreon_filedir}/qxmledit-doc.list
%files -n libqxmledit -f %{oreon_filedir}/libqxmledit.list
%files -n libqxmledit-devel -f %{oreon_filedir}/libqxmledit-devel.list

%changelog

%autochangelog
