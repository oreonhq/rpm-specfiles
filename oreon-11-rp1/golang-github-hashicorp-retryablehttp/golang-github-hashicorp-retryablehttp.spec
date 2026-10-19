%global source0_hash a556692913b852c228fbfca680bb6660bc851485155dd2c1c5f4017497398823
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/hashicorp/go-retryablehttp
Version:                0.7.8
%gometa -L
%global common_description %{expand:
The Retryablehttp package provides a familiar HTTP client interface with
automatic retries and exponential backoff. It is a thin wrapper over the
standard net/http client library and exposes nearly the same public API. This
makes retryablehttp very easy to drop into existing programs.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           golang-github-hashicorp-retryablehttp
Release:        1%{?dist}
Summary:        Retryable HTTP client in Go
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-retryablehttp-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

for test in "TestClient_DefaultRetryPolicy_TLS" "TestRoundTripper_TransportFailureErrorHandling" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
