%global source0_hash fe4be1d56d46dd42e382fb9c80a4749f80e1ae8910f9a03ef214abaaa10d8623
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jcmturner/aescts
Version:                2.0.0
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
Source0:        https://%{goipath}/archive/v%{version}/aescts-%{version}.tar.gz
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

sed -i 's|github.com/jcmturner/aescts|github.com/jcmturner/aescts/v2|' $(find . -maxdepth 1 -iname "*go" -type f)
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
