%global source0_hash 22b94323762b49f1f6985dfce0bc5ec8f43b3a5ddaceb1b577c00038d25c8d3d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/sergi/go-diff
Version:                1.4.0
%gometa -f
%global common_description %{expand:
Diff, match and patch text in Go.}
%global golicenses      APACHE-LICENSE-2.0 LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Diff, match and patch text in Go
License:        Apache-2.0 AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-diff-%{version}.tar.gz
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
