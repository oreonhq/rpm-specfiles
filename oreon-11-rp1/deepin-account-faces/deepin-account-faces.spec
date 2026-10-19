%global source0_hash 73fb4a25473ecf0f6c6d3536cb55e1d7297937744767294dd5cf9a519bc87e17
%global repo dde-account-faces
Name:           deepin-account-faces
Version:        1.0.19
Release:        1%{?dist}
Summary:        Account faces for Linux Deepin
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-account-faces
Source0:        https://github.com/linuxdeepin/%{repo}/archive/%{version}/%{repo}-%{version}.tar.gz
BuildArch:      noarch
Requires:       accountsservice
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
Account faces for Linux Deepin

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo}-%{version}

%build

%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
