%global source0_hash 73206d000fe0e33597d33e05572d8e09aae7896d2640d114a0f19f8f1a44582b
Name:           deepin-sound-theme
Version:        15.10.6
Release:        1%{?dist}
Summary:        Deepin sound theme
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-sound-theme
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
Sound files for the Deeping Desktop Environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
