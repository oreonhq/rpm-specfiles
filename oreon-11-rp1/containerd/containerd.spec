%global source0_hash c213c8222ec2b51f88eb541cd75e5905b35ae7d0b82d6d812f0b8121d11131a6
%bcond check 0
%global goipath         github.com/containerd/containerd
Version:                2.4.1
%global tag             v%{gsub %{version} ~ -}
%gometa -L -f
%global common_description %{expand:
Containerd is an industry-standard container runtime with an emphasis on
simplicity, robustness and portability. It is available as a daemon for Linux
and Windows, which can manage the complete container lifecycle of its host
system: image transfer and storage, container execution and supervision,
low-level storage and network attachments, etc.}
Name:           containerd
Release:        1%{?dist}
Summary:        An open and reliable container runtime
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Source3:        containerd.toml
Patch:          0001-Makefile-adjust-GO_LDFLAGS-quoting.patch
Requires:       runc
# oreon:deps
BuildRequires:  /usr/bin/go-md2man
BuildRequires:  btrfs-progs-devel
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  make
BuildRequires:  procps-ng
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1
# Replace default bin directory
sed -i "s|/usr/local/bin/containerd|/usr/bin/containerd|" containerd.service
cp -p %{S:3} .

%build

GO_LDFLAGS="" GO_BUILDFLAGS=""
%global makeflags %{expand:\\
    DATADIR=%{_datadir} \\
    DESTDIR=%{buildroot} \\
    EXTRA_LDFLAGS=%{gobuild_ldflags_shescaped} \\
    GO_BUILD_FLAGS=%{gobuild_baseflags_shescaped} \\
    MANDIR=%{_mandir} \\
    PREFIX=%{_prefix} \\
    REVISION=%{release} \\
    SHIM_CGO_ENABLED=1 \\
    VERSION=%{gsub %{version} ~ -} \\
}
%make_build %{makeflags} binaries man
%install
%go_vendor_license_install -c %{S:2}
%make_build %{makeflags} install install-man
install -Dpm 0644 containerd.service -t %{buildroot}%{_unitdir}
install -Dpm 0644 containerd.toml %{buildroot}%{_sysconfdir}/containerd/config.toml
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%global test_ignores %{shrink:
    %dnl tests below fail with create tmp file: open ... invalid argument
    -s "TestWriterTruncateRecoversFromIncompleteWrite"
    -s "TestWriteReadEmptyFileTimestamp"
    -s "TestWalkBlobs"
    -s "TestContentWriter"
    -s "TestContent"
    -s "TestSkipNonDistributableBlobs"
    -s "TestMetadataCollector"
    -s "TestIngestLeased"
    -s "TestContentLeased"
    -s "TestContent"
    -s "TestUsageCalculation"
    %dnl integration tests need network
    -t integration
    %dnl api is a separate module
    -d api
}
%gocheck2 %{test_ignores}
%endif
%post

%systemd_post containerd.service
%preun

%systemd_preun containerd.service
%postun

%systemd_postun_with_restart containerd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
