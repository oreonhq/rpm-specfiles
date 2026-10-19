%global source0_hash e08c34dbac44794bd851f5336991cf932c7aff4827f2bb977268dfbbd7c143dc
Name:    kremotecontrol 
Summary:        KDE frontend for your remote controls
Version: 17.08.3
Release:        21%{?dist}
License: GPL-2.0-or-later
URL:     http://utils.kde.org/projects/%{name}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch50: kremotecontrol-4.7.90-namelink_skip.patch
Conflicts: kdeutils-common < 6:4.7.80
Obsoletes: kdeutils-kremotecontrol < 6:4.7.80
Provides:  kdeutils-kremotecontrol = 6:%{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%{?kde_runtime_requires}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  kdelibs4-devel
BuildRequires:  make
BuildRequires:  pkgconfig(QtXmlPatterns)
# /oreon:deps
%description
KRemoteControl (formerly known as KDELirc) is a KDE frontend for your
remote controls. It allows to configure actions for button presses on
remotes. All types of remotes supported by the Solid module in the KDE
platform are also supported by KRemoteControl (e.g. with the Linux
Infrared Remote Control system (LIRC) as backend).

%package libs
Summary: Runtime libraries for %{name} 
Requires: %{name} = %{version}-%{release}
Obsoletes: kdeutils-kremotecontrol-libs < 6:4.7.80
Provides:  kdeutils-kremotecontrol-libs = 6:%{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd
make %{?_smp_mflags} -C %{_target_platform}
%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/kde4/krcdnotifieritem.desktop
%files -f %{oreon_filedir}/main.list
%files -n kremotecontrol-libs -f %{oreon_filedir}/kremotecontrol-libs.list

%changelog

%autochangelog
