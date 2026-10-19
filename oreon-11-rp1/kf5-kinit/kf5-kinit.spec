%global source0_hash e4a4acc661035d22f7636397d23307c2e4e4129a7ed82d458fdf2f7ee63dbc2c
%undefine __cmake_in_source_build
%global framework kinit
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
Name:           kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 tier 3 solution for process launching
License:        BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
Source10:       macros.kf5-kinit
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
kdeinit is a process launcher somewhat similar to the famous init used for
booting UNIX.

It launches processes by forking and then loading a dynamic library which should
contain a 'kdemain(...)' function.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build

%{cmake_kf5}
%cmake_build
%install
%cmake_install
%find_lang kinit5_qt --with-man --with-qt --all-name
install -p -m644 -D %{SOURCE10} \
  %{buildroot}%{rpm_macros_dir}/macros.%{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kinit-devel -f %{oreon_filedir}/kf5-kinit-devel.list

%changelog

%autochangelog
