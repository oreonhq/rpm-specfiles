%global source0_hash eedd7ad24c1a32e9790a9dfb503f194b8551d5feb1737ff033013d484923cd02
%bcond check 0
%global debug_package %{nil}
%global goipath         pkg.nimblebun.works/go-lsp
%global forgeurl        https://github.com/nimblebun/go-lsp
Version:                1.1.0
%gometa -L -f
%global common_description %{expand:
Language server protocol types and documentation for go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-pkg-nimblebun-lsp
Release:        1%{?dist}
Summary:        Language server protocol types and documentation for go
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/go-lsp-%{version}.tar.gz
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
