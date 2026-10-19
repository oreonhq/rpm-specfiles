%global source0_hash dc7aedce4a8c174b01df8406ff7d92779e2df76cee2ad17fa2ff6777feddadec
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/rivo/uniseg
Version:                0.4.7
%gometa
%global common_description %{expand:
Unicode Text Segmentation, Word Wrapping, and String Width Calculation in Go.}
%global golicenses      LICENSE.txt
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Unicode Text Segmentation, Word Wrapping, and String Width Calculation in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/uniseg-%{version}.tar.gz
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
