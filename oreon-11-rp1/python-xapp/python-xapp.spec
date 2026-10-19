%global source0_hash 30cf81249a7c5cabc25e465e369928724e091e95c5095704518f14ca6fd11f41
Name:           python-xapp
Version:        3.0.3
Release:        1%{?dist}
Summary:        Python bindings for xapps
License:        LicenseRef-Callaway-LGPLv2
URL:            https://github.com/linuxmint/%{name}
Source0:        https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  meson
BuildRequires:  python3-rpm-macros
# /oreon:deps
%description
%{summary}.

%package -n python3-xapp
Summary:        Python bindings for xapps
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
%global oreon_srcdir python3-xapp-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles python3-xapp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-xapp -f %{oreon_filedir}/python3-xapp.list

%changelog

%autochangelog
