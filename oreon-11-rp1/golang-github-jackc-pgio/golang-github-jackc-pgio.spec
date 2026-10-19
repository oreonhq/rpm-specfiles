%global source0_hash d36e367c877954acdc96b8cd1a0df417b4cfae80dae726474a8f0de3a68a68ab
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jackc/pgio
Version:                1.0.0
%gometa
%global common_description %{expand:
Package Pgio is a low-level toolkit building messages in the PostgreSQL wire
protocol.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Low-level toolkit building messages in the PostgreSQL wire protocol
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pgio-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
