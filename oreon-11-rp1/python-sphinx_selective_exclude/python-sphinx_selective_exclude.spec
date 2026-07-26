%global source0_hash 76fc8fd7c24311e0ca2199a9e4db2156585acd7652a5cead98b07ef4f70f9b78

%global srcname sphinx_selective_exclude

# Upstream does not have any tests yet
%bcond_with tests

Name:           python-%{srcname}
Version:        1.0.3
Release:        21%{?dist}
Summary:        Sphinx eager ".. only::" directive and other selective rendition extensions

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
Url:            https://github.com/pfalcon/sphinx_selective_exclude
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
The implementation of ".. only::" directive in Sphinx documentation generation
tool is known to violate principles of least user surprise and user expectations
in general. Instead of excluding content early in the pipeline (preprocessor
style), Sphinx defers exclusion until output phase, and what's the worst,
various stages processing ignore "only" blocks and their exclusion status, so
they may leak unexpected information into ToC, indexes, etc.

This projects tries to rectify situation on users' side. It actually changes the
way Sphinx processes "only" directive, but does this without forking the
project, and instead is made as a standard Sphinx extension, which a user may
add to their documentation config. Unlike normal extensions, extensions provided
in this package monkey-patch Sphinx core to work in a way expected by users.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
Requires:       python3-sphinx

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
%autochangelog
