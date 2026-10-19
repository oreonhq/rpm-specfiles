%global source0_hash 9b08bd280dcadce234effaa3945891e1fe8d6729721dd891d222764b399dd48a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mdlayher/raw
%global commit          50f2db8cc0658568575938a39dbaa46172921d98
%gometa
%global common_description %{expand:
Package Raw enables reading and writing data at the device driver level for a
network interface.}
%global golicenses      LICENSE.md
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Read and write data at the device driver level for a network interface
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/raw-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(golang.org/x/net/bpf)
BuildRequires:  golang(golang.org/x/sys/unix)
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
