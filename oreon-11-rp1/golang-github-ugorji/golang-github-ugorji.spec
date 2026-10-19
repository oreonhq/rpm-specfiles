%global source0_hash a95b1ce976e5ffed7c7b95d228781d047f4c3ff7de40ac3d7940b65ead38f77a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/ugorji/go
Version:                1.2.8
%gometa
%global common_description %{expand:
Idiomatic codec and rpc lib for msgpack, cbor, json, etc.}
%global golicenses      LICENSE
%global godocs          FAQ.md msgpack.org.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Idiomatic codec and rpc lib for msgpack, cbor, json, etc.
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d codec/bench
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
