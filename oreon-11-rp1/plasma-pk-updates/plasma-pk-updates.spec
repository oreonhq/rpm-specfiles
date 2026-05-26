%undefine __cmake_in_source_build

Name:           plasma-pk-updates
Epoch:          1
Version:        0.3.2
Release:        23%{?dist}
Summary:        Plasma applet for system updates using PackageKit

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/system/plasma-pk-updates
Source0:        https://download.kde.org/stable/plasma-pk-updates/%{version}/plasma-pk-updates-%{version}.tar.xz

# Upstream patches
Patch5: 0005-Several-fixes-related-to-the-network-state-and-apple.patch
Patch6: 0006-Don-t-force-a-check-for-updates-when-the-applet-runs.patch
Patch8: 0008-Replace-KIconLoader-pixmaps-with-standard-icon-names.patch
Patch9: 0009-Fix-usage-of-0-for-null-pointer-constants.patch
Patch10: 0010-Use-own-eventIds-and-ComponentName-instead-of-generi.patch
Patch11: 0011-Make-the-notifications-less-obtrusive.patch
Patch12: 0012-Fix-minor-typos.patch
Patch13: 0013-Fix-warning-remove-unsigned-int-0-check.patch
Patch14: 0014-Remove-explicit-initialization-of-default-constructe.patch
## Requires new SIP Power API from solid, not enabled by default
Patch15: 0015-Port-away-from-KDELibs4Support-use-Solid-Power-inter.patch
Patch30: 0030-Add-support-for-license-prompts.patch
Patch35: 0035-Make-action-buttons-translatable.patch
Patch42: 0042-Don-t-show-an-error-for-a-failed-automatic-refresh.patch

# Downstream patches
Patch100: plasma-pk-updates-0.3.2-notif.patch
# oreon url source checksums begin
%global source0_sha256 2ffdbd645ceec85ceb8002f4fbb73e46145612a9ceb831a770e6295f426d2f6c
%global source0_file plasma-pk-updates-0.3.2.tar.xz
# oreon url source checksums end

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-plasma-devel
# 5.75.0-2 when WIP api's used here were enabled -- rdieter
BuildRequires:  kf5-solid-devel >= 5.75.0-2
BuildRequires:  kf5-rpm-macros
BuildRequires:  PackageKit-Qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

BuildRequires:  libappstream-glib

Requires:       PackageKit
Requires:       kf5-solid%{?_isa} >= 5.75.0-2

%description
%{summary}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/plasma-pk-updates-0.3.2.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "2ffdbd645ceec85ceb8002f4fbb73e46145612a9ceb831a770e6295f426d2f6c" || { echo "oreon: Source0 SHA256 mismatch for plasma-pk-updates-0.3.2.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1


%build
# CMake 4 rejects cmake_minimum_required older than 3.5 unless policy is set for the whole run
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_kf5 -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.plasma.pkupdates.appdata.xml ||:


%files -f %{name}.lang
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.plasma.pkupdates.desktop
%{_kf5_qmldir}/org/kde/plasma/PackageKit/
%{_kf5_datadir}/plasma/plasmoids/org.kde.plasma.pkupdates/
%{_kf5_metainfodir}/org.kde.plasma.pkupdates.appdata.xml
%{_kf5_datadir}/knotifications5/plasma_pk_updates.notifyrc


%changelog
* Tue Apr 07 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.2-23
- Export CMAKE_POLICY_VERSION_MINIMUM for CMake 4 configure

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.2-22
- Prepare for Oreon 11 (RP1)
