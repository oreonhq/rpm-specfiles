%global source0_hash 7de15bf4a2600dc584bed0f25431dfed6bf20a7a5bc935a48d2ce50063339815

%global pypi_name pecan
%{!?_licensedir:%global license %%doc}
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-%{pypi_name}
Version:        1.7.0
Release:        5%{?dist}
Summary:        A lean WSGI object-dispatching web framework

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/pecan/pecan
Source0:        %pypi_source
BuildArch:      noarch

%description
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies

%package -n python3-%{pypi_name}
Summary:        A lean WSGI object-dispatching web framework

BuildRequires:  python3-devel

Conflicts:     python2-%{pypi_name} < 1.3.2-5

%description -n python3-%{pypi_name}
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/pecan
%{_bindir}/gunicorn_pecan

%changelog
%autochangelog
