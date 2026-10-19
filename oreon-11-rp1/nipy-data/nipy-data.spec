%global source1_hash 1809903e2671450b0373a5e743c7b40a574739668163d285c13466ee4c48915b
%global source0_hash 6193d3dcf9e0c32fae370696c66df41923beac7a7f649a7c6be42e0671e9d676
Name:           nipy-data
Version:        0.3
Release:        1%{?dist}
Summary:        Test data and brain templates for nipy
License:        BSD-3-Clause
URL:            http://nipy.org/nipy/
Source0:        http://nipy.org/data-packages/nipy-data-%{version}.tar.gz
Source1:        http://nipy.org/data-packages/nipy-templates-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%install
mkdir -p %{buildroot}%{_datadir}/nipy/nipy/
for i in data templates
do
  cp -a nipy-$i-%{version}/$i/ %{buildroot}%{_datadir}/nipy/nipy/
  cp -a nipy-$i-%{version}/README.txt ./README-$i.txt
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
