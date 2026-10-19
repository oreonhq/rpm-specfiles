%global source0_hash 3ae548d994c4d356337f1e966fef84d3c38f76033625e05340bab4435a875e88
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jedib0t/go-pretty/v6
Version:                6.8.3
%gometa -f
%global common_description %{expand:
Table-writer and more in golang!}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md SECURITY.md
Name:           golang-github-jedib0t-pretty-6
Release:        1%{?dist}
Summary:        Table-writer and more in golang
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/jedib0t/go-pretty/archive/v%{version}/go-pretty-%{version}.tar.gz
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
