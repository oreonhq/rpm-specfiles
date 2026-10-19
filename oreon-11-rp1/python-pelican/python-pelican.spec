%global source0_hash 3983b5d2dc84c7bdf967154359077a2b78c0bbd2f7dcc55292133a7779609458
Name:           python-pelican
Version:        4.12.0
Release:        1%{?dist}
Summary:        Static site generator supporting Markdown and reStructuredText
License:        AGPL-3.0-or-later
URL:            https://getpelican.com
Source0:        https://files.pythonhosted.org/packages/source/p/pelican/pelican-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pelican = %{version}-%{release}
# /oreon:deps
%package -n       python3-pelican+markdown
Summary:        Metapackage for python3-pelican markdown extras
Requires:       python3-pelican = %{version}-%{release}
Requires:       python3dist(markdown) >= 3.1
Provides:       python3dist(pelican[markdown]) = %{version}-%{release}

%description -n python3-pelican+markdown
Metapackage for python3-pelican markdown extras.

%description

%package -n     python3-pelican
Summary:        Static site generator supporting Markdown and reStructuredText
# oreon:reqs
Requires:       python3dist(blinker) >= 1.7.0
Requires:       python3dist(docutils) >= 0.22.0
Requires:       python3dist(feedgenerator) >= 2.1.0
Requires:       python3dist(jinja2) >= 3.1.2
Requires:       python3dist(ordered-set) >= 4.1.0
Requires:       python3dist(pygments) < 2.20.0
Requires:       python3dist(pygments) >= 2.16.1
Requires:       python3dist(python-dateutil) >= 2.8.2
Requires:       python3dist(rich) >= 13.6.0
Requires:       python3dist(unidecode) >= 1.3.7
Requires:       python3dist(watchfiles) >= 0.21.0
# /oreon:reqs
%description -n python3-pelican

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pelican-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pelican usr/lib/python3*/site-packages/pelican* usr/lib64/python3*/site-packages/pelican* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pelican* usr/lib64/python3*/site-packages/pelican* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pelican -f %{oreon_filedir}/python3-pelican.list

%changelog

%autochangelog
