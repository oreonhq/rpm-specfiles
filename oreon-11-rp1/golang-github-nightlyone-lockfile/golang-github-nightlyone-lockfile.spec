%global source0_hash ab6ae9054edde30a2d1adfd757bcd1d4610742a826cdad8b6e8c85c673f5d525
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/nightlyone/lockfile
Version:                1.0.0
%gometa
%global common_description %{expand:
Handle locking via pid files.}
%global golicenses      LICENSE
%global godocs          README.md
%global gosupfiles      glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Handle locking via pid files
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/lockfile-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
