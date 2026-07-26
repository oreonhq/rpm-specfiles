%global source0_hash none

Name:			diffuse
Version:		0.10.0
Release:		2%{?dist}
Summary:		Graphical tool for merging and comparing text files
License:		GPL-2.0-or-later
URL:			https://mightycreak.github.io/diffuse/
Source0:		https://codeload.github.com/MightyCreak/diffuse/tar.gz/v%{version}
BuildArch:		noarch
BuildRequires:		autoconf
BuildRequires:		desktop-file-utils
BuildRequires:		gettext
BuildRequires:		glib2-devel
BuildRequires:		gtk-update-icon-cache
BuildRequires:		meson
BuildRequires:		python3-cairo
BuildRequires:		python3-devel
BuildRequires:		python3-gobject
Requires:		gnome-icon-theme
Requires:		gnome-icon-theme-legacy
Requires:		hicolor-icon-theme
Requires:		python3-cairo
Requires:		python3-gobject
Provides:		difftool
Provides:		mergetool

%description
Diffuse is a graphical tool for merging and comparing text files. Diffuse is
able to compare an arbitrary number of files side-by-side and gives users the
ability to manually adjust line-matching and directly edit files. Diffuse can
also retrieve revisions of files from Bazaar, CVS, Darcs, Git, Mercurial,
Monotone, RCS, Subversion, and SVK repositories for comparison and merging.
This is the Python 3 fork of Diffuse.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.mightycreak.Diffuse.desktop
%meson_test

%files -f %{name}.lang
%license COPYING
%doc AUTHORS CHANGELOG.md README.md
%config(noreplace) %{_sysconfdir}/diffuserc
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/io.github.mightycreak.Diffuse.desktop
%{_datadir}/gnome/help/%{name}/
%{_datadir}/icons/hicolor/*/apps/io.github.mightycreak*
%{_datadir}/appdata/io.github.mightycreak.Diffuse.appdata.xml
%{_datadir}/omf/%{name}/
%{_mandir}/man*/*
%{_mandir}/*/man*/*

%changelog
%autochangelog
