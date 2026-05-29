%global source0_hash df347ed5ec399e8f30cd3add5ea52bb2c2fcf04b3e6c00da0e43eac839a6282f

%global debug_package %{nil}

Name:           plasma-mobile-sounds
Version: 0.1
Release: 1%{?dist}
# Automatically converted from old format: CC-BY-SA and CC0 and CC-BY - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA AND CC0-1.0 AND LicenseRef-Callaway-CC-BY
Summary:        Plasma Mobile Sound Theme
Url:            https://invent.kde.org/plasma-mobile/plasma-mobile-sounds
Source0:        https://invent.kde.org/plasma-mobile/plasma-mobile-sounds/-/archive/v0.1/plasma-mobile-sounds-v0.1.tar.gz#/plasma-mobile-sounds-0.1.tar.gz

# Use cmake datadir
# https://invent.kde.org/plasma-mobile/plasma-mobile-sounds/-/merge_requests/2
Patch1:         0001-Use-cmake-datadir.patch

BuildArch: noarch

BuildRequires: cmake
BuildRequires: kf6-rpm-macros

%description
%{summary}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n plasma-mobile-sounds-v0.1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%{_datadir}/sounds/plasma-mobile

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Troy Dawson <tdawson@redhat.com> - 0.1-9
- Use cmake datadir

* Wed Sep 4 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 11 2022 Justin Zobel <justin@1707.io> - 0.1-1
- Initial version of package
