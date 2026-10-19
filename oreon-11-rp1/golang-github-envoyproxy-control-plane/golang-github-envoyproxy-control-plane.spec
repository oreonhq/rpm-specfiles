%global source0_hash f5973fcd5e93ff7e061ea4f0f21248a0df537f4cf87040ca94993a83f150ed25
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/envoyproxy/go-control-plane
Version:                0.14.0
%gometa
%global common_description %{expand:
Go implementation of data-plane-api.}
%global golicenses      LICENSE
%global godocs          docs examples CHANGELOG.md CONTRIBUTING.md OWNERS.md\\\
                        README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go implementation of data-plane-api
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-control-plane-%{version}.tar.gz
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
