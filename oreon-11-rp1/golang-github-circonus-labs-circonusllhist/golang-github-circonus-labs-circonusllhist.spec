%global source0_hash ec28fd8dc0f033cdfd5538d68f2b69e7f9989bc0d4cd2c6ae4509fdf5b8a26b3
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/circonus-labs/circonusllhist
Version:                0.4.1
%gometa
%global common_description %{expand:
Package Circllhist provides an implementation of Circonus fixed log-linear
histogram data structure. This allows tracking of histograms in a composable way
such that accurate error can be reasoned about.}
%global golicenses      LICENSE
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go implementation of Circonus log-linear histograms
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/circonusllhist-%{version}.tar.gz
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
