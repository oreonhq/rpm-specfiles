%global source0_hash 092b5f04b3e05662c91ab55251b3bd8571cfaa3e347ba1200b0b84bcb32e980f

Name:           wayland-logout
Version:        1.4
Release:        12%{?dist}
Summary:        Simple program that sends SIGTERM to a wayland compositor

License:        MIT
URL:            https://github.com/soreau/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.55

%description
Wayland Logout is an utility designed to kill any wayland compositor
that uses libwayland-server. It looks up the PID for the socket file
by checking the socket path environment variables and sends a SIGTERM
signal. This is useful as a way to logout of a wayland compositor,
as the name implies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
