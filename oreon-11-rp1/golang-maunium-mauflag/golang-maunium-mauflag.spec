%global source0_hash 533084852643732519b0e39afa6388a8481c1c44519e71244e72d4b7e333e46b
%bcond check 0
%global debug_package %{nil}
%global goipath         maunium.net/go/mauflag
%global forgeurl        https://github.com/tulir/mauflag
Version:                1.0.0
%gometa -L -f
%global common_description %{expand:
An extendable argument parser for Golang.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-maunium-mauflag
Release:        1%{?dist}
Summary:        An extendable argument parser for Golang
License:        GPL-3.0-only
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/mauflag-%{version}.tar.gz
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
