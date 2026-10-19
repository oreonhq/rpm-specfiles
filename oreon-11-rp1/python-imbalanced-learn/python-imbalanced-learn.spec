%global source0_hash f80ce7eafbcece8686e32571bd12978546c729c3f277215bead61a906ce9afe4
Name:           python-imbalanced-learn
Version:        0.14.2
Release:        1%{?dist}
Summary:        Toolbox for imbalanced dataset in machine learning
License:        MIT
URL:            https://imbalanced-learn.org/
Source0:        https://files.pythonhosted.org/packages/source/i/imbalanced_learn/imbalanced_learn-%{version}.tar.gz
BuildArch:      noarch
Patch:          fix-scikit-learn-1.8-compat.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 71
BuildRequires:  python3dist(setuptools-scm[toml]) >= 8
Requires:       python3-imbalanced-learn = %{version}-%{release}
# /oreon:deps
%package -n       python3-imbalanced-learn+dev
Summary:        Metapackage for python3-imbalanced-learn dev extras
Requires:       python3-imbalanced-learn = %{version}-%{release}
Provides:       python3dist(imbalanced-learn[dev]) = %{version}-%{release}

%description -n python3-imbalanced-learn+dev
Metapackage for python3-imbalanced-learn dev extras.

%package -n       python3-imbalanced-learn+docs
Summary:        Metapackage for python3-imbalanced-learn docs extras
Requires:       python3-imbalanced-learn = %{version}-%{release}
Requires:       python3dist(pandas) >= 2.0.3
Requires:       python3dist(pandas) < 3
Requires:       python3dist(tensorflow) >= 2.16.1
Requires:       python3dist(tensorflow) < 3
Requires:       python3dist(matplotlib) >= 3.7.3
Requires:       python3dist(matplotlib) < 4
Requires:       python3dist(seaborn) >= 0.12.2
Requires:       python3dist(seaborn) < 1
Requires:       python3dist(memory-profiler) >= 0.61.0
Requires:       python3dist(memory-profiler) < 1
Requires:       python3dist(numpydoc) >= 1.5.0
Requires:       python3dist(numpydoc) < 2
Requires:       python3dist(sphinx) >= 8.0.2
Requires:       python3dist(sphinx) < 9
Requires:       python3dist(sphinx-gallery) >= 0.13.0
Requires:       python3dist(sphinx-gallery) < 1
Requires:       python3dist(sphinxcontrib-bibtex) >= 2.6.3
Requires:       python3dist(sphinxcontrib-bibtex) < 3
Requires:       python3dist(sphinx-copybutton) >= 0.5.2
Requires:       python3dist(sphinx-copybutton) < 1
Requires:       python3dist(pydata-sphinx-theme) >= 0.15.4
Requires:       python3dist(pydata-sphinx-theme) < 1
Requires:       python3dist(sphinx-design) >= 0.6.1
Requires:       python3dist(sphinx-design) < 1
Provides:       python3dist(imbalanced-learn[docs]) = %{version}-%{release}

%description -n python3-imbalanced-learn+docs
Metapackage for python3-imbalanced-learn docs extras.

%package -n       python3-imbalanced-learn+linters
Summary:        Metapackage for python3-imbalanced-learn linters extras
Requires:       python3-imbalanced-learn = %{version}-%{release}
Requires:       python3dist(black) == 23.3.0
Requires:       python3dist(ruff) == 0.14.2
Provides:       python3dist(imbalanced-learn[linters]) = %{version}-%{release}

%description -n python3-imbalanced-learn+linters
Metapackage for python3-imbalanced-learn linters extras.

%package -n       python3-imbalanced-learn+optional
Summary:        Metapackage for python3-imbalanced-learn optional extras
Requires:       python3-imbalanced-learn = %{version}-%{release}
Requires:       python3dist(pandas) >= 2.0.3
Requires:       python3dist(pandas) < 3
Provides:       python3dist(imbalanced-learn[optional]) = %{version}-%{release}

%description -n python3-imbalanced-learn+optional
Metapackage for python3-imbalanced-learn optional extras.

%package -n       python3-imbalanced-learn+tensorflow
Summary:        Metapackage for python3-imbalanced-learn tensorflow extras
Requires:       python3-imbalanced-learn = %{version}-%{release}
Requires:       python3dist(tensorflow) >= 2.16.1
Requires:       python3dist(tensorflow) < 3
Provides:       python3dist(imbalanced-learn[tensorflow]) = %{version}-%{release}

%description -n python3-imbalanced-learn+tensorflow
Metapackage for python3-imbalanced-learn tensorflow extras.

%package -n       python3-imbalanced-learn+keras
Summary:        Metapackage for python3-imbalanced-learn keras extras
Requires:       python3-imbalanced-learn = %{version}-%{release}
Requires:       python3dist(keras) >= 3.3.3
Requires:       python3dist(keras) < 4
Provides:       python3dist(imbalanced-learn[keras]) = %{version}-%{release}

%description -n python3-imbalanced-learn+keras
Metapackage for python3-imbalanced-learn keras extras.

%package -n       python3-imbalanced-learn+tests
Summary:        Metapackage for python3-imbalanced-learn tests extras
Requires:       python3-imbalanced-learn = %{version}-%{release}
Requires:       python3dist(packaging) >= 23.2
Requires:       python3dist(packaging) < 25
Requires:       python3dist(pytest) >= 7.2.2
Requires:       python3dist(pytest) < 9
Requires:       python3dist(pytest-cov) >= 4.1.0
Requires:       python3dist(pytest-cov) < 6
Requires:       python3dist(pytest-xdist) >= 3.5.0
Requires:       python3dist(pytest-xdist) < 4
Provides:       python3dist(imbalanced-learn[tests]) = %{version}-%{release}

%description -n python3-imbalanced-learn+tests
Metapackage for python3-imbalanced-learn tests extras.

%description

%package -n     python3-imbalanced-learn
Summary:        Toolbox for imbalanced dataset in machine learning
# oreon:reqs
Requires:       python3dist(joblib) < 2
Requires:       python3dist(joblib) >= 1.2.0
Requires:       python3dist(numpy) < 3
Requires:       python3dist(numpy) >= 1.25.2
Requires:       python3dist(scikit-learn) < 2
Requires:       python3dist(scikit-learn) >= 1.4.2
Requires:       python3dist(scipy) < 2
Requires:       python3dist(scipy) >= 1.11.4
Requires:       python3dist(sklearn-compat) < 0.2
Requires:       python3dist(sklearn-compat) >= 0.1.6
Requires:       python3dist(threadpoolctl) < 4
Requires:       python3dist(threadpoolctl) >= 2.0.0
# /oreon:reqs
%description -n python3-imbalanced-learn

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir imbalanced_learn-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-imbalanced-learn usr/lib/python3*/site-packages/imbalanced_learn* usr/lib64/python3*/site-packages/imbalanced_learn* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/imbalanced_learn* usr/lib64/python3*/site-packages/imbalanced_learn* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-imbalanced-learn -f %{oreon_filedir}/python3-imbalanced-learn.list

%changelog

%autochangelog
