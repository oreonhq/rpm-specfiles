%global source0_hash 4c962c5377c136dd551b822f96c997e0d93b02237381f5f695e7a974824271dd
%global stable_kf6 stable
Name:    kde-dev-scripts
Summary:        KDE SDK scripts
Version: 26.08.0
Release:        1%{?dist}
License: GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-only AND BSD-2-Clause
URL:     https://invent.kde.org/sdk/%{name}.git
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildArch:      noarch
Conflicts:      kdesdk-common < 4.10.80
Provides:       kdesdk-scripts = %{version}-%{release}
Obsoletes:      kdesdk-scripts < 4.10.80
Conflicts: kde-l10n < 17.08.3-2
# oreon:deps
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  extra-cmake-modules
BuildRequires:  perl-generators
BuildRequires:  python3-devel
# /oreon:deps
%description
KDE SDK scripts

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html --with-man
%py3_shebang_fix %{buildroot}%{_kf6_bindir}/*
rm -fv %{buildroot}%{_kf6_bindir}/krazy-licensecheck
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 26.08.0-1
- Latest upstream release

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
