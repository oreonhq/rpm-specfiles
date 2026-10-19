%global source0_hash 33e4944303c778581b6471c79e1273a5668917542e412c8125f028133b684718
Name:           zcfan
Version:        1.4.0
Release:        1%{?dist}
Summary:        Zero-configuration fan daemon for ThinkPads
License:        MIT
URL:            https://github.com/cdown/zcfan
Source0:        https://github.com/cdown/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
zcfan is a zero-configuration fan control daemon for ThinkPads.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%make_build prefix=%{_prefix}
%install
%make_install DESTDIR=%{buildroot} prefix=%{_prefix}
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
