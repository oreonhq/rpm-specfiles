%global source1_hash 464516b19e84f13b4cb70fa67d4d47ea5f52ca0d9cf16508b5e8690660f1b186
%global source0_hash 1701e40bef1c3c45ad221d42307ab66c395b053a567e3445b261ab18a22550b6
Name:           kde-qdoc-common
Version:        1.0.0
Release:        1%{?dist}
Summary:        Common files for KDE's API documentation (using QDoc)
BuildArch:      noarch
License:        GFDL-1.3-no-invariants-only AND BSD-3-Clause AND CC0-1.0
URL:            https://invent.kde.org/sdk/kde-qdoc-common
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
# oreon:deps
BuildRequires:  qt6-rpm-macros
# /oreon:deps
%description
This package contains common files for KDE's API documentation.
Individual projects include it in their documentation builds.
The files in the 'global' folder are forked from Qt.
We can modify them at will, however we should periodically
sync them with upstream to incorporate improvements from there.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{_qt6_docdir}/%{name}
cp -ar global %{buildroot}%{_qt6_docdir}/%{name}/global/
cp classes.qdoc %{buildroot}%{_qt6_docdir}/%{name}/
cp CMakeLists.txt %{buildroot}%{_qt6_docdir}/%{name}/
cp empty.cpp %{buildroot}%{_qt6_docdir}/%{name}/
cp index.qdoc %{buildroot}%{_qt6_docdir}/%{name}/
cp kde.qdocconf %{buildroot}%{_qt6_docdir}/%{name}/
rm -f LICENSES/LicenseRef-Qt-Commercial.txt
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 1.0.0-1
- Latest upstream release

%autochangelog
