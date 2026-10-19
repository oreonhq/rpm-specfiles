%global source0_hash f9e260b43d7b2ef28714d876c1960a776bdbf1b3b9829f0572048cae7692f052
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/emersion/go-sasl
%global commit          0b9dcfb154ac3d7515b08bc2691a0332800edfe9
%gometa
%global common_description %{expand:
A SASL library written in Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        SASL library written in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-sasl-%{commit}.tar.gz
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
