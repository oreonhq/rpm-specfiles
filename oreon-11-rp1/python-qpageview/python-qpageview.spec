%global source0_hash 0034b5483abc44d358e47a746714533fdffadde2b864d1ce49aa1e652cc64ae2

%global pypi_name qpageview

Name:           python-%{pypi_name}
Version:        1.0.3
Release:        1%{?dist}
Summary:        Widget to display page-based documents for Qt6/PyQt6

License:        GPL-3.0-or-later AND GPL-2.0-or-later
URL:            https://github.com/frescobaldi/qpageview
Source0:        %{pypi_source %pypi_name}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-mdinclude)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3-pyqt6
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3-docs

%description
The qpageview module *qpageview* provides a page based document viewer widget
for Qt6/PyQt6.It has a flexible architecture potentionally supporting many
formats. Currently, it supports SVG documents, images, and, using the Poppler-
Qt6 binding, PDF documents.:: import qpageview from PyQt6.Qt import * a
QApplication([]) v qpageview.View() v.show() v.loadPdf("path/to/afile.pdf")
Homepage < •...

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
The qpageview module *qpageview* provides a page based document viewer widget
for Qt6/PyQt6.It has a flexible architecture potentionally supporting many
formats. Currently, it supports SVG documents, images, and, using the Poppler-
Qt6 binding, PDF documents.:: import qpageview from PyQt6.Qt import * a
QApplication([]) v qpageview.View() v.show() v.loadPdf("path/to/afile.pdf")
Homepage < •...

%package doc
Summary:        Documentation for qpageview
%description doc
Documentation for qpageview

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.python\.org/3', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
  -i docs/source/conf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files qpageview

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE docs/source/license.rst
%doc README.rst

%files doc
%doc html
%license LICENSE docs/source/license.rst

%changelog
%autochangelog
