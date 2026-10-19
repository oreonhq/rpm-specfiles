%global source0_hash d52c89f053defbb406227a6af6107b31a818afa5ae7894d970e4b204fb6b31a2
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/yvasiyarov/gorelic
Version:                0.0.7
%gometa
%global common_description %{expand:
New Relic agent for Go runtime. It collect a lot of metrics about scheduler,
garbage collector and memory allocator and send them to NewRelic.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        New relic agent for Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gorelic-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/yvasiyarov/go-metrics)
BuildRequires:  golang(github.com/yvasiyarov/newrelic_platform_go)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

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
