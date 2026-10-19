%global source0_hash b30a48f53294c4f2da91ebcbc3800082b7987943ffdebca45594f2405b0154fe
Name:           numberstation
Version:        1.5.0
Release:        1%{?dist}
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
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  git
BuildRequires:  libappstream-glib
BuildRequires:  libhandy-devel
BuildRequires:  meson
BuildRequires:  python3-devel
# /oreon:deps
%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%meson_test
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.postmarketos.Numberstation.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.postmarketos.Numberstation.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
