%global source0_hash 288e3ca7d54b06f2ac191970bc275c1939cb46d450b255bf6718b04aa37ab4f7
Name:           python-beautifulsoup4
Version:        4.15.0
Release:        1%{?dist}
Summary:        Screen-scraping library
License:        MIT
URL:            https://www.crummy.com/software/BeautifulSoup/bs4/
Source0:        https://files.pythonhosted.org/packages/source/b/beautifulsoup4/beautifulsoup4-%{version}.tar.gz
BuildArch:      noarch
Patch11:        beautifulsoup4-4.14-disable-soupsieve.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-beautifulsoup4 = %{version}-%{release}
# /oreon:deps
%package -n       python3-beautifulsoup4+html5lib
Summary:        Metapackage for python3-beautifulsoup4 html5lib extras
Requires:       python3-beautifulsoup4 = %{version}-%{release}
Provides:       python3dist(beautifulsoup4[html5lib]) = %{version}-%{release}

%description -n python3-beautifulsoup4+html5lib
Metapackage for python3-beautifulsoup4 html5lib extras.

%package -n       python3-beautifulsoup4+lxml
Summary:        Metapackage for python3-beautifulsoup4 lxml extras
Requires:       python3-beautifulsoup4 = %{version}-%{release}
Provides:       python3dist(beautifulsoup4[lxml]) = %{version}-%{release}

%description -n python3-beautifulsoup4+lxml
Metapackage for python3-beautifulsoup4 lxml extras.

%package -n       python3-beautifulsoup4+chardet
Summary:        Metapackage for python3-beautifulsoup4 chardet extras
Requires:       python3-beautifulsoup4 = %{version}-%{release}
Provides:       python3dist(beautifulsoup4[chardet]) = %{version}-%{release}

%description -n python3-beautifulsoup4+chardet
Metapackage for python3-beautifulsoup4 chardet extras.

%package -n       python3-beautifulsoup4+cchardet
Summary:        Metapackage for python3-beautifulsoup4 cchardet extras
Requires:       python3-beautifulsoup4 = %{version}-%{release}
Provides:       python3dist(beautifulsoup4[cchardet]) = %{version}-%{release}

%description -n python3-beautifulsoup4+cchardet
Metapackage for python3-beautifulsoup4 cchardet extras.

%package -n       python3-beautifulsoup4+charset-normalizer
Summary:        Metapackage for python3-beautifulsoup4 charset-normalizer extras
Requires:       python3-beautifulsoup4 = %{version}-%{release}
Provides:       python3dist(beautifulsoup4[charset-normalizer]) = %{version}-%{release}

%description -n python3-beautifulsoup4+charset-normalizer
Metapackage for python3-beautifulsoup4 charset-normalizer extras.

%description

%package -n     python3-beautifulsoup4
Summary:        Screen-scraping library
# oreon:reqs
Requires:       python3dist(soupsieve) >= 1.6.1
Requires:       python3dist(typing-extensions) >= 4.0.0
# /oreon:reqs
%description -n python3-beautifulsoup4

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir beautifulsoup4-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-beautifulsoup4 usr/lib/python3*/site-packages/beautifulsoup4* usr/lib64/python3*/site-packages/beautifulsoup4* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/beautifulsoup4* usr/lib64/python3*/site-packages/beautifulsoup4* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-beautifulsoup4 -f %{oreon_filedir}/python3-beautifulsoup4.list

%changelog

%autochangelog
