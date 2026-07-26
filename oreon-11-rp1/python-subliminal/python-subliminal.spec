%global source0_hash c7aca034332c254ab0e52b3d67d903a7f97cd614f115803269b7ba2e540f1db9

%global srcname subliminal

Name:           python-%{srcname}
Version:        2.1.0
Release:        23%{?dist}
Summary:        Python library to search and download subtitles
License:        MIT
URL:            https://github.com/Diaoul/subliminal
Source:         https://github.com/Diaoul/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Don't download sphinx interlink inventory files, instead use local ones (for those which are packaged)
Patch0:         python-subliminal_doc-inventories.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# Doc building
BuildRequires:  python3-appdirs
BuildRequires:  python3-docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-babelfish
BuildRequires:  python3-guessit
BuildRequires:  python3-sphinxcontrib-programoutput
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-click
BuildRequires:  python-guessit-doc
BuildRequires:  python3-rarfile
BuildRequires:  python3-stevedore
BuildRequires:  python3-enzyme
BuildRequires:  python3-pysrt
BuildRequires:  python3-dogpile-cache
BuildRequires:  python3-rebulk
# Tests disabled
#BuildRequires:  python3-pytest-runner
#BuildRequires:  python3-pytz
#BuildRequires:  python3-rarfile
#BuildRequires:  python3-appdirs
#BuildRequires:  python3-six
#BuildRequires:  python3-pysrt
#BuildRequires:  python3-pbr
#BuildRequires:  python3-enzyme
#BuildRequires:  python3-stevedore
#BuildRequires:  python3-dogpile-cache
#BuildRequires:  python3-sympy
#BuildRequires:  python3-vcrpy
#BuildRequires:  python3-pytest-pep8
#BuildRequires:  python3-pytest-flakes
#BuildRequires:  python3-pytest-cov
#BuildRequires:  python3-guessit

%global _description\
Subliminal is a Python library to search and download subtitles.\
It comes with an easy to use yet powerful CLI suitable for direct use or\
cron jobs.\
\
Subliminal uses multiple providers to give users a vast choice and have\
a better chance to find the best matching subtitles. Current supported\
providers are:\
\
 - Addic7ed\
 - LegendasTV\
 - NapiProjekt\
 - OpenSubtitles\
 - Podnapisi\
 - Shooter\
 - TheSubDB\
 - TvSubtitles

%description %_description

%package -n python3-%{srcname}
Summary:        %summary
%{?python_provide:%python_provide python3-%{srcname}}
Suggests:       %{name}-doc

%description -n python3-%{srcname} %_description

%package doc
Summary:        %summary

%description doc %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

pushd docs
# Add folder containing subliminal script to PATH
export SPHINXBUILD=sphinx-build-3
PYTHONPATH=%{buildroot}%{python3_sitelib} PATH=$PATH:%{buildroot}%{_bindir} %make_build html
PYTHONPATH=%{buildroot}%{python3_sitelib} PATH=$PATH:%{buildroot}%{_bindir} %make_build text
PYTHONPATH=%{buildroot}%{python3_sitelib} PATH=$PATH:%{buildroot}%{_bindir} %make_build man
find . -name .buildinfo -type f -delete
popd
install -D -m 0644 docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1

%check
# Tests disabled because they connect to online services
#%%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%{_bindir}/subliminal
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py*.egg-info

%files doc
%doc README.rst docs/_build/html docs/_build/text
%license LICENSE
%{_mandir}/man1/%{srcname}.1*

%changelog
%autochangelog
