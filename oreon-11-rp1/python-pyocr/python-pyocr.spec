%global source0_hash eff33d95032426a92640e56fa0d71b496ee531c1d341a15cc610610a7c5eac55

%global srcname pyocr

Name:           python-%{srcname}
Version:        0.8.5
Release:        %autorelease
Summary:        Python wrapper for OCR engines (Tesseract, Cuneiform, etc)

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/OpenPaperwork/pyocr
Source:         %pypi_source %{srcname}

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  tesseract
BuildRequires:  tesseract-osd
BuildRequires:  tesseract-langpack-fra
BuildRequires:  tesseract-langpack-jpn

%global _description \
A Python wrapper for Tesseract and Cuneiform

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(sphinx)

Recommends:     tesseract

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x dev

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=${PWD}/build/lib sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
export LANG=C.UTF-8
%{pytest} tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md ChangeLog html

%changelog
%autochangelog
