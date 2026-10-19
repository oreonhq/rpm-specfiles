%global source0_hash d9428d95a1ff5105c6e050e5f351140ebc8c00b6545ceccdea533429a4c286db
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-chi/chi
Version:                5.3.2
Epoch:                  1
%gometa
%global goaltipaths     github.com/go-chi/chi/v5
%global common_description %{expand:
Chi is a lightweight, idiomatic and composable router for building Go HTTP
services. It's especially good at helping you write large REST API services that
are kept maintainable as your project grows and changes. chi is built on the new
context package introduced in Go 1.7 to handle signaling, cancelation and
request-scoped values across a handler chain.
The focus of the project has been to seek out an elegant and comfortable design
for writing REST API servers, written during the development of the Pressly API
service that powers our public API service, which in turn powers all of our
client-side applications.}
%global golicenses      LICENSE
%global godocs          _examples CHANGELOG.md CONTRIBUTING.md README.md\\\
                        SECURITY.md
Name:           golang-github-chi
Release:        1%{?dist}
Summary:        Lightweight, idiomatic and composable router for building Go HTTP services
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/chi-%{version}.tar.gz
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
