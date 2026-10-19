%global source1_hash d0a03cc099de813d2092aacf3fc144be33dfa1e3d972cd03a5987890db96fe25
%global source0_hash 452e5ab04f5e2d7cbf9357e4e12badf8493aefda437ba130eb38c9e511313b72
%global stable_kf6 stable
Name:           ocean-sound-theme
Summary:        Ocean Sound Theme for Plasma
Version:        6.7.5
Release:        1%{?dist}
BuildArch:      noarch
License:        CC0-1.0 AND BSD-2-Clause AND CC-BY-SA-4.0
URL:            https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6CoreTools)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{cmake_kf6}
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
