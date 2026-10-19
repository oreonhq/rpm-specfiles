%global source0_hash b14b147ea9afd54039691f9bb7e0d2dc9aae9e5416f61d240cec5132f9a78113
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/ProtonMail/go-crypto
Version:                1.5.2
%gometa -L
%global common_description %{expand:
Fork of go/x/crypto, providing an up-to-date OpenPGP implementation.}
%global golicenses      LICENSE PATENTS
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           golang-github-protonmail-crypto
Release:        1%{?dist}
Summary:        Fork of go/x/crypto, providing an up-to-date OpenPGP implementation
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-crypto-%{version}.tar.gz
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

%ifarch i686
%gocheck -d github.com/ProtonMail/go-crypto/openpgp
%else
%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
