%global source0_hash 190b50e97d2bb2cfa2ea20137a91aa5b113351f53f8c05fbb152ab97f31b57f7

Name:           rmtfs
Version:        1.1.1
Release:        %autorelease
Summary:        Qualcomm Remote Filesystem Service Implementation

License:        BSD-3-Clause
URL:            https://github.com/linux-msm/rmtfs/
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  qrtr-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros

Requires: qrtr

%description
Qualcomm Remote Filesystem Service Implementation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%make_build prefix="%{_prefix}"

%install
%make_install prefix="%{_prefix}"

%post
%systemd_post rmtfs.service rmtfs-dir.service

%preun
%systemd_preun rmtfs.service rmtfs-dir.service

%postun
%systemd_postun rmtfs.service rmtfs-dir.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/rmtfs.service
%{_unitdir}/rmtfs-dir.service

%changelog
%autochangelog
