%global source0_hash e4a4acc661035d22f7636397d23307c2e4e4129a7ed82d458fdf2f7ee63dbc2c

%undefine __cmake_in_source_build
%global framework kinit
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:           kf5-%{framework}
Version: 5.116.0
Release: 7%{?dist}
Summary:        KDE Frameworks 5 tier 3 solution for process launching

License:        BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/%{framework}

%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/stable/frameworks/5.116/%{framework}-%{version}.tar.xz

Source10:       macros.kf5-kinit

## upstream patches

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kconfig-devel >= %{version}
BuildRequires:  kf5-kcrash-devel >= %{version}
BuildRequires:  kf5-kdbusaddons-devel >= %{version}
BuildRequires:  kf5-kdoctools-devel >= %{version}
BuildRequires:  kf5-ki18n-devel >= %{version}
BuildRequires:  kf5-kio-devel >= %{version}
BuildRequires:  kf5-kservice-devel >= %{version}
BuildRequires:  kf5-kwindowsystem-devel >= %{version}

BuildRequires:  qt5-qtbase-devel

BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)

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

# rpm macros
install -p -m644 -D %{SOURCE10} \
  %{buildroot}%{rpm_macros_dir}/macros.%{name}

%ldconfig_scriptlets

%files -f kinit5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_bindir}/*
%{_kf5_libdir}/libkdeinit5_klauncher.so
%{_kf5_libexecdir}/*
%{_kf5_mandir}/man8/kdeinit5.8*

%files devel
%{_kf5_libdir}/cmake/KF5Init/
%{_kf5_datadir}/dbus-1/interfaces/*.xml
%{rpm_macros_dir}/macros.%{name}

%changelog
%autochangelog
