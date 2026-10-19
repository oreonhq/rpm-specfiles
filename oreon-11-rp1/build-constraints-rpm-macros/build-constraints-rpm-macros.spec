%global source0_hash none
Name:           build-constraints-rpm-macros
Version:        1
Release:        12%{?dist}
Summary:        RPM macros for build constraints
License:        MIT
URL:            https://src.fedoraproject.org/rpms/%{name}
Source0:        macros.build-constraints
Source200:      LICENSE
BuildArch:      noarch
Requires:       gawk
# oreon:deps

# /oreon:deps
%description
This package contains macros to constraint resource use during the build
process.

%prep

%autosetup -c -T
cp -a %{sources} .

%build

%install
%if 0%{?el7}
mkdir -p %{buildroot}%{rpmmacrodir}
%endif
install -Dpm 644 -t %{buildroot}%{rpmmacrodir} macros.*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
