%global source0_hash 830abe53f98e7a46ccbd829114998e1d7bbe9edfeb669011e7970d684493809e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/VividCortex/gohistogram
Version:                1.0.0
%gometa
%global common_description %{expand:
This package provides Streaming Approximate Histograms for efficient quantile
approximations.
The histograms in this package are based on the algorithms found in Ben-Haim &
Yom-Tov's A Streaming Parallel Decision Tree Algorithm. Histogram bins do not
have a preset size. As values stream into the histogram, bins are dynamically
added and merged.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Streaming approximate histograms in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gohistogram-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
