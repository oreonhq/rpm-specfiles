%global source0_hash 6cd96efca241a4b60fb6bf449c64dbad713b223c36e003ae89f45e34739d56d1
%bcond qt5 %[%{undefined rhel} || 0%{?rhel} < 10]
Name:           qadwaitadecorations
Version:        0.1.7
Release:        3%{?dist}
Summary:        Qt decoration plugin implementing Adwaita-like client-side decorations
License:        LGPL-2.1-or-later
URL:            https://github.com/FedoraQt/QAdwaitaDecorations
Source0:        https://github.com/FedoraQt/QAdwaitaDecorations/archive/%{version}/QAdwaitaDecorations-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtwayland-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-static
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  wayland-devel
# /oreon:deps
%description
%{summary}.

%if %{with qt5}
%package qt5
Summary:        Qt decoration plugin implementing Adwaita-like client-side decorations
BuildRequires:  qt5-qtbase-devel >= 5.15.2
BuildRequires:  qt5-qtbase-static >= 5.15.2
BuildRequires:  qt5-qtwayland-devel >= 5.15.2
BuildRequires:  qt5-qtbase-private-devel >= 5.15.2
BuildRequires:  qt5-qtsvg-devel >= 5.15.2
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Supplements:   (qt5-qtbase and gnome-shell)
%description qt5
%{summary}.
%endif

%if %{with qt6}
%package qt6
Summary:        Qt decoration plugin implementing Adwaita-like client-side decorations
BuildRequires:  qt6-qtbase-devel >= 6.5.0
BuildRequires:  qt6-qtbase-static >= 6.5.0
BuildRequires:  qt6-qtwayland-devel >= 6.5.0
BuildRequires:  qt6-qtbase-private-devel >= 6.5.0
BuildRequires:  qt6-qtsvg-devel >= 6.5.0
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
Supplements:   (qt6-qtbase and gnome-shell)
%description qt6
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir QAdwaitaDecorations-%{version}
%oreon_prep
%build

%if %{with qt5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake -DHAS_QT6_SUPPORT=true
%cmake_build
%endif
%if %{with qt6}
%global _vpath_builddir %{_target_platform}-qt6
%cmake -DUSE_QT6=true
%cmake_build
%endif
%install
%if %{with qt5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
%endif
%if %{with qt6}
%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%if %{with qt5}
%files -f %{oreon_filedir}/main.list
%files -n qadwaitadecorations-qt5 -f %{oreon_filedir}/qadwaitadecorations-qt5.list
%files -n qadwaitadecorations-qt6 -f %{oreon_filedir}/qadwaitadecorations-qt6.list

%changelog

%autochangelog
%endif
