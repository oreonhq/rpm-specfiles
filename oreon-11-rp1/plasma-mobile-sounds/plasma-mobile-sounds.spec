%global debug_package %{nil}

Name:           plasma-mobile-sounds
Version:        0.1
Release:	13%{?dist}
# Automatically converted from old format: CC-BY-SA and CC0 and CC-BY - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA AND CC0-1.0 AND LicenseRef-Callaway-CC-BY
Summary:        Plasma Mobile Sound Theme
Url:            https://invent.kde.org/plasma-mobile/plasma-mobile-sounds
Source:         https://download.kde.org/stable/plasma-mobile-sounds/0.1/plasma-mobile-sounds-0.1.tar.xz

# Use cmake datadir
# https://invent.kde.org/plasma-mobile/plasma-mobile-sounds/-/merge_requests/2
Patch1:         0001-Use-cmake-datadir.patch

BuildArch: noarch

BuildRequires: cmake
BuildRequires: kf6-rpm-macros

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%files
%{_datadir}/sounds/plasma-mobile

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1-12
- Prepare for Oreon 11 (RP1)
