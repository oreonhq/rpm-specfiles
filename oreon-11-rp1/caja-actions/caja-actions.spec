%global source0_hash 310d39488e707fad848959a0a800b6154f4498dfddaeff5af49e4db35d0bea4d
Summary:        Caja extension for customizing the context menu
Name:    caja-actions
Version: 1.28.0
Release:        1%{?dist}
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL: https://github.com/raveit65/%{name}
Source0:        https://github.com/raveit65/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Requires:       %{name}-doc = %{version}-%{release}
# oreon:deps
BuildRequires:  caja-devel
BuildRequires:  dblatex
BuildRequires:  desktop-file-utils
BuildRequires:  libSM-devel
BuildRequires:  libgtop2-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mate-common
BuildRequires:  yelp-tools
# /oreon:deps
%description
Caja actions is an extension for Caja, the MATE file manager.
It provides an easy way to configure programs to be launch on files 
selected in Caja interface

%package doc
Summary: Documentations for %{name}
BuildArch: noarch
%description doc
This package contains the documentation for %{name}

%package devel
Summary: Development tools for the caja-actions
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains headers and shared libraries needed for development
with caja-actions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
    --disable-gtk-doc \
    --enable-html-manuals \
    --enable-pdf-manuals \
    --enable-deprecated
make %{?_smp_mflags} V=1
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/INSTALL
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2008
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2009
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2010
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2011
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2012
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/MAINTAINERS
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/cact.desktop
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n caja-actions-doc -f %{oreon_filedir}/caja-actions-doc.list
%files -n caja-actions-devel -f %{oreon_filedir}/caja-actions-devel.list

%changelog

%autochangelog
