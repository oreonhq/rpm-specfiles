%global source0_hash e27f04b8b5619747ebfb955699d6895c1e4c7c5e4478507ca4e2d8b658b8b51c
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%global goipath         mvdan.cc/gofumpt
%global forgeurl        https://github.com/mvdan/gofumpt
Version:                0.5.0
%gometa -L -f
%global common_description %{expand:
A stricter gofmt.}
%global golicenses      LICENSE LICENSE.google
%global godocs          CHANGELOG.md README.md
Name:           golang-mvdan-gofumpt
Release:        1%{?dist}
Summary:        A stricter gofmt
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/gofumpt-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/gofumpt %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%if %{with check}
rm -rf testdata/script/diagnose.txtar
%oreon_autofiles main

%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
