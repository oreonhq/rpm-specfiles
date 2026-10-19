%global source0_hash e8df04c4630080ad9407f31cf259b67a320b59a671903d33da325c3911373ac3
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/zmap/rc2
%global commit          abaa705312480a270106b104862e79c8a024dd91
%gometa
%global common_description %{expand:
The RC2 Cipher in Golang.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        RC2 Cipher in Golang
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/rc2-%{commit}.tar.gz
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
