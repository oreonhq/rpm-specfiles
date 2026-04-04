%global		framework kcodecs

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:		kf6-%{framework}
Version:	6.24.0
Release:	8%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with string manipulation methods
License:	BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND MPL-1.1
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:	http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:	fdupes
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	gperf
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel

Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 addon with string manipulation methods.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	html
Summary:	Developer Documentation files for %{name} in HTML format
BuildArch:	noarch
%description	html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6
# Fedora rawhide spec uses %%{_qt6_docdir}/*/* here, which only matches two path
# segments under docdir (e.g. kcodecs/page.html). Current qdoc also drops CSS under
# kcodecs/style/, which is three segments, so a plain paste leaves those unpackaged.
# This find is the only intentional delta from Fedora's %%files html.
# Fedora also has a -doc package for %%{_qt6_docdir}/*.qch. %%cmake_kf6 sets
# BUILD_QCH OFF and QCH targets are EXCLUDE_FROM_ALL, so that glob often matches
# nothing and breaks the build. Ship QCH paths here when they exist.
: > %{_builddir}/kcodecs-html.files
if [ -d "%{buildroot}%{_qt6_docdir}/%{framework}" ]; then
  find "%{buildroot}%{_qt6_docdir}/%{framework}" -type f \
    ! -name '*.tags' ! -name '*.index' \
    | sed "s#^%{buildroot}##" >> %{_builddir}/kcodecs-html.files
fi
for f in "%{buildroot}%{_qt6_docdir}"/*.qch; do
  [ -f "$f" ] || continue
  printf '%s\n' "${f#%{buildroot}}" >> %{_builddir}/kcodecs-html.files
done
LC_ALL=C sort -u -o %{_builddir}/kcodecs-html.files %{_builddir}/kcodecs-html.files

%find_lang_kf6 kcodecs6_qt
%fdupes LICENSES

%files -f kcodecs6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6Codecs.so.*

%files devel
%{_kf6_includedir}/KCodecs/
%{_kf6_libdir}/libKF6Codecs.so
%{_kf6_libdir}/cmake/KF6Codecs/
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files html -f %{_builddir}/kcodecs-html.files

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-8
- Drop separate -doc (*.qch) subpackage, merge optional QCH paths into -html list

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-7
- Match Fedora spec

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
