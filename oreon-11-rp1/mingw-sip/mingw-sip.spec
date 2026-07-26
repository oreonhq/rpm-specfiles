%global source0_hash dc2e58c1798a74e1b31c28e837339822fe8fa55288ae30e8986eb28100ebca5a

%global pypi_name sip

Name:           mingw-%{pypi_name}
Summary:        MinGW Windows SIP6
Version:        6.15.1
Release:        1%{?dist}

License:        BSD-2-Clause
Url:            http://www.riverbankcomputing.com/software/sip/intro
Source0:        %{pypi_source}
# Drop setuptools-scm requirement
Patch0:         sip_no-setuptools-scm.patch

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build

%description
MinGW Windows SIP6.

%package -n mingw32-%{pypi_name}
Summary:       MinGW Windows SIP6

%description -n mingw32-%{pypi_name}
MinGW Windows SIP6.

%package -n mingw64-%{pypi_name}
Summary:       MinGW Windows SIP6

%description -n mingw64-%{pypi_name}
MinGW Windows SIP6.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}
# Set version (see sip_no-setuptools-scm.patch)
sed -i 's|@version@|%version|' pyproject.toml

%build
# Host build
%{mingw32_py3_build_host_wheel}
%{mingw64_py3_build_host_wheel}

# Target build
%{mingw32_py3_build_wheel}
%{mingw64_py3_build_wheel}

%install
# Host build
%{mingw32_py3_install_host_wheel}
%{mingw64_py3_install_host_wheel}

# Target build
%{mingw32_py3_install_wheel}
%{mingw64_py3_install_wheel}

# Wrappers
mkdir -p %{buildroot}%{_bindir}

for file in %{buildroot}%{_prefix}/%{mingw32_target}/bin/sip-*; do
mv $file $file.py
cat << EOF > $file
#!/bin/sh
mingw32-python3 %{_prefix}/%{mingw32_target}/bin/`basename $file`.py "\$@"
EOF
chmod +x $file
ln -s %{_prefix}/%{mingw32_target}/bin/`basename $file` %{buildroot}%{_bindir}/mingw32-`basename $file`
done

for file in %{buildroot}%{_prefix}/%{mingw64_target}/bin/sip-*; do
mv $file $file.py
cat << EOF > $file
#!/bin/sh
mingw64-python3 %{_prefix}/%{mingw64_target}/bin/`basename $file`.py "\$@"
EOF
chmod +x $file
ln -s %{_prefix}/%{mingw64_target}/bin/`basename $file` %{buildroot}%{_bindir}/mingw64-`basename $file`
done

%files -n mingw32-%{pypi_name}
%license LICENSE
%{_bindir}/mingw32-sip-*
%{mingw32_bindir}/sip-*
%{mingw32_python3_sitearch}/sipbuild/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/
%{_prefix}/%{mingw32_target}/bin/sip-*
%{mingw32_python3_hostsitearch}/sipbuild/
%{mingw32_python3_hostsitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-%{pypi_name}
%license LICENSE
%{_bindir}/mingw64-sip-*
%{mingw64_bindir}/sip-*
%{mingw64_python3_sitearch}/sipbuild/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/
%{_prefix}/%{mingw64_target}/bin/sip-*
%{mingw64_python3_hostsitearch}/sipbuild/
%{mingw64_python3_hostsitearch}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
