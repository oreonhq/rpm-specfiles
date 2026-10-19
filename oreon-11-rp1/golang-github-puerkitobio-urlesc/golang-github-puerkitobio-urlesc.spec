%global source0_hash 4bf883606155d8ed9c8ca5bd794e412025a16e3532d2b06053ff95f74fc3a9b2
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/PuerkitoBio/urlesc
%global commit          de5bf2ad457846296e2031421a34e2568e304e35
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-github-PuerkitoBio-urlesc-devel < 0-0.9
Obsoletes:      golang-github-PuerkitoBio-urlesc-unit-test-devel < 0-0.9
}
%global common_description %{expand:
Package urlesc implements query escaping as per RFC 3986.
It contains some parts of the net/url package, modified so as to allow some
reserved characters incorrectly escaped by net/url.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Proper URL escaping as per RFC3986
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/urlesc-%{commit}.tar.gz
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
