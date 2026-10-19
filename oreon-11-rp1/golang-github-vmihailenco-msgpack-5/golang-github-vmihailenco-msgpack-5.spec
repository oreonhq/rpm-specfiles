%global source0_hash ea944f50da36f44c610e36591b089724fed30414834c9fd1689052c94322d77b
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/vmihailenco/msgpack/v5
Version:                5.3.5
%gometa
%global common_description %{expand:
MessagePack encoding for Golang v5.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        MessagePack encoding for Golang v5
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://github.com/vmihailenco/msgpack/archive/v%{version}/msgpack-%{version}.tar.gz
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
