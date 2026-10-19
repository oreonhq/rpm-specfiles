%global source0_hash abc354944874dd761abe22058e792fa6d454fad66bf6aaad84ddd892ababf5af
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/dchest/siphash
Version:                1.2.3
%gometa
%global common_description %{expand: Go implementation of SipHash-2-4, a fast
short-input PRF created by Jean-Philippe Aumasson and Daniel J. Bernstein
(http://131002.net/siphash/).}
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go implementation of SipHash-2-4, a fast short-input PRF
License:        CC0-1.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/siphash-%{version}.tar.gz
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
