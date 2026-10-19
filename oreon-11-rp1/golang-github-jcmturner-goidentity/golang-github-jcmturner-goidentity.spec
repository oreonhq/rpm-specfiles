%global source0_hash 493e40431872340d8b7fdebb6ebb76442d0d52f362f4414bf28b69305c36fd81
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jcmturner/goidentity
Version:                6.0.1
%gometa
%global common_description %{expand:
Standard interface for holding authenticated identities and their attributes.}
%global golicenses      LICENSE
%global godocs          v6/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Standard interface for holding authenticated identities and their attributes
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/goidentity-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/hashicorp/go-uuid)
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

sed -i 's|github.com/jcmturner/goidentity|github.com/jcmturner/goidentity/v6|' $(find .  -maxdepth 1 -iname "*go" -type f)
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
