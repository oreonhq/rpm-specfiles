%global source0_hash 746359dbaf6aec5650cc8c1868b38b03c5764a353524d3fbee4d2cc67dd71e65
%global have_pygobject3_devel 1
%global have_xtest_devel  1
%global sub_version             1.1
%global libxklavier_version     4.0
%global libxml2_version         2.0
%global libinput_paddir %{_libdir}/%{name}-%sub_version
%global moduledir       %{_libdir}/%{name}-%sub_version/modules
%global kbduidir        %{_libdir}/%{name}-%sub_version/modules/kbdui
%global xkeysenddir     %{_libdir}/%{name}-%sub_version/modules/xkeysend
Name:       input-pad
Version:    1.1.0
Release:        1%{?dist}
Summary:        On-screen Input Pad to Send Characters with Mouse
License:    LGPL-2.1-or-later
URL:        https://github.com/fujiwarat/input-pad/wiki
Source0:        https://github.com/fujiwarat/input-pad/releases/download/%{version}/%{name}-%{version}.tar.gz
%if %have_xtest_devel
%endif
%if %have_pygobject3_devel
%endif
%if %have_pygobject3_devel
Requires:       gobject-introspection
Requires:       python3-gobject
%endif
Provides:       %{name}-xtest = %{version}-%{release}
Obsoletes:      %{name}-xtest < %{version}-%{release}
# oreon:deps
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  libXtst-devel
BuildRequires:  libtool
BuildRequires:  libxkbfile-devel
BuildRequires:  libxklavier-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
The input pad is a tool to send a character on button to text applications.

%package devel
Summary:    Development tools for input-pad
Requires:   %{name} = %{version}-%{release}
%description devel
The input-pad-devel package contains the header files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%autosetup -S git

%build

%configure \
%if %have_xtest_devel
    --enable-xtest              \
%endif
    --disable-static
%make_build
%install
%make_install
if [ ! -d $RPM_BUILD_ROOT%kbduidir ] ; then
    mkdir -p $RPM_BUILD_ROOT%kbduidir
fi
if [ ! -d $RPM_BUILD_ROOT%xkeysenddir ] ; then
    mkdir -p $RPM_BUILD_ROOT%xkeysenddir
fi
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
%if %have_xtest_devel
rm -f $RPM_BUILD_ROOT%xkeysenddir/*.la
rm -f $RPM_BUILD_ROOT%xkeysenddir/*.a
%endif
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n input-pad-devel -f %{oreon_filedir}/input-pad-devel.list

%changelog

%autochangelog
