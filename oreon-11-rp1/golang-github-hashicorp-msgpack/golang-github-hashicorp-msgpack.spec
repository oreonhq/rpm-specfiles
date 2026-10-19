%global source0_hash 5d78248c5d9c7abf03e8f7d6c93fd488e338e98e0d9ee9a1d98724ce3637e206
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/hashicorp/go-msgpack
Version:                2.1.5
%gometa -f
%global goaltipaths		github.com/hashicorp/go-msgpack/v2
%global common_description %{expand:
High Performance, Feature-Rich Idiomatic codec/encoding library}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Open-Source Go Code. msgpack.org[Go]
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-msgpack-%{version}.tar.gz
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
