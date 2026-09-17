%global source0_hash 0c6fd20214da86a9a0443359f7b62d9a2bd4ed802fd680853da4b757a371ac91

%if 0%{?rhel} >= 9
%global _lto_cflags %nil
%endif

Name: gnucash
Summary: Finance management application
Version: 5.14
URL: https://gnucash.org/
Release: 3%{?dist}
License: GPL-2.0-or-later
Source: https://downloads.sourceforge.net/sourceforge/gnucash/gnucash-%{version}.tar.bz2

ExcludeArch: %{ix86}

Patch0: rpath.patch
Patch1: no-implicit.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1563466
ExcludeArch: ppc64 s390x

BuildRequires: gcc >= 8, gcc-c++, cmake >= 3.10
BuildRequires: perl-generators, perl-podlators
BuildRequires: libxml2 >= 2.9.4, libxslt-devel, zlib-devel
BuildRequires: gtk3 >= 3.22.30, glib2 >= 2.56.1
BuildRequires: libofx-devel >= 0.9.12, aqbanking-devel >= 5.7.0, gwenhywfar-gui-gtk3-devel >= 4.20
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: guile30-devel
%global guilever 3.0
%else
BuildRequires: guile-devel
%global guilever 2.0
%endif
BuildRequires: swig >= 3.0.12
BuildRequires: desktop-file-utils, gettext >= 0.9.6
BuildRequires: libdbi-devel >= 0.8.3, libdbi-dbd-mysql, libdbi-dbd-pgsql, libdbi-dbd-sqlite
BuildRequires: libappstream-glib
BuildRequires: libsecret-devel >= 0.18
%if %{defined el8}
BuildRequires: boost-devel >= 1.66.0
%else
BuildRequires: boost-devel >= 1.67.0
%endif
BuildRequires: gtest-devel >= 1.8.0, gmock-devel >= 1.8.0
%if 0%{?rhel} >= 9
BuildRequires: webkit2gtk3-devel
%else
BuildRequires: webkit2gtk4.1-devel
%endif
BuildRequires: python3-devel >= 3.6
BuildRequires: python3-setuptools

Requires: gnucash-docs >= %{version}
Requires: dconf
Requires: perl(Finance::Quote)
Requires: perl(JSON::Parse)
Requires: perl(Getopt::Std)
Requires: gnome-icon-theme
Recommends: libdbi-dbd-sqlite
Suggests: libdbi-dbd-mysql
Suggests: libdbi-dbd-pgsql

%description
GnuCash is a personal finance manager. A check-book like register GUI
allows you to enter and track bank accounts, stocks, income and even
currency trades. The interface is designed to be simple and easy to
use, but is backed with double-entry accounting principles to ensure
balanced books.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# thanks gcc8
%global optflags %{optflags} -Wno-parentheses -Wno-error
sed -i s/3.8/%{python3_version}/g CMakeLists.txt
%cmake -D WITH_PYTHON=ON -D COMPILE_GSCHEMAS=OFF
%cmake_build

%install
%cmake_install

%find_lang %{name}

# vfolder desktop file install stuff
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

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/gnucash.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/gnucash.appdata.xml

%files -f %{name}.lang
%docdir %{_datadir}/doc/gnucash
%doc %{_datadir}/doc/gnucash/*
%license LICENSE
%dir %{_sysconfdir}/gnucash
%{_bindir}/*
%{_libdir}/gnucash/
%{_libdir}/guile/%{guilever}/site-ccache/gnucash/
%{python3_sitearch}/gnucash/
%{_datadir}/glib-2.0/schemas/org.gnucash.GnuCash.*.xml
%{_datadir}/gnucash
%{_datadir}/guile/site/%{guilever}/gnucash
%{_datadir}/metainfo/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man*/*
%config(noreplace) %{_sysconfdir}/gnucash/*

%changelog
%autochangelog
