%global source0_hash e23b6901f784d1c066fb6a607fee616545fc76580a8f704af0c4e881be636c91
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/sigurn/crc16
%global commit          20ab5afb07e3b6cc942a504ec32bd8aeda3ca356
%gometa -f
%global common_description %{expand:
Go implementation of CRC-16 calculation for majority of widely-used
polynomials.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go CRC16 package
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/crc16-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
