%global source0_hash ea2ccf508594f935661e29854496f350f0b83680dd9a4d630dd3e3e03652951e
Name:           R-mlbench
Version:        %R_rpm_version 2.1-6
Release:        1%{?dist}
Summary:        Machine Learning Benchmark Problems
License:        GPL-2.0-only
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=mlbench&version=2.1-6#/mlbench_2.1-6.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A collection of artificial and real-world machine learning benchmark
problems, including, e.g., several data sets from the UCI repository.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Fix encoding.
iconv --from=ISO-8859-1 --to=UTF-8 mlbench/NEWS > NEWS.new && \
    touch -r mlbench/NEWS NEWS.new && \
    mv NEWS.new mlbench/NEWS

%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
