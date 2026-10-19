%global source0_hash 84fa627c7eec92df62ecae129fe30fc7d16e297f20a3d126b8c53d04a6c35c60
Name:           zps
Version:        2.0.0
Release:        1%{?dist}
Summary:        A small utility for listing and cleaning up zombie processes
License:        GPL-3.0-only
URL:            https://github.com/orhun/zps
Source0:        https://github.com/orhun/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
# /oreon:deps
%description
zps lists the running processes with theirs stats and indicates/reaps the 
zombie processes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
install -Dpm 0644 man/%{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications .application/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
