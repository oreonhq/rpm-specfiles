%global source0_hash 8c93f717e222c63bbfbcff388c08d387604a778e361e5ddb8ae0da4e1ef308ac
%define rpm_macros_dir %{_sysconfdir}/rpm
Name:		liblxqt
Version:	2.4.0
Release:        1%{?dist}
License:	LicenseRef-Callaway-LGPLv2
Summary:        Core shared library for LXQt desktop suite
Url:		https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	macros.lxqt
%if 0%{?el7}
%endif
Requires: xdg-utils >= 1.1.0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(qt6xdg)
BuildRequires:  gcc-c++
BuildRequires:  libXScrnSaver-devel
BuildRequires:  lxqt-build-tools
BuildRequires:  pkgconfig(glib-2.0)
# /oreon:deps
%description
Core utility library for all LXQT components

%package devel
Summary:	Devel files for liblxqt
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:       lxqt-build-tools >= 0.13.0
Requires: cmake3 >= 3.3
%description devel
LXQt libraries for development.

%package l10n
BuildArch:      noarch
Summary:        Translations for liblxqt
Requires:       liblxqt
Obsoletes:      lxqt-l10n < 0.14.0
%description l10n
This package provides translations for the liblxqt package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif
%cmake
%cmake_build
%if 0%{?el7}
EOF
%endif
%install
%cmake_install
install -p -m0644 -D %{SOURCE1} %{buildroot}%{rpm_macros_dir}/macros.lxqt
sed -i -e "s|@@CMAKE_VERSION@@|%{version}|" %{buildroot}%{rpm_macros_dir}/macros.lxqt
touch -r %{SOURCE1} %{buildroot}%{rpm_macros_dir}/macros.lxqt
%find_lang %{name} --with-qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n liblxqt-devel -f %{oreon_filedir}/liblxqt-devel.list
%files -n liblxqt-l10n -f %{oreon_filedir}/liblxqt-l10n.list

%changelog

%autochangelog
