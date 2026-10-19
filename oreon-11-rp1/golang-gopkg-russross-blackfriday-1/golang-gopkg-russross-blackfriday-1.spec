%global source0_hash 3c92006c3ff14cdeacc7edd992acb487749e7234dbc6f95e8fb8abfaf60cdc49
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/russross/blackfriday.v1
%global forgeurl        https://github.com/russross/blackfriday
Version:                1.6.0
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-github-russross-blackfriday-devel < 2.0.1-4
}
%global common_description %{expand:
Blackfriday is a Markdown processor implemented in Go. It is paranoid about its
input (so you can safely feed it user-supplied data), it is fast, it supports
common extensions (tables, smart punctuation substitutions, etc.), and it is
safe for all utf-8 (unicode) input.
HTML output is currently supported, along with Smartypants extensions.}
%global golicenses      LICENSE.txt
%global godocs          README.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Markdown processor for Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/blackfriday-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
