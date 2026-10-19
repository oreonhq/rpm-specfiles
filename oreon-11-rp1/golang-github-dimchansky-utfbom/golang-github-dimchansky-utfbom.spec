%global source0_hash 081a9e23640c56f9a90cb76ce538c6cfb33b58ea58d4e6253533adf238904166
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/dimchansky/utfbom
Version:                1.1.1
%gometa
%global common_description %{expand:
The package utfbom implements the detection of the BOM (Unicode Byte Order
Mark) and removing as necessary. It can also return the encoding detected
by the BOM.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Detection of the BOM and removing as necessary
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/utfbom-%{version}.tar.gz
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
