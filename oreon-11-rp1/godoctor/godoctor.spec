%global source0_hash c1517a444783224fdad46b7a7ce82407b714b121f60b17e9df9834b5b6773332
%bcond check 0
%global goipath         github.com/godoctor/godoctor
Version:                0.8
%gometa -L -f
%global common_description %{expand:
Go Doctor - The Golang Refactoring Engine.}
%global golicenses      LICENSE
%global godocs          doc README.md
Name:           godoctor
Release:        1%{?dist}
Summary:        A golang refactoring tool
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          0001-Skip-names-tests-that-use-modules.patch
Patch:          0002-Skip-tests-that-appear-to-be-broken.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/godoctor %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%global gotestflags %{gotestflags} -timeout 60m
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
