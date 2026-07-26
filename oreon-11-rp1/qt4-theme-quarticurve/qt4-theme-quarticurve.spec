%global source0_hash baddbc2aeca7c3dfbd9449b40868e1d3ded38768c845479574c773857b729a87

Name: qt4-theme-quarticurve
Version: 0.0
Release: 0.48.beta8%{?dist}
URL: http://www.kde-look.org/content/show.php/Quarticurve?content=59884
# downloadable from URL above
Source: quarticurve-beta8.tar.bz2
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
BuildRequires: make
BuildRequires: kdelibs4-devel
Requires: kde-filesystem >= 4-7

Summary: Unofficial port of the Bluecurve widget theme to Qt 4
%description
Quarticurve is an unofficial port of Red Hat's Bluecurve Qt 3 widget theme to
Qt 4.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n quarticurve-beta8

%build
%{qmake_qt4}
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT

%files
%{_qt4_plugindir}/styles/libquarticurve.so
%{_kde4_appsdir}/color-schemes/Quarticurve.colors
%doc COPYING ChangeLog readme.txt

%changelog
%autochangelog
