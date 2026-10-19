%global source0_hash 0a6b7a5175aeb38c52ae794d49373f2a9baa5a5e47b7cf430db2cbb668297689
%bcond check 0
%global goipath         github.com/mailru/easyjson
Version:                0.9.2
%gometa
%global common_description %{expand:
Package Easyjson provides a fast and easy way to marshal/unmarshal Go structs
to/from JSON without the use of reflection. In performance tests, easyjson
outperforms the standard encoding/json package by a factor of 4-5x, and other
JSON encoding packages by a factor of 2-3x.
Easyjson aims to keep generated Go code simple enough so that it can be easily
optimized or fixed. Another goal is to provide users with the ability to
customize the generated code by providing options not available with the
standard encoding/json package, such as generating "snake_case" names or
enabling omitempty behavior by default.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Fast JSON serializer for golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/easyjson-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

for cmd in easyjson; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d tests
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
