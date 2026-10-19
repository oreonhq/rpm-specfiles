%global source0_hash 52ad91168ccaddba195b43fbb4c2de7a7b94cb86f5b3e0119dc037a6a87f31b2
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/aykevl/go-wasm
%global commit          42b86c49413943f0f64000fbb9ed4d4829e5e26f
%gometa -L -f
%global common_description %{expand:
WebAssembly binary file parser written in go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-aykevl-wasm
Version:        0
Release:        1%{?dist}
Summary:        WebAssembly binary file parser written in go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-wasm-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

# Remove the binary, as this package is only used for the Go library, and the
# binary can come from the original fork, if needed.
# It also causes an unfulfilled dependency on the original repo, since the
# import is not patched.
rm -r cmd/

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
