%global source0_hash c236c216a16e4286338e66e0947938944992f918fe827c31f8745c0be98818d2
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/NYTimes/gziphandler
Version:                1.1.1
%gometa
%global common_description %{expand:
This is a tiny Go package which wraps HTTP handlers to transparently gzip the
response body, for clients which support it. Although it's usually simpler to
leave that to a reverse proxy (like nginx or Varnish), this package is useful
when that's undesirable.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go middleware to gzip HTTP responses
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gziphandler-%{version}.tar.gz
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
