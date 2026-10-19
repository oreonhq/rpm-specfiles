%global source0_hash bec332b844f48e4b4f00f1051619b95b43a5362ded929c5f7c4d80be054844bb
%bcond check 0
%global goipath         modernc.org/golex
%global forgeurl        https://gitlab.com/cznic/golex
Version:                1.0.1
%global tag             v1.0.1
%gometa
%global common_description %{expand:
A lex/flex like (not fully POSIX lex compatible) utility.}
%global golicenses      LICENSE
%global godocs          examples AUTHORS CONTRIBUTORS README
Name:           %{goname}
Release:        1%{?dist}
Summary:        A lex/flex like (not fully POSIX lex compatible) utility
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/golex-%{tag}.tar.bz2
Patch0001:      0001-Fix-build-with-Go-1.24.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/golex %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

rm -rfv lex/example_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
