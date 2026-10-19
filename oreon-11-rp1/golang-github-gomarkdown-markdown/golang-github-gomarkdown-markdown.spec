%global source0_hash ae5755583d1ebe6572c0f4960d999628800799cb000998af095f59315e668fbb
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gomarkdown/markdown
%global commit          722100d81a8e7c2e0019667c25e498c02e86ea0a
%gometa
%global common_description %{expand:
Package Markdown is a very fast Go library for parsing Markdown documents and
rendering them to HTML.
It's fast and supports common extensions.}
%global golicenses      LICENSE.txt
%global godocs          README.md changes-from-blackfriday.md todo.md\\\
                        tracking-perf.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Markdown parser and HTML renderer for Go
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/markdown-%{commit}.tar.gz
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
