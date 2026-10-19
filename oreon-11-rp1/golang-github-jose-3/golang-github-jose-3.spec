%global source0_hash 06fe2a7dbc16f27993a979eeb3a20c2608a02ea2d04480ed3141056be98c279c
%bcond check 0
%global goipath         github.com/go-jose/go-jose/v3
Version:                3.0.0
%gometa -f
%global common_description %{expand:
An implementation of JOSE standards (JWE, JWS, JWT) in Go.}
%global golicenses      LICENSE LICENSE-json
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        An implementation of JOSE standards (JWE, JWS, JWT) in Go
License:        BSD-3-Clause AND Apache-2.0
URL:            %{gourl}
Source0:        https://github.com/go-jose/go-jose/archive/v%{version}/go-jose-%{version}.tar.gz
Patch0:         b7b32c1007cb6e57ac14c6959f6546ca1591f591.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1
mv json/LICENSE LICENSE-json
sed -i "s|github.com/go-jose/go-jose/jose-util|github.com/go-jose/go-jose/v3/jose-util|" $(find . -iname "*.go" -type f)

%build

%gobuild -o %{gobuilddir}/bin/jose-util %{goipath}/jose-util
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
