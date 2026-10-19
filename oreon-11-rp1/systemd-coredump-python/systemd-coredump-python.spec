%global source0_hash e419af86d1abd7e3f3a80b3bd5c65144ac00994d0dab737d8859538464f5a36d
Name:           systemd-coredump-python
Version:        3
Release:        1%{?dist}
Summary:        systemd-coredump helper to log Python exceptions
License:        GPL-2.0-or-later
URL:            https://github.com/systemd/systemd-coredump-python
Source0:        https://github.com/systemd/systemd-coredump-python/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description

%package -n python3-systemd-coredump
Summary:        systemd-coredump helper to log Python exceptions
Conflicts:      systemd < 233
%description -n python3-systemd-coredump

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-systemd-coredump usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-systemd-coredump -f %{oreon_filedir}/python3-systemd-coredump.list

%changelog

%autochangelog
