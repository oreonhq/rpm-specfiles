%global source0_hash ea32205bc5c1190eb59b06284fe5332bc7462bf35ca69eed405c74a30746dcb5
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/JohnCGriffin/overflow
%global commit          46fa312c352cdb9517817d04f2067d49f418e332
%gometa -f
%global common_description %{expand:
Check for int/int64/int32 arithmetic overflow in Golang.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Check for int/int64/int32 arithmetic overflow in Golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/overflow-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1
# https://github.com/JohnCGriffin/overflow/pull/5
sed -n '/^MIT License/,$p' README.md > LICENSE

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
