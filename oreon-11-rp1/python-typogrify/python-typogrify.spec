# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 8be4668cda434163ce229d87ca273a11922cb1614cb359970b7dc96eed13cb38
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global pypi_name typogrify

Name:           python-%{pypi_name}
Version:        2.0.7
Release:        28%{?dist}
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
%oreon_verify_sources
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
