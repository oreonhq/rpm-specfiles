%global source0_hash 9f667106fd5b3400ec5e500ac0e687be76d3a7bd208698103f73793c5e18d1e5
Name: kover
Summary:        WYSIWYG CD cover printer with CDDB support
Version: 7
Release:        1%{?dist}
License: GPL-2.0-or-later
Source0:        https://github.com/adrianreber/kover/releases/download/v%{version}/kover-%{version}.tar.bz2
URL: https://github.com/adrianreber/kover
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kxmlgui-devel
BuildRequires:  libcddb-devel
BuildRequires:  libcdio-devel
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
Kover is an easy to use WYSIWYG CD cover printer with CDDB support.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake
%cmake_build
%install
%cmake_install
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --add-category Utility \
  --add-category AudioVideo \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
%{__install} -p -D %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png \
	%{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-%{name}.png
%find_lang %{name} --with-kde
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
