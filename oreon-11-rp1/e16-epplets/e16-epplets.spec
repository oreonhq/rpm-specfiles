%global source0_hash d444e812d8945f5a90cba3cb8e0f05cc67fb0c8c45e4fb57a72e07f071eecba5

Summary:       Epplets for Enlightenment, DR16
Name:          e16-epplets
Version:       0.18
Release:       1%{?dist}
# Automatically converted from old format: MIT with advertising and GPL+ and GPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-MIT-with-advertising AND GPL-1.0-or-later AND GPL-2.0-or-later
URL:           http://www.enlightenment.org/
Source0:       http://downloads.sourceforge.net/enlightenment/e16-epplets-%{version}.tar.xz
BuildRequires: make
BuildRequires: freeglut-devel
BuildRequires: gcc
BuildRequires: imlib2-devel
BuildRequires: mesa-libGLU-devel
Requires:      e16 >= 0.16.8
%description
Epplets are small, handy Enlightenment applets, similar to dockapps or
applets for other packages.  The epplets package contains the base
epplet API library and header files, as well as the core set of
epplets, including CPU monitors, clocks, a mail checker, mixers, a
slideshow, a URL grabber, a panel-like toolbar, and more.

%package       devel
Summary:       Development tools for epplets
Requires:      %{name} = %{version}-%{release}
%description devel
The %{name}-devel package contains the header files and libs for
developing epplets for Enlightenment, DR16

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{__sed} -i -e 's/-rpath $(libdir)//' epplets/Makefile.in
%configure
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libepplet{,_glx}.{a,la}

%ldconfig_scriptlets

%files
%doc ChangeLog 
%{_libdir}/libepplet.so.*
%{_libdir}/libepplet_glx.so.*
%{_bindir}/E*.epplet
%{_datadir}/e16/epplet_icons
%{_datadir}/e16/epplet_data

%files devel
%{_includedir}/epplet.h
%{_libdir}/libepplet.so
%{_libdir}/libepplet_glx.so

%changelog
%autochangelog
