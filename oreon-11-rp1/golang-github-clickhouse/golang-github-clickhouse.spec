%global source0_hash 42700c08c7347b9069c3c6213d89b430ce97c66ac659b9302e948965aea3b1ce
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/ClickHouse/clickhouse-go
Version:                2.48.0
%gometa
%global common_description %{expand:
Golang driver for ClickHouse.}
%global golicenses      LICENSE lib/lz4/LICENSE-lz4
%global godocs          examples CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang driver for ClickHouse
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/clickhouse-go-%{version}.tar.gz
Patch0:         %{url}/pull/381.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/DataDog/golz4)
BuildRequires:  golang(github.com/bkaradzic/go-lz4)
BuildRequires:  golang(github.com/jmoiron/sqlx)
BuildRequires:  golang(github.com/pierrec/lz4)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1
mv lib/lz4/LICENSE lib/lz4/LICENSE-lz4

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
