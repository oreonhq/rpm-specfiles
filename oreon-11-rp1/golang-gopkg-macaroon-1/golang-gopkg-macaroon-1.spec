%global source0_hash 6fc21b56a0135bb3776b719516f70e93386731d58369197d3cd2417b41de4722
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/macaroon.v1
%global forgeurl        https://github.com/go-macaroon/macaroon
Version:                1.0.0
%gometa
%global common_description %{expand:
The Macaroon package implements macaroons as described in the paper "Macaroons:
Cookies with Contextual Caveats for Decentralized Authorization in the Cloud"
(http://theory.stanford.edu/~ataly/Papers/macaroons.pdf)}
%global golicenses      LICENSE
%global godocs          README.md TODO
Name:           %{goname}
Release:        1%{?dist}
Summary:        Native Go implementation of macaroons
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/macaroon-%{version}.tar.gz
Patch0:         0001-Convert-int-to-string-using-rune.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/crypto/nacl/secretbox)
BuildRequires:  golang(gopkg.in/check.v1)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
