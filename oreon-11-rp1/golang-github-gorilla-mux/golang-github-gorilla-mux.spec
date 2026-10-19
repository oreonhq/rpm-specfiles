%global source0_hash c2a09e78d1886abb2d291b472eba3ac9185acb35234c1f5616669664ba893d6d
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/gorilla/mux
Version:                1.8.1
%gometa -L -f
%global common_description %{expand:
Package gorilla/mux implements a request router and dispatcher for matching
incoming requests to their respective handler.
The name mux stands for "HTTP request multiplexer". Like the standard
http.ServeMux, mux.Router matches incoming requests against a list of registered
routes and calls a handler for the route that matches the URL or other
conditions. The main features are:
 - It implements the http.Handler interface so it is compatible with the
   standard http.ServeMux.
 - Requests can be matched based on URL host, path, path prefix, schemes,
   header and query values, HTTP methods or using custom matchers.
 - URL hosts, paths and query values can have variables with an optional
   regular expression.
 - Registered URLs can be built, or "reversed", which helps maintaining
   references to resources.
 - Routes can be used as subrouters: nested routes are only tested if the
   parent route matches. This is useful to define groups of routes that share
   common conditions like a host, a path prefix or other repeated attributes.
   As a bonus, this optimizes request matching.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-gorilla-mux
Release:        1%{?dist}
Summary:        A powerful HTTP router and URL matcher for building Go web servers
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/mux-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
