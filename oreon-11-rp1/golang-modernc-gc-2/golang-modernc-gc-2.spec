%global source0_hash 7a9df6392652a409328caba7c80f97b4bd6eeeffbd412734a011d4b76448eb92
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/gc/v2
%global forgeurl        https://gitlab.com/cznic/gc
Version:                2.6.3
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
Package gc is a Go compiler front end. Work in progess.}
%global golicenses      GO-LICENSE LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Package gc is a Go compiler front end. Work in progess
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/gc-%{tag}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
find . ! \( -name v2 -o -name _build -o -name AUTHORS -o -name CONTRIBUTORS -o -name GO-LICENSE -o -name LICENSE \) -maxdepth 1 -exec rm -rvf {} \;
mv v2/* .

%build

%gobuild -o %{gobuilddir}/bin/gc %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

rm -rfv internal/ebnf/all_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
