%global source0_hash none

Name:           build-constraints-rpm-macros
Version:        1
Release:        12%{?dist}
Summary:        RPM macros for build constraints

License:        MIT
URL:            https://src.fedoraproject.org/rpms/%{name}
Source0:        macros.build-constraints

# license text
Source200:      LICENSE

BuildArch:      noarch

Requires:       gawk

%description
This package contains macros to constraint resource use during the build
process.

%prep
%autosetup -c -T
cp -a %{sources} .

%build

%install
%if 0%{?el7}
# install -Dt does not precreate target directory
mkdir -p %{buildroot}%{rpmmacrodir}
%endif
install -Dpm 644 -t %{buildroot}%{rpmmacrodir} macros.*

%files
%license LICENSE
%{rpmmacrodir}/macros.build-constraints

%changelog
%autochangelog
