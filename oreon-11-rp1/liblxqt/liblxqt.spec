%global source0_hash c59987b2c4388bf41226847261c168a6cb34637f881ed66a425440fea0769091

%define rpm_macros_dir %{_sysconfdir}/rpm
%if 0%{?fedora}
%define rpm_macros_dir %{_rpmconfigdir}/macros.d
%endif

Name:		liblxqt
Version:	2.3.0
Release:	2%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2
Summary:	Core shared library for LXQt desktop suite
Url:		https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	macros.lxqt

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libXScrnSaver-devel
BuildRequires: lxqt-build-tools
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(qt6xdg)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(PolkitQt6-1)
%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%endif
Requires: xdg-utils >= 1.1.0

%description
Core utility library for all LXQT components

%package devel
Summary:	Devel files for liblxqt
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:       lxqt-build-tools >= 0.13.0
%if 0%{?fedora}
Requires: cmake >= 3.3
%else
Requires: cmake3 >= 3.3
%endif

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

%autosetup -p1

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

# RPM macros
install -p -m0644 -D %{SOURCE1} %{buildroot}%{rpm_macros_dir}/macros.lxqt
sed -i -e "s|@@CMAKE_VERSION@@|%{version}|" %{buildroot}%{rpm_macros_dir}/macros.lxqt
touch -r %{SOURCE1} %{buildroot}%{rpm_macros_dir}/macros.lxqt
%find_lang %{name} --with-qt

%files
%doc AUTHORS COPYING
%{_libdir}/liblxqt.so.2
%{_libdir}/liblxqt.so.%{version}
%{_bindir}/lxqt-backlight_backend
%{_datadir}/lxqt/power.conf
%{_datadir}/polkit-1/actions/org.lxqt.backlight.pkexec.policy

%files devel
%{_libdir}/liblxqt.so
%{_includedir}/lxqt/
%{_datadir}/cmake/lxqt/
%{_libdir}/pkgconfig/lxqt.pc
%{rpm_macros_dir}/macros.lxqt

%files l10n -f %{name}.lang
%license COPYING
%doc AUTHORS README.md
%dir %{_datadir}/lxqt/translations/%{name}

%changelog
%autochangelog
