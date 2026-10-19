%global source0_hash c4f1730194afc9ebe2636b3a069c6795b863619003ea6394c6b1978af9ce6326
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/boombuler/barcode
Version:                1.1.0
%gometa
%global common_description %{expand:
This is a package for Go which can be used to create different types of
barcodes.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Barcode creation lib for golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/barcode-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
