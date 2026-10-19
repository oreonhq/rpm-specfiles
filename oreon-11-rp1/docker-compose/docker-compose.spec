%global source0_hash 311077662698fd8e34769a894f9d5240befb1730990efa8ed58e0fa8725d2d84
%bcond check 0
%global goipath         github.com/docker/compose/v5
Version:                5.5.1
%global tag             v%{gsub %{version} ~ -}
%gometa -L -f
%global common_description %{expand:
Define and run multi-container applications with Docker.}
Name:           docker-compose
Release:        1%{?dist}
Summary:        Define and run multi-container applications with Docker
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://github.com/docker/compose/archive/v%{version}/compose-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Requires:       (docker-cli or podman-docker)
Suggests:       docker-cli >= 28.0.0
Requires:       moby-filesystem
Recommends:       docker-compose-switch
Conflicts:      docker-compose-plugin
# oreon:deps
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

export GO_LDFLAGS="-X %{goipath}/internal.Version=%{version}"
%gobuild -o %{gobuilddir}/bin/docker-compose %{goipath}/cmd
%install
%go_vendor_license_install -c %{S:2}
install -Dpm 0755 \
    %{gobuilddir}/bin/docker-compose \
    %{buildroot}%{moby_cli_plugins_dir}/docker-compose
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%global test_ignores %{shrink:
    %dnl possibly fixed in next upstream release
    -s "TestValidatePathInBase"
    %dnl e2e tests require external services
    -d pkg/e2e
}
%gocheck2 %{test_ignores}
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
