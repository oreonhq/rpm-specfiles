%global source0_hash d6f042dd46aba79c4e7302ff20ec17878c41a8543d167845a73c26a108c082d1

%global srcname templated-dictionary
%global python3_pkgversion 3

%if 0%{?rhel} == 7
%global python3_pkgversion 36
%endif

Name:       python-%{srcname}
Version:    1.6
Release:    6%{?dist}
Summary:    Dictionary with Jinja2 expansion

License:    GPL-2.0-or-later
URL:        https://github.com/xsuchy/templated-dictionary

# Source is created by:
# git clone https://github.com/xsuchy/templated-dictionary && cd templated-dictionary
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %name-%version.tar.gz

BuildArch: noarch

%if 0%{?rhel} > 10 || 0%{?fedora} > 42
BuildRequires: python%{python3_pkgversion}-devel
%else
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
%endif

BuildRequires: python%{python3_pkgversion}-setuptools
Requires:      python%{python3_pkgversion}-jinja2

%global _description\
Dictionary where __getitem__() is run through Jinja2 template.

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%{?py_provides:%py_provides python3-%{srcname}}
%description -n python3-%{srcname} %_description

%if 0%{?rhel} > 10 || 0%{?fedora} > 42
%generate_buildrequires
%pyproject_buildrequires
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%if 0%{?rhel} > 10 || 0%{?fedora} > 42
version="%version" %pyproject_wheel
%else
version="%version" %py3_build
%endif

%install
%if 0%{?rhel} > 10 || 0%{?fedora} > 42
version=%version %pyproject_install
%else
version=%version %py3_install
%endif

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/templated_dictionary/
%if 0%{?rhel} > 10 || 0%{?fedora} > 42
%{python3_sitelib}/*.dist-info
%else
%{python3_sitelib}/templated_dictionary-*.egg-info/
%endif

%changelog
%autochangelog
