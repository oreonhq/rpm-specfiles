%global source0_hash ece3eabdf1c5df18bd91f8f210131444de8360b8c9a7f3926f76a6b5f14fc376

%global repo dde-account-faces

Name:           deepin-account-faces
Version:        1.0.16
Release:        %autorelease
Summary:        Account faces for Linux Deepin
# migrated to SPDX
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-account-faces
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make

Requires:       accountsservice

%description
Account faces for Linux Deepin

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo}-%{version}

%build

%install
%make_install

%files
%{_sharedstatedir}/AccountsService/icons/*

%changelog
%autochangelog
