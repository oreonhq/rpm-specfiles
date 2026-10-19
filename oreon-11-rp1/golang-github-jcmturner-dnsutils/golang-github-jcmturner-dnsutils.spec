%global source0_hash cf159f3bad90db84dc8c8814d10f10560c7ec83c4ec160dfad9502d4a17c9958
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jcmturner/dnsutils
Version:                2.0.0
%gometa
%global common_description %{expand:
DNS utils for Go.}
%global golicenses      LICENSE
Name:           %{goname}
Release:        1%{?dist}
Summary:        DNS utils for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/dnsutils-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
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

sed -i 's|github.com/jcmturner/dnsutils|github.com/jcmturner/dnsutils/v2|' $(find .  -maxdepth 1 -iname "*go" -type f)
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
