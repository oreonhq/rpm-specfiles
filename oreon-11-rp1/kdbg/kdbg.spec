Name: kdbg
Summary: A GUI for gdb, the GNU debugger, and KDE
Version: 3.2.0
Release:	4%{?dist}
Epoch: 1
Source: http://download.sourceforge.net/kdbg/%{name}-%{version}.tar.gz
# No version specified.
License: GPL-1.0-or-later
URL: http://www.kdbg.org/

Requires: gdb
Requires: xterm

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6WindowSystem)

%description
KDbg is a K Desktop Environment (KDE) GUI for gdb, the GNU debugger.
KDbg provides the programmer with an intuitive interface for setting
breakpoints, inspecting variables, and stepping through code. KDbg
requires X and KDE to be installed in order to run.

%prep
%setup -q

%build
%cmake_kf6 -DBUILD_FOR_KDE_VERSION=6

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --with-html

%files -f %{name}.lang
%doc BUGS COPYING README TODO ReleaseNotes-*
%config (noreplace) /etc/xdg/kdbgrc
%{_bindir}/*
%{_datadir}/kxmlgui5/%{name}
%{_datadir}/applications/*
%{_kf6_datadir}/%{name}
%{_datadir}/icons/*/*/*/*

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.2.0-3
- Prepare for Oreon 11 (RP1)
