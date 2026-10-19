%global source0_hash 4d83772262864d35f8490d919eb405aa47c44d5b703496494b3141c691ed8987
%bcond check 0
%global goipath         ariga.io/atlas
%global forgeurl        https://github.com/ariga/atlas
Version:                1.3.0
%gometa
%global common_description %{expand:
A database toolkit.}
%global golicenses      LICENSE
%global godocs          doc README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A database toolkit
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/atlas-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/cmd/atlas
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
