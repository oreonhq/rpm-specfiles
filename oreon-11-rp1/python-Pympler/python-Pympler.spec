%global source0_hash 1eaa867cb8992c218430f1708fdaccda53df064144d1c5656b1e6f1ee6000424

%global pname pympler

%global desc \
Pympler is a development tool to measure, monitor and analyze the memory\
behavior of Python objects in a running Python application.\
\
By pympling a Python application, detailed insight in the size and the lifetime\
of Python objects can be obtained. Undesirable or unexpected runtime behavior\
like memory bloat and other “pymples” can easily be identified.\
\
Pympler integrates three previously separate modules into a single,\
comprehensive profiling tool. The asizeof module provides basic size information\
for one or several Python objects, module muppy is used for on-line monitoring\
of a Python application and module Class Tracker provides off-line analysis of\
the lifetime of selected Python objects.

Name: python-Pympler
Version: 1.1
Release: 9%{?dist}
Summary: Measure, monitor and analyze the memory behavior of Python objects
License: Apache-2.0 and BSD-3-Clause and MIT
# bundled stuff
# pympler/asizeof.py: BSD
# pympler/static/jquery.sparkline.min.js: BSD
# pympler/templates/jquery.flot*.min.js: MIT
URL: http://pythonhosted.org/Pympler/
Source0: https://pypi.python.org/packages/source/P/Pympler/%{pname}-%{version}.tar.gz
Patch0: python-Pympler-no-shebang.patch
BuildArch: noarch

%description
%{desc}

%package -n python3-Pympler
Summary: %{summary}
BuildRequires: python3-bottle
BuildRequires: python3-devel
BuildRequires: python3-matplotlib
BuildRequires: python3-setuptools
BuildRequires: python3-pip
BuildRequires: python3-wheel
Requires: python3-bottle
# http://www.flotcharts.org
Provides: bundled(js-jquery-flot) = 0.8.3
# https://github.com/krzysu/flot.tooltip
Provides: bundled(js-jquery-flot-tooltip) = 0.8.4
# http://omnipotent.net/jquery.sparkline/
Provides: bundled(js-jquery-sparkline) = 2.1.1
# asizeof.py is bundled
Provides: bundled(python%{python3_version}dist(asizeof))
# required by pympler/charts.py, but doesn't throw an exception without
Recommends: python3-matplotlib
# pympler/panels.py is an extension for django-debug-toolbar
Enhances: python3-django-debug-toolbar

%description -n python3-Pympler
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pname}-%{version}
rm pympler/util/bottle.py
chmod -x pympler/asizeof.py
%patch -P 0 -p1 -b .no-shebang

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pympler

# Disabled due to 3.13 failure: https://github.com/pympler/pympler/issues/163
#%%check
#PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py test

%files -n python3-Pympler -f %{pyproject_files}
%license LICENSE
%doc NOTICE README.md

%changelog
%autochangelog
