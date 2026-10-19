%global source0_hash 0edb42adb5f7405d33920e21acba412b00bf9a8fbe97075924fd57c58ca6cad1
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/josharian/native
Version:                1.0.0
%gometa -f
%global common_description %{expand:
Easy to use native encoding/binary.ByteOrder.}
%global golicenses      license
%global godocs          readme.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Easy to use native encoding/binary.ByteOrder
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/native-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
