%global source0_hash 6656199c1599fa8b334dde6ddcf09d4147aadd52ec26668130c8fdd11f8d78eb
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/soniakeys/quant
Version:                1.0.0
%gometa -f
%global common_description %{expand:
An interface for image color quantizers.}
%global golicenses      license
%global godocs          changelog.md readme.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        An interface for image color quantizers
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/quant-%{version}.tar.gz
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
