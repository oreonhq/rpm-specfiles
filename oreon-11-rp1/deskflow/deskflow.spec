%global source0_hash 3ed16983bb8a037ebe90b0dd642e7af44e17b258d601995a54fd0324b949f9eb
%bcond x11 %[%{undefined rhel} || 0%{?rhel} < 10]
%global rdnn_name org.deskflow.deskflow
%global qt6ver 6.7.0
Name:		deskflow
Version:	1.26.0
Release:        1%{?dist}
Summary:        Share mouse and keyboard between multiple computers over the network
License:	GPL-2.0-only
URL:		https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:	%{ix86}
%if %{with x11}
%endif
Requires:	hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libei-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
# /oreon:deps
%description
Deskflow is software that mimics the functionality of a KVM switch, which
historically would allow you to use a single keyboard and mouse to control
multiple computers by physically turning a dial on the box to switch the
machine you're controlling at any given moment.

Deskflow does this in software, allowing you to tell it which machine to
control by moving your mouse to the edge of the screen, or by using a
key press to switch focus to a different system.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
%cmake -DSKIP_BUILD_TESTS=1 %{!?with_x11:-DBUILD_X11_SUPPORT=OFF}

%build

%cmake_build
%install
%cmake_install
echo -e "#!/bin/sh\n%{_bindir}/%{name}-core server \$@" > %{buildroot}/%{_bindir}/%{name}-server
echo -e "#!/bin/sh\n%{_bindir}/%{name}-core client \$@" > %{buildroot}/%{_bindir}/%{name}-client
chmod 755 %{buildroot}/%{_bindir}/%{name}-server  %{buildroot}/%{_bindir}/%{name}-client
cp %{buildroot}%{_datadir}/licenses/deskflow/LICENSE_EXCEPTION .
rm -fr %{buildroot}%{_docdir}/%{name}/html
%oreon_autofiles main

%check

export QT_QPA_PLATFORM=minimal
%ifarch s390x
%{__ctest} --test-dir  "%{_vpath_builddir}/src/unittests" --output-on-failure --force-new-ctest-process %{?_smp_mflags} || :
%{_vpath_builddir}/bin/legacytests || :
%else
%{__ctest} --test-dir  "%{_vpath_builddir}/src/unittests" --output-on-failure --force-new-ctest-process %{?_smp_mflags}
%{_vpath_builddir}/bin/legacytests
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn_name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
