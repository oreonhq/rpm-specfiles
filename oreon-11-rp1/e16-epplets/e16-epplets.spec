%global source0_hash d444e812d8945f5a90cba3cb8e0f05cc67fb0c8c45e4fb57a72e07f071eecba5
Summary:        Epplets for Enlightenment, DR16
Name:          e16-epplets
Version:       0.18
Release:        1%{?dist}
License:       LicenseRef-Callaway-MIT-with-advertising AND GPL-1.0-or-later AND GPL-2.0-or-later
URL:           http://www.enlightenment.org/
Source0:        http://downloads.sourceforge.net/enlightenment/e16-epplets-%{version}.tar.xz
Requires:      e16 >= 0.16.8
# oreon:deps
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  imlib2-devel
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
# /oreon:deps
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
%oreon_prep
%build

%{__sed} -i -e 's/-rpath $(libdir)//' epplets/Makefile.in
%configure
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/libepplet{,_glx}.{a,la}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n e16-epplets-devel -f %{oreon_filedir}/e16-epplets-devel.list

%changelog

%autochangelog
