%global source0_hash a3850c34e48f23b7bc360d70f1e91700de2f8c60af003eda93e14182f8cf6af1
Name:           tqftpserv
Version:        1.2
Release:        1%{?dist}
Summary:        Trivial File Transfer Protocol server over AF_QIPCRTR
License:        BSD-3-Clause
URL:            https://github.com/linux-msm/tqftpserv
Source0:        https://github.com/linux-msm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(qrtr)
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
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
