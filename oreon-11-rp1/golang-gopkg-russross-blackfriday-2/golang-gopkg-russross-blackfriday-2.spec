%global source0_hash a13af0fc5305713f5154693feaf654d024689efea76390091a5e8c757335b4f4
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/russross/blackfriday.v2
%global forgeurl        https://github.com/russross/blackfriday
Version:                2.1.0
%gometa
%global goaltipaths     github.com/russross/blackfriday/v2
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
License:        BSD
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
