%global source0_hash 6b4cdf64fd6b919b65be75fdfcfb6a42c9738730ee18453e26641132ecc177b4
%bcond check 0
%global goipath         github.com/docker/buildx
Version:                0.37.2
%global tag             v%{gsub %{version} ~ -}
%gometa -L -f
%global common_description %{expand:
Docker CLI plugin for extended build capabilities with BuildKit.}
Name:           docker-buildx
Release:        1%{?dist}
Summary:        Docker CLI plugin for extended build capabilities with BuildKit
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND Unicode-DFS-2016
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/buildx-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
%if %{with check}
%endif
Requires:       docker-cli
# oreon:deps
BuildRequires:  git-core
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  moby-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global buildtags   seccomp
%global specldflags -X %{goipath}/version.Version=%{version} -X %{goipath}/version.Revision=%{release} -X %{goipath}/version.Package=%{goipath}
export GO_BUILDTAGS="%{buildtags}"
export GO_LDFLAGS="%{specldflags}"
%gobuild -o %{gobuilddir}/bin/buildx %{goipath}/cmd/buildx
%install
%go_vendor_license_install -c %{S:2}
install -Dpm 0755 %{gobuilddir}/bin/buildx %{buildroot}%{moby_cli_plugins_dir}/docker-buildx
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
rm tests/integration_test.go
%gocheck -d util/gitutil
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
