%global source0_hash 9b81d6a9ea62e75a04a1a9d9f931942016890beec9ab5d129a2a4432cf595c0a

# Wants to download sample data, also wants firefox or geckodriver etc.
# So, we skip tests and rely on upstream's CI
%bcond_with tests

%global pypi_name bokeh

%global _description %{expand:
Bokeh is an interactive visualization library for modern web browsers. It
provides elegant, concise construction of versatile graphics, and affords
high-performance interactivity over large or streaming data sets. Bokeh can help
anyone who would like to quickly and easily make interactive plots, dashboards,
and data applications.}

Name:           python-%{pypi_name}
Version:        3.6.3
Release:        1%{?dist}
Summary:        Interactive plots and applications in the browser from Python

# License breakdown: licensecheck -r . | sed '/UNKNOWN/ d' | sort -t ':' -k 2
# The software is released under the BSD license, but includes files that are
# independently also marked with ASL 2.0 and MIT licenses
# The JS bits are npm based

# ASL:
# bokeh/palettes.py
# bokeh/server/static/lib/lib.*

# BSD:
# bokeh/server/static/js/bokeh-api.js
# bokeh/server/static/js/bokeh-api.legacy.js
# bokeh/server/static/js/bokeh-api.legacy.min.js
# bokeh/server/static/js/bokeh-api.min.js
# bokeh/server/static/js/bokeh.js
# bokeh/server/static/js/bokeh.legacy.js
# bokeh/server/static/js/bokeh.legacy.min.js
# bokeh/server/static/js/bokeh.min.js
# bokeh/server/static/js/bokeh-tables.js
# bokeh/server/static/js/bokeh-tables.legacy.js
# bokeh/server/static/js/bokeh-widgets.js
# bokeh/server/static/js/bokeh-widgets.legacy.js
# bokeh/server/static/js/bokeh-widgets.legacy.min.js
# bokeh/server/static/js/bokeh-widgets.min.js
# bokeh/server/static/js/compiler.js
# bokeh/server/static/js/compiler/prelude.js
# tests/unit/bokeh/test___init__.py
# bokeh/server/static/js/lib/api/palettes.js
# bokeh/server/static/js/types/api/palettes.d.ts

# MIT (Expat)
# bokeh/server/static/js/lib/core/util/array.js
# bokeh/server/static/js/lib/core/util/callback.js
# bokeh/server/static/js/lib/core/util/types.js
# bokeh/server/static/js/lib/core/util/wheel.js
# bokeh/server/static/js/types/core/util/wheel.d.ts

# Multiple licenses:
# bokeh/server/static/js/bokeh.json: Expat License Apache License 2.0
# bokeh/server/static/js/bokeh-tables.legacy.min.js: Expat License BSD 3-clause "New" or "Revised" License
# bokeh/server/static/js/bokeh-tables.min.js: Expat License BSD 3-clause "New" or "Revised" License

# Also see the breakdown in the bundled JS below
# and https://github.com/bokeh/bokeh/blob/branch-2.2/bokehjs/LICENSE
# Automatically converted from old format: BSD and ASL 2.0 and MIT and ISC - review is highly recommended.
License:        BSD-3-Clause AND Apache-2.0 AND MIT AND ISC
URL:            https://github.com/bokeh/bokeh
Source0:        %pypi_source
# Read package-lock.json and general list of bundled runtime libraries their versions
Source1:        parse-deps.py

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

###### Bundles various js bits #####
# From: https://github.com/bokeh/bokeh/blob/0b9526ef553d938bf5de187e2511564c648c13bd/bokehjs/package-lock.json
# using parse-deps.py
# Also verify using the instructions here
# https://github.com/bokeh/bokeh/blob/branch-2.2/bokehjs/LICENSE#L45
# MIT
Provides: bundled(nodejs-@bokeh/numbro) = 1.6.2
# MIT
Provides: bundled(nodejs-@bokeh/slickgrid) = 2.4.4103
# MIT
Provides: bundled(nodejs-@types/jquery) = 3.5.29
# MIT
Provides: bundled(nodejs-@types/sizzle) = 2.3.8
# MIT
Provides: bundled(nodejs-@types/slickgrid) = 2.1.40
# MIT
Provides: bundled(nodejs-choices.js) = 10.2.0
# MIT
Provides: bundled(nodejs-deepmerge) = 4.3.1
# MIT
Provides: bundled(nodejs-esm) = 3.2.25
# ISC
Provides: bundled(nodejs-flatbush) = 4.4.0
# MIT
Provides: bundled(nodejs-flatpickr) = 4.6.13
# ISC
Provides: bundled(nodejs-flatqueue) = 2.0.3
# ASL 2.0
Provides: bundled(nodejs-fuse.js) = 6.6.2
# MIT
Provides: bundled(nodejs-jquery-ui) = 1.13.2
# MIT
Provides: bundled(nodejs-jquery) = 3.7.1
# ASL 2.0
Provides: bundled(nodejs-mathjax-full) = 3.2.2
# ASL 2.0
Provides: bundled(nodejs-mhchemparser) = 4.2.1
# MIT
Provides: bundled(nodejs-nouislider) = 15.7.1
# MIT
Provides: bundled(nodejs-proj4) = 2.11.0
# MIT
Provides: bundled(nodejs-regl) = 2.1.0
# MIT
Provides: bundled(nodejs-redux) = 4.2.1
# BSD
Provides: bundled(nodejs-sprintf-js) = 1.1.4
# MIT
Provides: bundled(nodejs-timezone) = 1.0.23
# BSD
Provides: bundled(nodejs-tslib) = 2.7.0
# MIT
Provides: bundled(nodejs-underscore.template) = 0.1.7
# MIT
Provides: bundled(nodejs-wkt-parser) = 1.3.3

# Optional deps
# https://docs.bokeh.org/en/latest/docs/installation.html#installation
Recommends:       %{py3_dist jupyter-core}
Recommends:       %{py3_dist networkx}
Recommends:       %{py3_dist pandas}
Recommends:       %{py3_dist psutil}
Recommends:       %{py3_dist sphinx}

# Bokeh will look for whatever browser is available and use that, so not adding
# firefox etc to Recommends
# https://docs.bokeh.org/en/latest/docs/user_guide/export.html#userguide-export

%if %{with tests}
BuildRequires:  %{py3_dist beautifulsoup4}
BuildRequires:  %{py3_dist flaky}
BuildRequires:  %{py3_dist Jinja2} >= 2.7
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist nbconvert}
BuildRequires:  %{py3_dist networkx}
BuildRequires:  %{py3_dist numpy} >= 1.11.3
BuildRequires:  %{py3_dist packaging} >= 16.8
BuildRequires:  %{py3_dist pillow} >= 7.1.0
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist python-dateutil} >= 2.1
BuildRequires:  %{py3_dist PyYAML} >= 3.10
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist selenium}
BuildRequires:  %{py3_dist tornado} >= 5.1
BuildRequires:  %{py3_dist typing_extensions} >= 3.7.4
%endif

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1
rm -rf %{pypi_name}.egg-info
# Add to generate correctly egg-info
sed -i 's/dynamic = \["version"\]/version = "%{version}"'/ pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Remove zero length file
rm -f %{buildroot}/%{python3_sitelib}/bokeh/server/static/.keep
# Remove static typing information generated files
rm -rf %{buildroot}/%{python3_sitelib}/typings

%check
%if %{with tests}
# https://docs.bokeh.org/en/latest/docs/dev_guide/testing.html
# skip js tests, skip selenium tests
%pytest -m "not selenium" tests/unit
%endif

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
%{python3_sitelib}/%{pypi_name}

%changelog
%autochangelog
