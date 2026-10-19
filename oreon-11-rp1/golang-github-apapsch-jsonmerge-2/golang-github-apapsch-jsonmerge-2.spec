%global source0_hash 617f4e0c2029a2e6858a56c5fb2f8e6637cfdab42e4cfbfc8d2b95899fdee6fd
%bcond check 0
%global goipath         github.com/apapsch/go-jsonmerge/v2
%global forgeurl        https://github.com/apapsch/go-jsonmerge
Version:                2.0.0
%gometa -f
%global common_description %{expand:
Merge JSON objects.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Merge JSON objects
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/go-jsonmerge-%{version}.tar.gz
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

%gobuild -o %{gobuilddir}/bin/jsonmerge %{goipath}/cmd/jsonmerge
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
