%global source0_hash bf8c315dbd3b15006227f26ff5484397e98c081388a70e251fc51c8b409f365f

Name:           quearcode
Version:        0.4.2
Release:        3%{?dist}
Summary:        A tool for creating QR Codes

License:        GPL-3.0-or-later
URL:            https://codeberg.org/gwync/quearcode
Source0:        https://codeberg.org/gwync/quearcode/archive/%{version}.tar.gz
Source1:        org.esrum.Quearcode.desktop
BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-qrcode python3-gobject hicolor-icon-theme

%description
Convert strings and small files to QR Codes

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}

%generate_buildrequires
%pyproject_buildrequires

%build
./t_build.sh
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyquearcode
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata

install -m 644 quearcode.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 pyquearcode/logo.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/quearcode.png

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

%check
%pyproject_check_import

%files
%doc COPYING README.md
%{_bindir}/quearcode
%{_datadir}/applications/org.esrum.Quearcode.desktop
%{_datadir}/icons/hicolor/scalable/apps/quearcode.png
%{_datadir}/appdata/quearcode.appdata.xml
%{python3_sitelib}/pyquearcode
%{python3_sitelib}/quearcode-%{version}.dist-info/

%changelog
%autochangelog
