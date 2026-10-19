%global source0_hash 6beca48af3066fc8d87c3ce17c5dd3debac61ff8f296c0e95c0634fd3ab05599
%bcond check 1
%global goipath         github.com/johnkerl/miller/v6
Version:                6.13.0
%gometa -L -f
%global common_description %{expand:
Miller is like awk, sed, cut, join, and sort for name-indexed data such as CSV,
TSV, and tabular JSON.
With Miller, you get to use named fields without needing to count positional
indices, using familiar formats such as CSV, TSV, JSON, JSON Lines, and
positionally-indexed. Then, on the fly, you can add new fields which are
functions of existing fields, drop fields, sort, aggregate statistically,
pretty-print, and more.}
Name:           miller
Release:        1%{?dist}
Summary:        Name-indexed data processing tool
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
URL:            %{gourl}
Source0:        https://github.com/johnkerl/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Patch:          miller-go1_24-non_constant_string.diff
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

# These should not be shipped
rm -rf cmd/experiments

%build

for cmd in cmd/mlr ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
