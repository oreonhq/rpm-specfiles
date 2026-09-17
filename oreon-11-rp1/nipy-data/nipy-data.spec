%global source0_hash 84f8330d492174fdccd6e5b991794abad1b0c91c3a035d0e0a01e192c57a36d8

Name:           nipy-data
Version:        0.2
Release:        25%{?dist}
Summary:        Test data and brain templates for nipy

# from main nipy repository
License:        BSD-3-Clause
URL:            http://nipy.org/nipy/
Source0:        http://nipy.org/data-packages/nipy-data-%{version}.tar.gz
Source1:        http://nipy.org/data-packages/nipy-templates-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -a 1

%install
mkdir -p %{buildroot}%{_datadir}/nipy/nipy/
for i in data templates
do
  cp -a nipy-$i-%{version}/$i/ %{buildroot}%{_datadir}/nipy/nipy/
  cp -a nipy-$i-%{version}/README.txt ./README-$i.txt
done

%files
%doc README-data.txt README-templates.txt
%{_datadir}/nipy/

%changelog
%autochangelog
