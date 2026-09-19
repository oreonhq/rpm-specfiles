%global source0_hash d55b809129a8c829a4bdce2bf36f9c26c3df649100b13bfdc4b5afd02edc9504

Name:           python-gradunwarp
Version:        1.2.3
Release:        %autorelease
Summary:        Gradient Unwarping

%global forgeurl https://github.com/Washington-University/gradunwarp
%global tag %{version}
%forgemeta

# SPDX
License:        MIT
URL:            %forgeurl
Source0:        %forgesource
Source1:        gradient_unwarp.1

BuildArch:  noarch

%description
Python/Numpy package used to unwarp the distorted volumes (due to the gradient
field inhomogenities).

%package -n python3-gradunwarp
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
# used in setup.py
BuildRequires:  python3-numpy
# not mentioned in setup.py
BuildRequires:  python3-scipy
BuildRequires:  python3-nibabel
# not mentioned in setup.py
Requires:  python3-numpy
Requires:  python3-scipy
Requires:  python3-nibabel

%description -n python3-gradunwarp
Python/Numpy package used to unwarp the distorted volumes (due to the gradient
field inhomogenities).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
# correct version string
# remove extra compilation flags
sed -i -e "s/HCP-%{version}/%{version}/" \
    -e "s/extra_compile_args=.*)/)/" \
    setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# install script
mv %{buildroot}%{_bindir}/gradient_unwarp.py %{buildroot}%{_bindir}/gradient_unwarp
sed -i -e '1s|^.*$|#!%{__python3}|' %{buildroot}%{_bindir}/gradient_unwarp

%pyproject_save_files gradunwarp

# install man page generated using help2man
install -m 0644 %{SOURCE1} -Dt $RPM_BUILD_ROOT/%{_mandir}/man1/

%check
# See: https://github.com/Washington-University/gradunwarp/blob/master/.github/workflows/test.yml
%pytest --pyargs gradunwarp
# Run import test in addition
%pyproject_check_import

%files -n python3-gradunwarp -f %{pyproject_files}
%exclude %{python3_sitelib}/gradunwarp/core/gradient_unwarp.py
%license Copying.md
%doc README.md
%{_bindir}/gradient_unwarp
%{_mandir}/man1/gradient_unwarp.*

%changelog
%autochangelog
