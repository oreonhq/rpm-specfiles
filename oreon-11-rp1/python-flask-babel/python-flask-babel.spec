%global source0_hash 12104c31bd5dc91d876f512981dde24d7bf9ebf4840b9784b375ff3c88bd13d4

%global pkg_name flask-babel
%global mod_name flask_babel
%bcond_without docs

%if 0%{?rhel}
%undefine with_docs
%endif

Name:           python-%{pkg_name}
Version:        4.1.0
Release:        3%{?dist}
Summary:        Adds i18n/l10n support to Flask applications
License:        BSD-3-Clause
URL:            https://github.com/mitsuhiko/%{pkg_name}/
BuildArch:      noarch
Source0:        https://github.com/python-babel/flask-babel/archive/v%{version}/%{pkg_name}-%{version}.tar.gz
# Proposed fix for list-translations() ordering in tests (#2433806)
# https://github.com/python-babel/flask-babel/pull/242
Patch0:         0001-Fix-list-translations-ordering-in-tests.patch

# For documentation
%if %{with docs}
BuildRequires:  make
BuildRequires:  python3-docs
BuildRequires:  python3-furo
BuildRequires:  python3-sphinx
%endif

%global _description\
Adds i18n/l10n support to Flask applications with the help of the Babel library.

%description %_description

%package -n python3-%{pkg_name}
Summary:        Adds i18n/l10n support to Flask applications
# A modified version of speaklater is bundled
Provides:       bundled(python3-speaklater)
BuildRequires:  python3-devel
BuildRequires:  python3-pytest-mock

%description -n python3-%{pkg_name} %_description

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkg_name}-%{version}

%build
%pyproject_wheel

%if %{with docs}
# Build the documentation
make -C docs html

# We do not want the sphinx marker
rm -f docs/_build/html/.buildinfo
%endif

%install
%pyproject_install
%pyproject_save_files %{mod_name}

%check
%pytest

%files -n python3-%{pkg_name} -f %{pyproject_files}
%if %{with docs}
%doc docs/_build/html README.md
%else
%doc README.md
%endif
%license LICENSE

%changelog
%autochangelog
