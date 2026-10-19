%global source0_hash 1591d32f4b88b078f86566a1db1e91e036b564a17ef2e62283bdcb58bc310fff
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/lex
%global forgeurl        https://gitlab.com/cznic/lex
Version:                1.1.0
%global tag             v1.1.0
%gometa
%global common_description %{expand:
Support for a *nix (f)lex like tool on .l sources.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Support for a *nix (f)lex like tool on .l sources
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/lex-%{tag}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/golex %{goipath}
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
