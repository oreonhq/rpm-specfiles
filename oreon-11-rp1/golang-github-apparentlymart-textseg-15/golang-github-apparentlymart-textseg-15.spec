%global source0_hash d73ee2bce8c1a8e35b0355a8cb66d05cd65a07099b7edaf1e44edc51cf33210d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/apparentlymart/go-textseg/v15
Version:                15.0.0
%gometa -f
%global common_description %{expand:
Go implementation of Unicode Text Segmentation.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-apparentlymart-textseg-15
Release:        1%{?dist}
Summary:        Go implementation of Unicode Text Segmentation
License:        Apache-2.0 AND MIT
URL:            %{gourl}
Source0:        https://github.com/apparentlymart/go-textseg/archive/v%{version}/go-textseg-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

rm -rfv autoversion

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
