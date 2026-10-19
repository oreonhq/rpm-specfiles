%global source0_hash 6ddc6bc4e94a0b3a8366bdd5674b4c2890faca1171afc3f7d20aec95e2c8d413
%ifnarch aarch64
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/shopspring/decimal
Version:                1.4.0
%gometa
%global common_description %{expand:
Package Decimal implements an arbitrary precision fixed-point decimal.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Arbitrary-precision fixed-point decimal numbers in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/decimal-%{version}.tar.gz
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
