%global source0_hash 34c20801d17bb0e16111556539e90776cc33dbed8a53dc814c82ffabe526acc0
Name:    kwalletmanager
Summary:        Wallet Management Tool for KDE4
Version: 15.04.3
Release:        28%{?dist}
License: GPL-2.0-or-later
URL:     https://quickgit.kde.org/?p=%{name}.git
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch100: kwalletmanager-15.04.3-kde4.patch
Patch101: kwalletmanager-15.04.3-defaults.patch
Conflicts: kdeutils-common < 6:4.7.80
Obsoletes: kdeutils-kwalletmanager < 6:4.7.80
Provides:  kdeutils-kwalletmanager = 6:%{version}-%{release}
Provides: kwalletmanager4 = %{version}-%{release}
Obsoletes: kwallet < 4.12.3-10
Provides:  kwallet = %{version}-%{release}
%{?kde_runtime_requires}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  kdelibs4-devel
BuildRequires:  make
BuildRequires:  pkgconfig(polkit-qt-1)
# /oreon:deps
%description
KDE Wallet Manager is a tool to manage the passwords for KDE4 applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n kwalletmanager-%{version}

%patch -P100 -p1 -b .kde4
%patch -P101 -p1 -b .defaults

%build

mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd
make %{?_smp_mflags} -C %{_target_platform}
%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
