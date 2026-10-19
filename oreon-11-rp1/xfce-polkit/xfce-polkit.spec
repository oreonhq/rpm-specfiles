%global source0_hash 378b5dce1fea9ebcc6cc6c116e9c4ffe02573c7ffdd0112f4139ec151d5b4ef0
Name:           xfce-polkit
Version:        0.3
Release:        1%{?dist}
Summary:        Simple PolicyKit authentication agent for Xfce
License:        GPL-2.0-or-later
URL:            https://github.com/ncopa/%{name}
Source0:        https://github.com/ncopa/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Provides: PolicyKit-authentication-agent
Requires: polkit >= 0.97
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libxfce4ui-devel
BuildRequires:  make
BuildRequires:  polkit-devel
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
autoreconf -fi

%build

%configure
%make_build
%install
%make_install
desktop-file-edit --remove-key=NotShowIn --add-only-show-in=XFCE \
 %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
