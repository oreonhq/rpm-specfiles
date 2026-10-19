%global source0_hash d92ea96b63254e7145bd720a62fc56b2932c82c24534073ae5d9f20fc13bf511
Name:      plasma-welcome-fedora
Version:   6.3.4
Release:        1%{?dist}
Summary:        Fedora-related customizations for Plasma-welcome
License:   (GPL-2.0-only OR GPL-3.0-only) AND CC-BY-SA-4.0
URL:       https://pagure.io/fedora-kde/plasma-welcome-fedora
Source0:        %{name}-v%{version}.tar.gz
BuildArch: noarch
Requires:  plasma-welcome
Requires:  fedora-third-party
Requires:  fedora-workstation-repositories
Requires:  fedora-flathub-remote
# oreon:deps
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

make build_all
%install
%make_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
