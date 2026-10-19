%global source0_hash 411a20eeacb4b474e57b33a1515e4ab21153e234d15235a294abc556cc0764e7
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gogs/chardet
%global commit          b7413eaefb8fa9e364c87539451333f77500ffee
%gometa
%global common_description %{expand:
A fork of saintfish/chardet.}
%global golicenses      LICENSE
%global godocs          AUTHORS README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        A fork of saintfish/chardet
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/chardet-%{commit}.tar.gz
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
