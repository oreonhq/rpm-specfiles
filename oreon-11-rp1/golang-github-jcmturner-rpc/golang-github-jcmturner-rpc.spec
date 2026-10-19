%global source0_hash 4bedb66a89dd261063d42e5f08d22eab3373ef529a78d72800f8727b62336ca3
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jcmturner/rpc
Version:                2.0.3
%gometa
%global common_description %{expand:
Remote Procedure Call libraries
(http://pubs.opengroup.org/onlinepubs/9629399/).}
%global golicenses      LICENSE
%global godocs          v2/examples v2/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Remote Procedure Call libraries
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/rpc-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(golang.org/x/net/http2/hpack)
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

sed -i 's|github.com/jcmturner/rpc|github.com/jcmturner/rpc/v2|' $(find .  -maxdepth 2 -iname "*go" -type f)
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
