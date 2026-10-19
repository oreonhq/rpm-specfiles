%global source0_hash 044ab46b73e8aac007f504cf4e8c3ee3a2eb05c4c2a65018bd8b6f2c56a17f62
%bcond check 1
%global goipath         github.com/moby/buildkit
Version:                0.33.1
%global tag             v%{gsub %{version} ~ -}
%gometa -L -f
%global common_description %{expand:
Concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit.}
Name:           docker-buildkit
Release:        1%{?dist}
Summary:        Concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/buildkit-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Requires:       containerd
Requires:       runc
Requires:       containernetworking-plugins
Recommends:     qemu-user-static
Provides:       golang-github-moby-buildkit = %{version}-%{release}
Obsoletes:      golang-github-moby-buildkit < 0.12.0-1
# oreon:deps
BuildRequires:  docker-distribution
BuildRequires:  git
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
# no patch file at this time
# %%autopatch -p1

%build

%global buildtags   seccomp
%global specldflags -X %{goipath}/version.Version=%{version} -X %{goipath}/version.Revision=%{release} -X %{goipath}/version.Package=%{goipath}
export GO_BUILDTAGS="%{buildtags}"
export GO_LDFLAGS="%{specldflags}"
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%global test_ignores %{shrink:
    %dnl skip tests that fail with create tmp file: open - invalid argument
    -s "TestConversion"
    -s "TestSetBlob"
    -s "TestLoopLeaseContent"
    -s "TestSharingCompressionVariant"
    -s "TestContentAttachable"
    %dnl skip specific tests that fail with 'operation not permitted'
    -s "TestGetRemotes"
    -s "TestExtractOnMutable"
    -s "TestMergeOp"
    -s "TestDiffOp"
    -s "TestCLIIntegration"
    -s "TestSnapshotExtract"
    -s "TestJobsIntegration"
    -s "TestGhaCacheIntegration"
    %dnl exclude directories where tests fail with 'operation not permitted'
    -d cache/contenthash
    -t source
    -d client
    -d frontend
    -t frontend/dockerfile
    -d snapshot
    -t util/overlay
}
%gocheck2 %{test_ignores}
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
