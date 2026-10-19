%global source0_hash 197465ef53219f3aeb1a6940b70e16d288fe4e4108d4831b91ea101118440e63
%bcond check 0
%global goipath         github.com/dgrijalva/jwt-go
Version:                3.2.0
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-github-dgrijalva-jwt-go-devel < 3.2.0-3
}
%global common_description %{expand:
Golang implementation of json web tokens (jwt).}
%global golicenses      LICENSE
%global godocs          MIGRATION_GUIDE.md VERSION_HISTORY.md README.md README-jwt.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang implementation of json web tokens (jwt)
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/jwt-go-%{version}.tar.gz
Source1:        glide.lock
Source2:        glide.yaml
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .
mv cmd/jwt/README.md README-jwt.md

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
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
