%global source0_hash 0a3f07fee5fa073aa4cb0e672b27273b252ae93382f84fcb3443dffa8d8050a0

Name:           numberstation
Version:        1.4.0
Release:        4%{?dist}
Summary:        TOTP Authenticator application
License:        GPL-3.0-or-later
URL:            https://sr.ht/~martijnbraam/%{name}/
Source0:        https://git.sr.ht/~martijnbraam/%{name}/archive/%{version}.tar.gz
Requires:       libhandy
Requires:       python3-gobject
Requires:       python3-keyring
Requires:       python3-pyotp
Requires:       hicolor-icon-theme
BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  git
BuildRequires:  libhandy-devel
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.postmarketos.Numberstation.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.postmarketos.Numberstation.appdata.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_metainfodir}/org.postmarketos.Numberstation.appdata.xml
%{_datadir}/applications/org.postmarketos.Numberstation.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.postmarketos.Numberstation.svg
%{_datadir}/%{name}

%changelog
%autochangelog
