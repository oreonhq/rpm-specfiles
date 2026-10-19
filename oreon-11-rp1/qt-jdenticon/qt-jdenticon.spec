%global source0_hash 39fca8c8a6a95fd76419ace3ec5f0b7876044abc78b979c2632ab73b2da50b58
%global __provides_exclude_from ^%{_qt6_plugindir}/.*\\.so$
Name: qt-jdenticon
Version: 0.3.1
Release:        1%{?dist}
License: MIT
Summary:        Jdenticon Qt5 plugin
URL: https://github.com/Nheko-Reborn/%{name}
Source0:        https://github.com/Nheko-Reborn/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
Special Qt/C++14 port of Jdenticon distributed as a Qt plugin.

The eventual plan for this is that it will be made into a Qt library that can
be used in other applications with a command-line application for use as a
standalone generator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%qmake_qt6 QtIdenticon.pro
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
%if 0%{?flatpak}
mv %{buildroot}/usr %{buildroot}/app
%oreon_autofiles main
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
