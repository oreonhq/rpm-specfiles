Name:    kde-dev-scripts
Summary: KDE SDK scripts
Version: 25.12.3
Release: 1%{?dist}

License: GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-only AND BSD-2-Clause
URL:     https://invent.kde.org/sdk/%{name}.git

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6DocTools)

BuildRequires:  perl-generators
BuildRequires:  python3-devel

Requires:       advancecomp
Requires:       optipng

BuildArch:      noarch

Conflicts:      kdesdk-common < 4.10.80
Provides:       kdesdk-scripts = %{version}-%{release}
Obsoletes:      kdesdk-scripts < 4.10.80

Conflicts: kde-l10n < 17.08.3-2

%description
KDE SDK scripts


%prep
%autosetup


%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man

%py3_shebang_fix %{buildroot}%{_kf6_bindir}/*

# unpackaged files
# This one fits better into krazy2 (it requires krazy2), and the version in
# kdesdk does not understand lib64.
rm -fv %{buildroot}%{_kf6_bindir}/krazy-licensecheck


%files -f %{name}.lang
%doc README
%license COPYING
%{_kf6_bindir}/grantlee_strings_extractor.py
%{_kf6_bindir}/c++-copy-class-and-file
%{_kf6_bindir}/c++-rename-class-and-file
%{_kf6_bindir}/svnrevertlast
%{_kf6_bindir}/fixuifiles
%{_kf6_bindir}/cvscheck
%{_kf6_bindir}/extend_dmalloc
%{_kf6_bindir}/extractattr
%{_kf6_bindir}/noncvslist
%{_kf6_bindir}/pruneemptydirs
%{_kf6_bindir}/cvsrevertlast
%{_kf6_bindir}/create_makefile
%{_kf6_bindir}/colorsvn
%{_kf6_bindir}/cvslastchange
%{_kf6_bindir}/svngettags
%{_kf6_bindir}/create_svnignore
%{_kf6_bindir}/svnchangesince
%{_kf6_bindir}/build-progress.sh
%{_kf6_bindir}/package_crystalsvg
%{_kf6_bindir}/svnbackport
%{_kf6_bindir}/svnlastlog
%{_kf6_bindir}/cxxmetric
%{_kf6_bindir}/kdemangen.pl
%{_kf6_bindir}/cvsforwardport
%{_kf6_bindir}/includemocs
%{_kf6_bindir}/svnlastchange
%{_kf6_bindir}/wcgrep
%{_kf6_bindir}/nonsvnlist
%{_kf6_bindir}/svnforwardport
%{_kf6_bindir}/create_cvsignore
%{_kf6_bindir}/svnintegrate
%{_kf6_bindir}/kdekillall
%{_kf6_bindir}/create_makefiles
%{_kf6_bindir}/cvsbackport
%{_kf6_bindir}/fixkdeincludes
%{_kf6_bindir}/kde-systemsettings-tree.py
%{_kf6_bindir}/zonetab2pot.py
%{_kf6_bindir}/kde_generate_export_header
%{_kf6_bindir}/cvs-clean
%{_kf6_bindir}/kdelnk2desktop.py
%{_kf6_bindir}/findmissingcrystal
%{_kf6_bindir}/adddebug
%{_kf6_bindir}/cvsversion
%{_kf6_bindir}/cheatmake
%{_kf6_bindir}/cvsblame
%{_kf6_bindir}/optimizegraphics
%{_kf6_bindir}/cvsaddcurrentdir
%{_kf6_bindir}/fix-include.sh
%{_kf6_bindir}/kdedoc
%{_kf6_bindir}/svn-clean
%{_kf6_bindir}/png2mng.pl
%{_kf6_bindir}/extractrc
%{_kf6_bindir}/makeobj
%{_kf6_bindir}/cvslastlog
%{_kf6_bindir}/svnversions
%{_kf6_bindir}/draw_lib_dependencies
%{_kf6_bindir}/reviewboard-am
%{_kf6_bindir}/uncrustify-kf5
%{_kf6_bindir}/clean-forward-declaration.sh
%{_kf6_bindir}/clean-includes.sh
%{_kf6_bindir}/addmocincludes
%{_kf6_bindir}/port_new_gitlab_ci_template.sh
%{_kf6_datadir}/uncrustify/
%{_mandir}/man1/adddebug.1*
%{_mandir}/man1/cheatmake.1*
%{_mandir}/man1/create_cvsignore.1*
%{_mandir}/man1/create_makefile.1*
%{_mandir}/man1/create_makefiles.1*
%{_mandir}/man1/cvscheck.1*
%{_mandir}/man1/cvslastchange.1*
%{_mandir}/man1/cvslastlog.1*
%{_mandir}/man1/cvsrevertlast.1*
%{_mandir}/man1/cxxmetric.1*
%{_mandir}/man1/extend_dmalloc.1*
%{_mandir}/man1/extractrc.1*
%{_mandir}/man1/fixincludes.1*
%{_mandir}/man1/pruneemptydirs.1*
%{_mandir}/man1/zonetab2pot.py.1*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
