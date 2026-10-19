%global source0_hash 7efa2aec34f47af45bdab3e1888e4adaf76fc0505180c832f76b7df1c5513e8b
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/multiformats/go-base32
Version:                0.0.4
%gometa
%global common_description %{expand:
Base32 encoding package from go with NoPadding option.}
%global golicenses      LICENSE
Name:           %{goname}
Release:        1%{?dist}
Summary:        Base32 encoding package from go with NoPadding option
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-base32-%{version}.tar.gz
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
