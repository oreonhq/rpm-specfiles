%global source0_hash 3f0d7bcdcea6d6267a816bc62360a7c632ade149054932ec8e40423e74016b40

%global srcname enthought-sphinx-theme
%global modname enthought_sphinx_theme

Name:           python-%{srcname}
Version:        0.7.3
Release:        %autorelease
Summary:        Sphinx theme for Enthought projects

# Bundled bootstrap is MIT
# Bundles the fonts Source Sans Pro and Source Code Pro from Adobe Systems Incorporated under the 
# SIL Open Font License, Version 1.1.
# Automatically converted from old format: BSD and MIT and OFL - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-OFL
URL:            https://github.com/enthought/enthought-sphinx-theme
Source0:        https://github.com/enthought/enthought-sphinx-theme/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
Sphinx theme for Enthought projects, derived from the Scipy theme.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
Provides:       bundled(bootstrap) = 2.3.2

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

#check
# No tests

%files -n python3-%{srcname} -f %{pyproject_files}
%license licenses/*.txt
%doc CHANGES.rst README.rst

%changelog
%autochangelog
