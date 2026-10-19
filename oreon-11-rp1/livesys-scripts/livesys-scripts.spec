%global source0_hash a1c60837b5fdb42e05081c903050ad2e0282f5a4a36b566f12d8d3a7fa8c0469
Name:           livesys-scripts
Version:        0.9.7
Release:        1%{?dist}
Summary:        Scripts for auto-configuring live media during boot
License:        GPL-3.0-or-later
URL:            https://pagure.io/livesys-scripts
Source0:        https://tarballs.oreonhq.com/livesys-scripts-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%make_install
mkdir -p %{buildroot}%{_sharedstatedir}/livesys
touch %{buildroot}%{_sharedstatedir}/livesys/livesys-session-extra
touch %{buildroot}%{_sharedstatedir}/livesys/livesys-session-late-extra
%oreon_autofiles main

%preun

%systemd_preun livesys.service livesys-late.service
%post

%systemd_post livesys.service livesys-late.service
%postun

%systemd_postun livesys.service livesys-late.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
