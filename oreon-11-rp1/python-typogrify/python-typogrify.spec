%global source0_hash f0aa004e98032a6e6be4c9da65e7eb7150e36ca3bf508adbcda82b4d003e61ee

%global pypi_name typogrify

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Filters to enhance web typography, with support for Django & Jinja templates

# typogrify/packages/titlecase/__init__.py is MIT
License:        BSD-3-Clause AND MIT
URL:            https://github.com/mintchaos/typogrify
Source:         %{pypi_source %{pypi_name}}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Typogrify provides a set of custom filters that automatically apply various
transformations to plain text in order to yield typographically-improved HTML.
While often used in conjunction with Jinja_ and Django_ template systems, the
filters can be used in any environment.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{pypi_name}-%{version}
# remove shebang line from the python scripts
for lib in $(find -type f -name '*.py'); do
 sed -i.python -e '1{\@^#!@d}' $lib
done

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
# importing typogrify.templatetags.jinja_filters needs jinja2 installed
# importing typogrify.templatetags.typogrify_tags needs django installed
%pyproject_check_import -e typogrify.templatetags.jinja_filters -e typogrify.templatetags.typogrify_tags

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.7-28
- Prepare for Oreon 11 (RP1)
