%global source0_hash 2446eb14dfd491e4930521ea532706fff86f25e78783f7af84c05a9344153491

%bcond_without tests
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We would like to generate PDF documentation as a substitute, but have not
# been able to successfully build the Sphinx-generated LaTeX for this
# particular package.
%bcond_without doc_pdf

Name:           python-pdf2image
Version:        1.16.3
Release:        13%{?dist}
Summary:        Convert PDF to PIL Image object

License:        MIT
URL:            https://github.com/Belval/pdf2image
Source:         %{url}/archive/v.%{version}/pdf2image-v.%{version}.tar.gz

# Import memory_profiler only when it is enabled
# https://github.com/Belval/pdf2image/pull/269
Patch:          %{url}/pull/269.patch

BuildArch:      noarch

%global _description %{expand:
A wrapper around the pdftoppm and pdftocairo
command line tools to convert PDF to a PIL
Image list.}

%description %_description

%package -n python3-pdf2image
Summary:        %{summary}
BuildRequires:  python3-devel
Requires:  poppler

%if %{with tests}
BuildRequires:  python3dist(pytest) >= 3.7.1
BuildRequires:  poppler
%endif

%description -n python3-pdf2image %_description

%package doc
Summary:        Documentation and examples for %{name}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-recommonmark
BuildRequires:  latexmk
BuildRequires:  tex-xetex-bin
%endif

%description doc
%{summary}.

Full HTML documentation is available at
https://belval.github.io/pdf2image/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pdf2image-v.%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet -f'
%endif

%install
%pyproject_install
%pyproject_save_files pdf2image

%check
%if %{with tests}
%pytest tests.py
%endif

%files -n python3-pdf2image -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/pdf2image.pdf
%endif

%changelog
%autochangelog
