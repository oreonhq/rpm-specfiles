%global source0_hash 1860ac06fe7d2d6af727c4a1007e3ccd6c09da99464be8307201f1710b799cd4

Name:		uARMSolver
Version:	0.4.0
Release:	2%{?dist}
Summary:	Universal Association Rule Mining Solver

License:	MIT
URL:		https://github.com/firefly-cpp/uARMSolver
Source0:	https://github.com/firefly-cpp/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	make

%description
uARMSolver allows users to preprocess their data in a transaction database, to 
make discretization of data, to search for association rules and to guide a
presentation/visualization of the best rules found using external tools. 
Mining the association rules is defined as an optimization and solved using 
the nature-inspired algorithms that can be incorporated easily. Because 
the algorithms normally discover a huge amount of association rules, the 
framework enables a modular inclusion of so-called visual guiders for 
extracting the knowledge hidden in data, and visualize these using 
external tools. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{set_build_flags}
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 ./bin/uARMSolver %{buildroot}/%{_bindir}/%{name}
	
install -D -t '%{buildroot}%{_mandir}/man1' -m 0644 %{name}.1

rm -f %{buildroot}%{_infodir}/dir

%files
%{_bindir}/uARMSolver
%license LICENSE
%doc bin/README.txt
%doc README.md
%doc CHANGELOG.md CODE_OF_CONDUCT.md
%doc docs/2010.10884.pdf docs/231.pdf
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
