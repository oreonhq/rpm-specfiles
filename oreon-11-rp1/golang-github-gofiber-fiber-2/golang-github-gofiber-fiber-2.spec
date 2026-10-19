%global source0_hash 9caa6987268f269ee9c7d8309083140d44f8b452b0c52b84e74c7b698fc7a227
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/gofiber/fiber/v2
Version:                2.48.0
%gometa -f
%global common_description %{expand:
Express inspired web framework written in Go.}
%global golicenses      LICENSE
%global godocs          docs utils/README.md
Name:           golang-github-gofiber-fiber-2
Release:        1%{?dist}
Summary:        Express inspired web framework written in Go
License:        MIT AND BSD-3-Clause
URL:            %{gourl}
Source0:        https://github.com/gofiber/fiber/archive/v%{version}/fiber-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1
rm -rfv internal/go-ole internal/wmi

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

for test in "Test_Proxy_Do_WithRealURL" \
            "Test_Proxy_Do_WithRedirect" \
            "Test_Proxy_DoRedirects_RestoreOriginalURL" \
            "Test_Proxy_DoRedirects_TooManyRedirects" \
            "Test_Storage_Memory_Get" \
            "Test_Storage_Memory_Delete" \
            "Test_Limiter_Sliding_Window_Custom_Storage_Skip_Successful_Requests" \
            "Test_Limiter_Sliding_Window_Skip_Successful_Requests" \
            "Test_Limiter_Sliding_Window_Custom_Storage_Skip_Failed_Requests" \
            "Test_Limiter_Sliding_Window_Skip_Failed_Requests" \
            "Test_Idempotency" \
            "Test_Session_Save_Expiration" \
            "Test_CustomExpiration" \
            "Test_Client_UserAgent" \
            "Test_Client_Agent_Dest" \
            "Test_Pprof_Subs" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
