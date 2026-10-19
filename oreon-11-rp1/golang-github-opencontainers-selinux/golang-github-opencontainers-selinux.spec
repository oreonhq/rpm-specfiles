%global source0_hash d38db799fbb67e15d5fe5f4efee219e64add3d74dff5d823e9de44b1be28ab3a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/opencontainers/selinux
Version:                1.15.1
%gometa
%global common_description %{expand:
Common SELinux package used across the container ecosystem.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
%global gosupfiles      ${selinux[@]}
Name:           %{goname}
Release:        1%{?dist}
Summary:        Common selinux implementation
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/selinux-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
mapfile -t selinux <<< $(find . -name "*.go" -type f)
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
