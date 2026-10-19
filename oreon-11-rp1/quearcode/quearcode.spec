%global source0_hash 8fbcf2d1b719e1f1ecf4d8acd57854464020ad9c749eedab23fd0f4e68ab8c2f
Name:           quearcode
Version:        0.4.2
Release:        1%{?dist}
Summary:        A tool for creating QR Codes
License:        GPL-3.0-or-later
URL:            https://codeberg.org/gwync/quearcode
Source0:        https://codeberg.org/gwync/quearcode/archive/%{version}.tar.gz
Source1:        org.esrum.Quearcode.desktop
BuildArch:      noarch
Requires:       python3-qrcode python3-gobject hicolor-icon-theme
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-quearcode = %{version}-%{release}
# /oreon:deps
%description
Convert strings and small files to QR Codes

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}

%build

./t_build.sh
%pyproject_wheel
%install
%pyproject_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -m 644 quearcode.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 pyquearcode/logo.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/quearcode.png
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
%oreon_autofiles main

%check

%pyproject_check_import
%files

%changelog

%autochangelog
