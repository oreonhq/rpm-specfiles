%global source0_hash f2649914d3067904effa2b4ce8d83aae994cd47008253311d5ae7949f467939f
Name:           python-subliminal
Version:        2.7.1
Release:        1%{?dist}
Summary:        Subtitles, faster than your thoughts
License:        MIT
URL:            https://github.com/Diaoul/subliminal
Source0:        https://files.pythonhosted.org/packages/source/s/subliminal/subliminal-%{version}.tar.gz
BuildArch:      noarch
Patch0:         python-subliminal_doc-inventories.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-subliminal = %{version}-%{release}
# /oreon:deps
%package -n       python3-subliminal+rar
Summary:        Metapackage for python3-subliminal rar extras
Requires:       python3-subliminal = %{version}-%{release}
Requires:       python3dist(rarfile) >= 2.7
Provides:       python3dist(subliminal[rar]) = %{version}-%{release}

%description -n python3-subliminal+rar
Metapackage for python3-subliminal rar extras.

%package -n       python3-subliminal+docs
Summary:        Metapackage for python3-subliminal docs extras
Requires:       python3-subliminal = %{version}-%{release}
Requires:       python3dist(sphinx) < 8.2
Requires:       python3dist(sphinx-rtd-theme) >= 2
Requires:       python3dist(vcrpy) >= 5
Provides:       python3dist(subliminal[docs]) = %{version}-%{release}

%description -n python3-subliminal+docs
Metapackage for python3-subliminal docs extras.

%package -n       python3-subliminal+tests
Summary:        Metapackage for python3-subliminal tests extras
Requires:       python3-subliminal = %{version}-%{release}
Requires:       python3dist(coverage[toml]) >= 7
Requires:       python3dist(pytest) >= 6.0
Requires:       python3dist(vcrpy) >= 5
Provides:       python3dist(subliminal[tests]) = %{version}-%{release}

%description -n python3-subliminal+tests
Metapackage for python3-subliminal tests extras.

%package -n       python3-subliminal+types
Summary:        Metapackage for python3-subliminal types extras
Requires:       python3-subliminal = %{version}-%{release}
Provides:       python3dist(subliminal[types]) = %{version}-%{release}

%description -n python3-subliminal+types
Metapackage for python3-subliminal types extras.

%package -n       python3-subliminal+dev
Summary:        Metapackage for python3-subliminal dev extras
Requires:       python3-subliminal = %{version}-%{release}
Requires:       python3dist(pre-commit) >= 2.9.3
Provides:       python3dist(subliminal[dev]) = %{version}-%{release}

%description -n python3-subliminal+dev
Metapackage for python3-subliminal dev extras.

%description

%package -n     python3-subliminal
Summary:        Subtitles, faster than your thoughts
# oreon:reqs
Requires:       python3dist(babelfish) >= 0.6.1
Requires:       python3dist(beautifulsoup4) >= 4.4.0
Requires:       python3dist(chardet) >= 5.0
Requires:       python3dist(click-option-group) >= 0.5.6
Requires:       python3dist(defusedxml) >= 0.7.1
Requires:       python3dist(dogpile.cache) >= 1.0
Requires:       python3dist(guessit) >= 3.0.0
Requires:       python3dist(knowit) >= 0.5.5
Requires:       python3dist(platformdirs) >= 3
Requires:       python3dist(pysubs2) >= 1.7
Requires:       python3dist(requests) >= 2.0
Requires:       python3dist(srt) >= 3.5
Requires:       python3dist(stevedore) >= 3.0
Requires:       python3dist(tomlkit) >= 0.13.2
# /oreon:reqs
%description -n python3-subliminal

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir subliminal-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-subliminal usr/lib/python3*/site-packages/subliminal* usr/lib64/python3*/site-packages/subliminal* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/subliminal* usr/lib64/python3*/site-packages/subliminal* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-subliminal -f %{oreon_filedir}/python3-subliminal.list

%changelog

%autochangelog
