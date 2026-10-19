%global source0_hash 4b6c398806a1046e2256a685d592833de0f37b7245b8adc4797e1791f0e117ee
Name:           rmtfs
Version:        1.3
Release:        1%{?dist}
Summary:        Qualcomm Remote Filesystem Service Implementation
License:        BSD-3-Clause
URL:            https://github.com/linux-msm/rmtfs/
Source0:        https://github.com/linux-msm/%{name}//archive/v%{version}/%{name}-%{version}.tar.gz
Requires: qrtr
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  qrtr-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Qualcomm Remote Filesystem Service Implementation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build prefix="%{_prefix}"
%install
%make_install prefix="%{_prefix}"
%oreon_autofiles main

%post

%systemd_post rmtfs.service rmtfs-dir.service
%preun

%systemd_preun rmtfs.service rmtfs-dir.service
%postun

%systemd_postun rmtfs.service rmtfs-dir.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
