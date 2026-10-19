%global source0_hash d28780f21377085732bc2925ee1192a29f3e4c3fab82316a714a6e14fa52e42a
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/google/go-querystring
Version:                1.2.0
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-github-google-go-querystring-devel < 1.0.0-3
}
%global common_description %{expand:
Go-querystring is Go library for encoding structs into URL query parameters.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go library for encoding structs into url query parameters
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-querystring-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/google/go-cmp/cmp)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
