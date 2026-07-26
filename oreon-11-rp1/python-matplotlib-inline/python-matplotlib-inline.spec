%global source0_hash bf48c58f1d5c961ebcb8302953ace3a83201db530f8c03c16701e13bef85b841

Name:           python-matplotlib-inline
Version:        0.2.1
Release:        2%{?dist}
Summary:        Inline Matplotlib backend for Jupyter

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/ipython/matplotlib-inline
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Inline Matplotlib backend for Jupyter

%package -n     python3-matplotlib-inline
Summary:        %{summary}

%description -n python3-matplotlib-inline
Inline Matplotlib backend for Jupyter

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n matplotlib-inline-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files matplotlib_inline

%files -n python3-matplotlib-inline -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
