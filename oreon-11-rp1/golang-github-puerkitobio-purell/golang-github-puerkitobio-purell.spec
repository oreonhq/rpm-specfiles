%global source0_hash 2cc85b92059715a3b53a486c1ba162fb612040eb98cde0ba24de1581ed6da007
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/PuerkitoBio/purell
Version:                1.2.2
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-github-PuerkitoBio-purell-devel < 1.1.1-2
Obsoletes:      golang-github-PuerkitoBio-purell-unit-test-devel < 1.1.1-2
}
%global common_description %{expand:
Purell is a tiny Go library to normalize URLs. It returns a pure URL.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Tiny Go library to normalize URLs
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/purell-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/PuerkitoBio/urlesc)
BuildRequires:  golang(golang.org/x/net/idna)
BuildRequires:  golang(golang.org/x/text/unicode/norm)
BuildRequires:  golang(golang.org/x/text/width)
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
