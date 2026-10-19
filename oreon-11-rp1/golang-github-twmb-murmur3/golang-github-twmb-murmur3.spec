%global source0_hash e72a62bc9770e6bc1282cee9cbb2f6fe7213a239528d51d2fb9b0a4f190b7022
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/twmb/murmur3
Version:                1.1.5
%gometa
%global common_description %{expand:
Fast, fully fledged murmur3 in Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Fast, fully fledged murmur3 in Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/murmur3-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  gcc-c++
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
