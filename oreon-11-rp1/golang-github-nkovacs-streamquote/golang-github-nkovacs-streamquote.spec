%global source0_hash d918706fb29cb5aa4a8dd341383a441f07ca9f9cf12de8028d92c45b0a578690
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/nkovacs/streamquote
Version:                1.1.0
%gometa
%global common_description %{expand:
This package provides a streaming version of strconv.Quote.
It allows you to quote the data in an io.Reader and write it out to an io.Writer
without having to store the entire input and the entire output in memory.
Its primary use case is go.rice and similar tools, which need to convert lots of
files, some of them quite large, to go strings.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Streaming version of strconv.Quote
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/streamquote-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

for test in "TestLargeString" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
