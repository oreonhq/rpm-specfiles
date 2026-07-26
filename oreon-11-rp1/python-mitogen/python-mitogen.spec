%global source0_hash dd0d6f0046e53409325cec43e7fa727b62f48dd09c4a2c06586886aa8fdb12ba

# what it's called on pypi
%global srcname mitogen
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

Name:           python-%{pkgname}
Version:        0.3.29
Release:        2%{?dist}
Summary:        Distributed self-replicating programs in Python

License:        LicenseRef-Callaway-BSD
URL:            https://github.com/dw/mitogen
Source0:        %pypi_source
BuildArch:      noarch

%global common_description %{expand:
Mitogen is a Python library for writing distributed self-replicating programs.

There is no requirement for installing packages, copying files around, writing
shell snippets, upfront configuration, or providing any secondary link to a
remote machine aside from an SSH connection. Due to its origins for use in
managing potentially damaged infrastructure, the remote machine need not even
have free disk space or a writeable filesystem.

It is not intended as a generic RPC framework; the goal is to provide a robust
and efficient low-level API on which tools like Salt, Ansible, or Fabric can be
built, and while the API is quite friendly and comparable to Fabric, ultimately
it is not intended for direct use by consumer software.

The focus is to centralize and perfect the intricate dance required to run
Python code safely and efficiently on a remote machine, while avoiding
temporary files or large chunks of error-prone shell scripts, and supporting
common privilege escalation techniques like sudo, potentially in combination
with exotic connection methods such as WMI, telnet, or console-over-IPMI.}

%description %{common_description}

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{pkgname} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p 1
# No compat support needed
rm -r mitogen/compat ansible_mitogen/compat

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{srcname}

%check
# tests/README.md says the tests need:
#    - internet connection
#    - working docker daemon

%files -n python%{python3_pkgversion}-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{python3_sitelib}/ansible_%{libname}

%changelog
%autochangelog
