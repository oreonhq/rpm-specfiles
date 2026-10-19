%global source0_hash 379bbf93dc3365a5c5fcd6c2538b63f21f9e5493a439b69999e01fad3de1ea39
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/distribution/reference
Version:                0.6.0
%gometa -f
%global common_description %{expand:
Go library for handling references to container images held in container
registries.}
%global golicenses      LICENSE
%global godocs          README.md SECURITY.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go library to handle references to container images
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/reference-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
