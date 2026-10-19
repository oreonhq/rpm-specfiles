%global source0_hash 5b6ff8719485a712ad59935416df001d16d9d4b9fee6d36014f0f285a91d6047
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/lestrrat-go/xstrings
%global commit          cacb16b8ddb78da759e593009f982ee9ba7151c4
%gometa -f
%global common_description %{expand:
Unicode-aware string utilities for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Unicode-aware string utilities for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/xstrings-%{commit}.tar.gz
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
