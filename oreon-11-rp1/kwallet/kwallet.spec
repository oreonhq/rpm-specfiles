%global source0_hash 2693359ce34ffe7d72c60f2e3db4185c18a8c0672e5c18cfb0196cc87a430541

Name:    kwallet
Summary: Manage KDE passwords 
Version: 4.12.3
Release: 29%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://projects.kde.org/projects/kde/kdeutils/kwallet 
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/kwalletmanager-%{version}.tar.xz

## upstream patches

BuildRequires: desktop-file-utils
BuildRequires: kdelibs4-devel >= %{version}
BuildRequires: pkgconfig(polkit-qt-1)
BuildRequires: make

# when split occured
Conflicts: kdeutils-common < 6:4.7.80

Obsoletes: kdeutils-kwalletmanager < 6:4.7.80
Provides:  kdeutils-kwalletmanager = 6:%{version}-%{release}

Provides:  kwalletmanager = %{version}-%{release}

Requires: kde-runtime%{?_kde4_version: >= %{_kde4_version}}

%description
KDE Wallet Manager is a tool to manage the passwords on your KDE system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n kwalletmanager-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang kwallet --with-kde --without-mo

%files -f kwallet.lang
%doc COPYING
%{_kde4_bindir}/kwalletmanager
%{_kde4_appsdir}/kwalletmanager/
%{_kde4_iconsdir}/hicolor/*/apps/kwalletmanager*.*
%{_kde4_datadir}/kde4/services/kwallet*.desktop
%{_kde4_datadir}/applications/kde4/kwalletmanager*.desktop
%{_kde4_libdir}/kde4/kcm_kwallet.so
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmkwallet.conf
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkwallet.service
%{_kde4_libexecdir}/kcm_kwallet_helper
%{_polkit_qt_policydir}/org.kde.kcontrol.kcmkwallet.policy

%changelog
%autochangelog
