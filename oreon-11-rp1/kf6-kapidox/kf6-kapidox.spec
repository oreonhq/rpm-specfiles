%global framework kapidox

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:    kf6-%{framework}
Version: 6.24.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 4 scripts and data for building API documentation

License: BSD
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

## downstream patches

# Fix kapidox installing in a broken state.
# See: https://invent.kde.org/frameworks/kapidox/-/issues/14
Patch0:  fix-broken-installation.patch

## upstream patches

# make sure BuildArch comes *after* patches, to ensure %%autosetup works right
BuildArch:      noarch

BuildRequires:  kf6-rpm-macros
BuildRequires:  python3-devel

Requires:       kf6-filesystem
Requires:       doxygen
Requires:       qt6-doc-devel

# Required for the import test
BuildRequires:  python3dist(gv)

%global __python %{__python3}
%global python_sitelib %{python3_sitelib}

%description
Scripts and data for building API documentation (dox) in a standard format and
style.


%prep
%autosetup -n %{framework}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files kapidox

%check
# Test suite don't run, so we'll do a simple import test.
%pyproject_check_import

%files -f %{pyproject_files}
%license LICENSES/*.txt
%{_kf6_bindir}/depdiagram_generate_all
%{_kf6_bindir}/kapidox-depdiagram-generate
%{_kf6_bindir}/kapidox-depdiagram-prepare
%{_kf6_bindir}/kapidox-generate


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
