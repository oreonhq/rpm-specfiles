%global source0_hash 2078766e2553eea0ff2ee598212d4883a226df63d014d060756c6274db024823

Name:           python-xapp
Version:        3.0.2
Release:        2%{?dist}
Summary:        Python bindings for xapps

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://github.com/linuxmint/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python3-xapp
Summary:       %{summary}

BuildRequires: meson
BuildRequires: python3-rpm-macros

Requires:      gtk3
Requires:      python3-gobject-base
Requires:      python3-psutil
Requires:      xapps

%description -n python3-xapp
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n python3-xapp-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files -n python3-xapp
%license COPYING debian/copyright
%doc PKG-INFO debian/changelog
%{python3_sitelib}/xapp/

%changelog
%autochangelog
