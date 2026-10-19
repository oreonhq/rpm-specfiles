%global source0_hash 89d8aa45b05c9cd5e66c40a5c4f3a5224dbf9632d1fd1e27d05f2ad26effae32
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/jcmturner/aescts.v1
%global forgeurl        https://github.com/jcmturner/aescts
Version:                1.0.1
%gometa
%global common_description %{expand:
AES CBC Ciphertext Stealing mode for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        AES CBC Ciphertext Stealing mode for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/aescts-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

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
