%global source0_hash b41555d6a36de28fd1b6b47171b4375d7ae3b38955205a5286fb190bd1ae37cd
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/ssor/bom
%global commit          6386211fdfcf24c0bfbdaceafd02849ed9a8a509
%gometa
%global common_description %{expand:
Small tools for cleaning bom from byte array or reader.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Small tools for cleaning bom from byte array or reader
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/bom-%{commit}.tar.gz
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
