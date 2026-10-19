%global source0_hash e8cfbc89372fad7a720d9d8f2539490407b2e8416f915c00223274892eaf7aad
Name:			diffuse
Version:		0.10.0
Release:        1%{?dist}
Summary:        Graphical tool for merging and comparing text files
License:		GPL-2.0-or-later
URL:			https://mightycreak.github.io/diffuse/
Source0:        https://codeload.github.com/MightyCreak/diffuse/tar.gz/v%{version}
BuildArch:		noarch
Requires:		gnome-icon-theme
Requires:		gnome-icon-theme-legacy
Requires:		hicolor-icon-theme
Requires:		python3-cairo
Requires:		python3-gobject
Provides:		difftool
Provides:		mergetool
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk-update-icon-cache
BuildRequires:  meson
BuildRequires:  python3-cairo
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
# /oreon:deps
%description
Diffuse is a graphical tool for merging and comparing text files. Diffuse is
able to compare an arbitrary number of files side-by-side and gives users the
ability to manually adjust line-matching and directly edit files. Diffuse can
also retrieve revisions of files from Bazaar, CVS, Darcs, Git, Mercurial,
Monotone, RCS, Subversion, and SVK repositories for comparison and merging.
This is the Python 3 fork of Diffuse.

%prep
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.mightycreak.Diffuse.desktop
%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
