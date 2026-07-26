%global source0_hash d18b0a9b2cf0427d05b9b8a955bf7bb1028c9849fb2fa44c562d0fe34b6e3655

%global pypi_name pelican
Name:           python-%{pypi_name}
Version:        4.11.0
Release:        4%{?dist}
Summary:        A tool to generate a static blog from reStructuredText or Markdown input files

# Automatically converted from old format: AGPLv3
License:        AGPL-3.0-only
URL:            http://getpelican.com
Source0:        https://github.com/getpelican/pelican/archive/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
Pelican is a static site generator, written in Python_.

* Write your weblog entries directly with your editor of choice (vim!)
  in reStructuredText_ or Markdown_
* Includes a simple CLI tool to ...

%package -n python3-%{pypi_name}
Summary:        A tool to generate a static blog from reStructuredText or Markdown input files

Obsoletes:      python-%{pypi_name} < 3.7.1-4
Obsoletes:      python2-%{pypi_name} < 3.7.1-4
Conflicts:      python2-%{pypi_name} < 3.7.1-4
Provides:       %{pypi_name} == %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-blinker
BuildRequires:  python3-sphinx
BuildRequires:  python3-unidecode
BuildRequires:  python3-rich

BuildRequires:  python3-markdown
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-lxml
BuildRequires:  python3-jinja2
BuildRequires:  python3-feedgenerator
BuildRequires:  python3-dateutil
BuildRequires:  python3-sphinxext-opengraph
BuildRequires:  python3-furo

BuildRequires:  python3-pygments
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-xdist
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/diff

Requires:  python3-blinker
Requires:  python3-six
Requires:  python3-unidecode
Requires:  python3-jinja2
Requires:  python3-pytz
Requires:  python3-pygments
Requires:  python3-docutils
Requires:  python3-markdown
Requires:  python3-feedparser
Requires:  python3-dateutil
Requires:  python3-feedgenerator

%description -n python3-%{pypi_name}
Pelican is a static site generator, written in Python_.

* Write your weblog entries directly with your editor of choice (vim!)
  in reStructuredText_ or Markdown_
* Includes a simple CLI tool to ...

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -S git -n %{pypi_name}-%{version}
# make file not zero length to silence rpmlint
echo " " > pelican/themes/simple/templates/tag.html

# remove bangpath #!/usr/bin/env from files
sed -i '1d' pelican/tools/pelican_import.py
sed -i '1d' pelican/tools/pelican_quickstart.py
sed -i '1d' pelican/tools/pelican_themes.py
sed -i '1d' pelican/tools/templates/pelicanconf.py.jinja2
sed -i '1d' pelican/tools/templates/publishconf.py.jinja2

# release pygments constraints
sed -i 's/.*pygments.*/    "pygments",/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# build docs
PYTHONPATH=.:$PYTHONPATH sphinx-build-3 docs html

# remove leftovers from sphinxbuild
rm html/_downloads/*/theme-basic.zip html/_static/theme-basic.zip
rm -rf html/.doctrees html/.buildinfo

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name} -L

# backwards compatibility helpers
ln -s ./pelican %{buildroot}/%{_bindir}/pelican-3
ln -s ./pelican-import %{buildroot}/%{_bindir}/pelican-import-3
ln -s ./pelican-quickstart %{buildroot}/%{_bindir}/pelican-quickstart-3
ln -s ./pelican-themes %{buildroot}/%{_bindir}/pelican-themes-3

%check
%pyproject_check_import -t

# re-checked tests, upstream is on python3.8, we are using 3.9.
# pytest -s --cov=pelican pelican

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc html README.rst

%{_bindir}/pelican
%{_bindir}/pelican-import
%{_bindir}/pelican-plugins
%{_bindir}/pelican-quickstart
%{_bindir}/pelican-themes

%{_bindir}/pelican-3
%{_bindir}/pelican-import-3
%{_bindir}/pelican-quickstart-3
%{_bindir}/pelican-themes-3

%changelog
%autochangelog
