%global source0_hash 3386467289656998fe32e7fe6889a0944506f43351b36c1a480c815bcdee1ac8
%bcond check 0
%global goipath         github.com/docker/compose-switch
Version:                1.0.5
%gometa -L -f
%global common_description %{expand:
Compose Switch is a replacement for the Compose V1 "docker-compose" (python)
executable. It translates the command line into Compose V2 "docker compose" and
then runs the latter.
}
Name:           docker-compose-switch
Release:        1%{?dist}
Summary:        docker-compose CLI shim
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/compose-switch-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Requires:       docker-compose >= 2
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

GO_LDFLAGS="-X %{goipath}/internal.Version=%{version}"
%gobuild -o %{gobuilddir}/bin/docker-compose %{goipath}
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
