%global source0_hash c23caf5bc7b390fbd338a994ec6fb4b7d00d442b9fc8d99ecf5d773cf3c05616
%ifnarch ppc64le s390x
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/remyoudompheng/bigfft
%global commit          eec4a21b6bb01e5c1260ca5e04d0c58e11e20f30
%gometa
%global common_description %{expand:
Big integer multiplication library for Go using Fast Fourier transform.}
%global golicenses      LICENSE
%global godocs          README
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Big integer multiplication library for Go using Fast Fourier transform
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/bigfft-%{commit}.tar.gz
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
