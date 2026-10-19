%global source0_hash 45f9f1df8c600bf8a505f88b69d826ff78c901399419a27ffdb143dd582ed800
Name:           foosnapper
Version:        1.5
Release:        1%{?dist}
Summary:        Automatic filesystem snapshotter
License:        GPL-2.0-or-later
URL:            https://github.com/FoobarOy/foosnapper
Source0:        https://github.com/FoobarOy/foosnapper/archive/v%{version}/foosnapper-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3
%{?systemd_requires}
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Automatic filesystem snapshotter, supporting Stratis and Btrfs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
make install DESTDIR=%{buildroot}
%oreon_autofiles main

%post

%systemd_post foosnapper.service foosnapper.timer
%preun

%systemd_preun foosnapper.service foosnapper.timer
%postun

%systemd_postun foosnapper.service
%systemd_postun_with_restart foosnapper.timer
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
