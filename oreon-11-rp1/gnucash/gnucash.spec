%global source0_hash 3d18a88f5b8230f01e04c2d2d73bf95e7dcd3bf8d8cee6ffa54bb24dee58b85f
Name: gnucash
Summary:        Finance management application
Version: 5.17
URL: https://gnucash.org/
Release:        1%{?dist}
License: GPL-2.0-or-later
Source0:        https://downloads.sourceforge.net/sourceforge/gnucash/gnucash-%{version}.tar.bz2
ExcludeArch: %{ix86}
Patch0: rpath.patch
Patch1: no-implicit.patch
ExcludeArch: ppc64 s390x
%global guilever 2.0
%if %{defined el8}
%else
%endif
Requires: gnucash-docs >= %{version}
Requires: dconf
Requires: perl(Finance::Quote)
Requires: perl(JSON::Parse)
Requires: perl(Getopt::Std)
Requires: gnome-icon-theme
Recommends: libdbi-dbd-sqlite
Suggests: libdbi-dbd-mysql
Suggests: libdbi-dbd-pgsql
# oreon:deps
BuildRequires:  aqbanking-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glib2
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  gtk3
BuildRequires:  guile-devel
BuildRequires:  gwenhywfar-gui-gtk3-devel
BuildRequires:  libappstream-glib
BuildRequires:  libdbi-dbd-mysql
BuildRequires:  libdbi-dbd-pgsql
BuildRequires:  libdbi-dbd-sqlite
BuildRequires:  libdbi-devel
BuildRequires:  libofx-devel
BuildRequires:  libsecret-devel
BuildRequires:  libxml2
BuildRequires:  libxslt-devel
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  swig
BuildRequires:  webkit2gtk4.1-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
GnuCash is a personal finance manager. A check-book like register GUI
allows you to enter and track bank accounts, stocks, income and even
currency trades. The interface is designed to be simple and easy to
use, but is backed with double-entry accounting principles to ensure
balanced books.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%global optflags %{optflags} -Wno-parentheses -Wno-error
sed -i s/3.8/%{python3_version}/g CMakeLists.txt
%cmake -D WITH_PYTHON=ON -D COMPILE_GSCHEMAS=OFF
%cmake_build
%install
%cmake_install
%find_lang %{name}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/
mv $RPM_BUILD_ROOT/%{_libdir}/lib* $RPM_BUILD_ROOT/%{_libdir}/gnucash
rm -rf $RPM_BUILD_ROOT/%{_infodir} \
	$RPM_BUILD_ROOT/%{_includedir} \
	$RPM_BUILD_ROOT/%{_datadir}/aclocal \
	$RPM_BUILD_ROOT/%{_libdir}/lib*.a \
	$RPM_BUILD_ROOT/%{_libdir}/gnucash/lib*.a \
	$RPM_BUILD_ROOT/%{_bindir}/gnc-test-env \
	$RPM_BUILD_ROOT/%{_bindir}/gnc-fq-update \
	$RPM_BUILD_ROOT/%{_datadir}/guile/site/%{guilever}/tests
find $RPM_BUILD_ROOT/%{_libdir} -name *.la -delete
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gnucash.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/gnucash.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
